#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_gov_tempo as lib_gov_tempo
import libs.lib_tempo as lib_tempo

import datetime
import json
import os
import requests
import shutil
from slugify import slugify
import logging
import subprocess
import random



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
# CUT = './Automator/'

if not os.path.isdir(CUT):
    script = ROOT + 'scripts/mountCut.scpt'
    parametros = ['osascript', script ]
    retorno = subprocess.call(parametros)

receivers = ['luis.rocha@ebc.com.br']

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOGS + 'gov2024_onair_tempo.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

titulo = "Tempo - " + data_hora_str
tipo = "gov2024_onair_tempo"
local = "DF"

logger.info("%r - %r - Iniciando item", titulo, tipo)


ID = 'gov2024_onair_tempo'
JSX = ROOT + 'scripts/gov2024_onair_tempo.jsx'
EXPORT = ROOT + 'export/gov2024_onair_tempo/'
DESTINO = local + '/GovOnAir/'


estados_selecionados = random.sample(list(lib_tempo.codigo_estados.keys()), 10)

# Selecionar 2 cidades aleatórias para cada estado selecionado
resultado = {}
for estado in estados_selecionados:
    sigla_estado = lib_tempo.codigo_estados[estado]
    capital = next(capital for capital in lib_tempo.capitais_tempo if capital[3] == sigla_estado)
    cidades_do_estado = [cidade for cidade in lib_tempo.cidades_tempo if cidade[0][:2] == estado]
    cidades_selecionadas = random.sample(cidades_do_estado, 2) if cidades_do_estado else []
    resultado[sigla_estado] = [capital] + cidades_selecionadas



for n, item in enumerate(resultado):

    novo_projeto = ID + '_' + str(n) + '_' +  data_hora_str
    SAIDA = lib_gov_tempo.getGovOnAirTempo(data, novo_projeto, resultado[item])
    logger.info("%r - Preparando JSON", titulo)

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

    if retorno != 0:
        logger.info("%r - %r - Erro atualizando o projeto JSX", titulo, arq)

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
        nome_arquivo = render['arquivo']
        arquivo = export + render['arquivo']

        retorno = automator.geraArte(projetoAfter, comp, inicio, fim, om, arquivo)
        logger.info("%r - %r - Gerando Arte " + arquivo, titulo, retorno)

        if 'renomear' in render.keys():
            os.rename(arquivo + '00000', arquivo)

        if 'converter' in render.keys():
            arquivo = automator.converter(render['converter'], arquivo)

        origem_aux = arquivo
        destino_aux = dest
        retorno = os.system("cp  %s  %s" % (origem_aux,  destino_aux))

        # retorno = automator.enviaCut(arquivo, dest)
        logger.info("%r - %r - Arte copiada para destino: " + arquivo, titulo, retorno)
