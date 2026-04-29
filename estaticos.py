#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_redes_cards as lib_redes_cards


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

receivers = ['luis.rocha@ebc.com.br']

listas = [
    'http://172.105.152.165:8080/automate/getRedesPendentes',
    # 'http://vmebc:8080/automator2023/getRedesPendentes',
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
    arq = automator.alteraStatus(endereco, 'gerar')

for item in itens:
    endereco = item['endereco']
    titulo = item['titulo']
    tipo = item['tipo']
    print(tipo)

    logger.info("%r - %r - Iniciando item", titulo, tipo)

    dados = automator.buscaDados(endereco)
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    logger.info("%r - Baixando dados do item", titulo)

    EXPORT = ROOT + 'export/abr_cards/'

    export = EXPORT + ano + '/' + mes + '/' + dia + '/'
    if not os.path.isdir(export):
        os.makedirs(export)

    if tipo == "Boletim":
        ARQ_GERADO1 = lib_redes_cards.gera_modelo_boletim(dados, export)

    elif tipo == "Nota":
        ARQ_GERADO1 = lib_redes_cards.gera_modelo_nota(dados, export)


    # FINALIZA
    arq = requests.get(endereco+'/setWorkflowState?acao=finalizar')
    print(endereco+'/setWorkflowState?acao=finalizar')
