#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_conasems as lib_conasems

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
CUT = './Automate/'

# if not os.path.isdir(CUT):
#     script = ROOT + 'scripts/mountCut.scpt'
#     parametros = ['osascript', script ]
#     retorno = subprocess.call(parametros)

receivers = ['lflrocha@gmail.com']

listas = [
    # 'http://automate.lflr.com.br:8080/automate/getConasemsPendentes',
    'https://conasems.beat-ti.com.br/getCongressoPendentes'
    # 'http://vmebc:8080/conasems/getCongressoPendentes',
]

itens = []
for lista in listas:
    itens = itens + automator.baixaLista(lista)

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
    local = CUT
    logger.info("%r - Baixando dados do item", titulo)

    if tipo == "Congresso Programacao":
        ID = 'congresso_programacao'
        JSX = ROOT + 'scripts/congresso_programacao.jsx'
        EXPORT = ROOT + 'export/congresso_programacao/'
        DESTINO = local + '/Conasems/Congresso/'
        SAIDA = lib_conasems.getCongressoProgramacao(dados)



    logger.info("%r - Preparando JSON", titulo)

    # SALVA ARQUIVO JSON
    if SAIDA:
        arq_projeto = TEMP + novo_projeto + '.json'
        with open(arq_projeto, 'w') as f:
            json.dump(SAIDA['dados'], f, indent=4, sort_keys=True)
        logger.info("%r - Salvando JSON", titulo)
    else:
        arq = requests.get(endereco+'/setWorkflowState?acao=erro')
        logger.info("%r - %r - Erro salvando JSON", titulo, arq)
        break

    # CRIA ARQUIVO AEP
    projetoAfter = TEMP + novo_projeto + '.aep'
    jsx = TEMP + novo_projeto + '.jsx'
    retorno = automator.copiaArquivo(JSX, jsx)
    retorno = automator.atualizaProjeto(jsx)
    logger.info("%r - %r - Atualizando o projeto JSX", titulo, retorno)

    if retorno != 0:
        arq = automator.alteraStatus(endereco, 'erro')
        logger.info("%r - %r - Erro atualizando o projeto JSX", titulo, arq)
        break

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
        if retorno != 0:
            arq = requests.get(endereco+'/setWorkflowState?acao=erro')
            break

        if 'renomear' in render.keys():
            os.rename(arquivo + '00000', arquivo)

        if 'converter' in render.keys():
            arquivo = automator.converter(render['converter'], arquivo)

        origem_aux = arquivo
        destino_aux = dest
        retorno = os.system("cp  %s  %s" % (origem_aux,  destino_aux))

        # retorno = automator.enviaCut(arquivo, dest)
        logger.info("%r - %r - Arte copiada para destino: " + arquivo, titulo, retorno)


    # FINALIZA
    arq = requests.get(endereco+'/setWorkflowState?acao=finalizar')
