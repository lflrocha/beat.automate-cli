#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import libs.lib_dados as lib_dados

import datetime
import json
import os
import requests
from slugify import slugify
import logging

ROOT = automator.getBase()

data = datetime.datetime.now()
diaSemana = data.weekday()
ano = data.strftime('%Y')
mes = data.strftime('%m')
dia = data.strftime('%d')
data_hora_str = data.strftime("%Y%m%d%H%M%S")


ARQUIVOS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
CUT = '/Volumes/Automator/'
CUT = './Automator/'

receivers = ['luis.rocha@ebc.com.br']

url_consolidado = "http://simulador.ebc/json/dev/2022/federal/primeiro-turno/complemento/governador/estados.json"
local = "DF"
ID = 'tvbr_eleicoes2022_mapa_governador'
tipo = ID
JSX = ROOT + 'scripts/tvbr_eleicoes2022_mapa_governador.jsx'
EXPORT = ROOT + 'export/tvbr_eleicoes2022_mapa_governador/'
DESTINO = local + '/TVBr_Eleicoes2022/'

titulo = "Mapa Governador"
identificador = titulo + " " + data_hora_str
novo_projeto = data_hora_str + '_' + ID

dados = {
    "novo_projeto": novo_projeto,
    "identificador": identificador,
    "url_consolidado": url_consolidado,
    "data_hora": data_hora_str
}

SAIDA = lib_dados.getTVBrEleicoes2022MapaGovernador(dados)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOGS + tipo + '.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("%r - %r - Iniciando item", titulo, tipo)

# SALVA ARQUIVO JSON
logger.info("%r - Preparando JSON", titulo)
if SAIDA:
    arq_projeto = TEMP + novo_projeto + '.json'
    with open(arq_projeto, 'w') as f:
        json.dump(SAIDA['dados'], f, indent=4, sort_keys=True)
    logger.info("%r - Salvando JSON", titulo)

# CRIA ARQUIVO AEP
projetoAfter = TEMP + novo_projeto + '.aep'
jsx = TEMP + novo_projeto + '.jsx'
retorno = automator.copiaArquivo(JSX, jsx)
retorno = automator.atualizaProjeto(jsx)
logger.info("%r - %r - Atualizando o projeto JSX", titulo, retorno)

# CRIA PASTA NO EXPORT
export = EXPORT + ano + '/' + mes + '/' + dia + '/'
if not os.path.isdir(export):
    os.makedirs(export)

# CRIA PASTA NO DESTINO
dest = DESTINO + ano + '/' + mes + '/' + dia + '/'
if not os.path.isdir(dest):
    os.makedirs(dest)

renders = SAIDA['renders']
for render in renders:
    comp = render['comp']
    inicio  = render['inicio']
    fim = render['fim']
    om = render['OM']
    arquivo = export + render['arquivo']

    print(render)
    retorno = automator.geraArte(projetoAfter, comp, inicio, fim, om, arquivo)
    logger.info("%r - %r - Gerando Arte " + arquivo, titulo, retorno)

    if 'renomear' in render.keys():
        print(arquivo)
        os.rename(arquivo + '00000', arquivo)

    if 'converter' in render.keys():
        arquivo = automator.converter(render['converter'], arquivo)
        print(arquivo)

    cmd = "cp " + arquivo + "  /Users/lflrocha/Sistemas/ebc.eleicoes2022/saida/MAPA_GOVERNADORES.png"
    aux = os.system(cmd)
