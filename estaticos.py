#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_agencia_cards as lib_agencia_cards


import datetime
import json
import os
import requests
import shutil
from slugify import slugify
import logging
import subprocess


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

if not os.path.isdir(CUT):
    script = ROOT + 'scripts/mountCut.scpt'
    parametros = ['osascript', script ]
    retorno = subprocess.call(parametros)

receivers = ['luis.rocha@ebc.com.br']

listas = [
    'http://automator-prod01.ebc:8080/automator/getAgenciaPendentes',
    'http://automator-prod01.ebc:8080/automator2023/getRedesPendentes',
]

itens = []
for lista in listas:
    itens = itens + automator.baixaLista(lista)
    print(itens)

print(len(itens))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOGS + 'automatorcc.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("%r - Itens pendentes: ", len(itens))

for item in itens:
    endereco = item['endereco']
    # arq = automator.alteraStatus(endereco, 'gerar')

for item in itens:
    endereco = item['endereco']
    titulo = item['titulo']
    tipo = item['tipo']
    print(tipo)

    logger.info("%r - %r - Iniciando item", titulo, tipo)

    dados = automator.buscaDados(endereco)
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    local = CUT + dados['local']
    logger.info("%r - Baixando dados do item", titulo)

    EXPORT = ROOT + 'export/abr_cards/'
    DESTINO = local + '/Redes/ABrCards/'

    export = EXPORT + ano + '/' + mes + '/' + dia + '/'
    if not os.path.isdir(export):
        os.makedirs(export)

    # CRIA PASTA NO DESTINO
    dest = DESTINO + ano + '/' + mes + '/' + dia + '/'
    if not os.path.isdir(dest):
        os.makedirs(dest)

    # CRIA PASTA NO EXPORT

    if tipo == "ABr Card Link 1":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link01(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square01(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories01(dados, export)

    elif tipo == "ABr Card Link 2":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link02(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square02(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories02(dados, export)

    elif tipo == "ABr Card Link 3":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link03(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square03(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories03(dados, export)

    elif tipo == "ABr Card Link 4":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link04(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square04(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories04(dados, export)

    elif tipo == "ABr Card Link 5":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link05(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square05(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories05(dados, export)


    elif tipo == "Cards Modelo1":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link01(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square01(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories01(dados, export)

    elif tipo == "Cards Modelo2":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link02(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square02(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories02(dados, export)

    elif tipo == "Cards Modelo3":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link03(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square03(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories03(dados, export)

    elif tipo == "Cards Modelo4":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link04(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square04(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories04(dados, export)

    elif tipo == "Cards Modelo5":
        ARQ_GERADO1 = lib_agencia_cards.gera_modelo_link05(dados, export)
        ARQ_GERADO2 = lib_agencia_cards.gera_modelo_square05(dados, export)
        ARQ_GERADO3 = lib_agencia_cards.gera_modelo_stories05(dados, export)



    retorno = os.system("cp  %s  %s" % (ARQ_GERADO1,  dest))
    retorno = os.system("cp  %s  %s" % (ARQ_GERADO2,  dest))
    retorno = os.system("cp  %s  %s" % (ARQ_GERADO3,  dest))
    logger.info("%r - Arte copiada para destino: " +  titulo, retorno)

    # FINALIZA
    arq = requests.get(endereco+'/setWorkflowState?acao=finalizar')
