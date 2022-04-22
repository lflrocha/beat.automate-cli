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
CUT = '/Volumes/CUT/Automator/'

receivers = ['luis.rocha@ebc.com.br']

listas = [
    'http://automator-prod01.ebc:8080/automator/getMarketingPendentes',
    'http://automator-prod01.ebc:8080/automator/getTVBrProgramacaoAgenciaPendentes',
    'http://automator-prod01.ebc:8080/automator/getTVBrProgramacao2022Pendentes',
]

itens = []
for lista in listas:
    itens = itens + automator.baixaLista(lista)

print(itens)
print(len(itens))

for item in itens:
    arq = automator.alteraStatus(endereco, 'gerar')
    

for item in itens:
    endereco = item['endereco']
    titulo = item['titulo']
    tipo = item['tipo']
    print(tipo)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(LOGS + tipo + '.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("%r - %r - Iniciando item", titulo, tipo)

    arq = automator.alteraStatus(endereco, 'gerar')
    logger.info("%r - Setando status para 'gerando'", titulo)

    dados = automator.buscaDados(endereco)
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    local = dados['local']
    logger.info("%r - Baixando dados do item", titulo)

    if tipo == "MKT Midia Indoor Agencia 2022":
        ID = 'mkt_midia_indoor_agencia_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_agencia_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_agencia_2022/'
        DESTINO = local + '/Marketing/'
        SAIDA = lib_dados.getMktMidiaIndoorAgencia2022(dados)

    elif tipo == "TVBr Programacao Chamadas 2022":
        ID = 'tvbr_programacao_chamadas_2022'
        JSX = ROOT + 'scripts/tvbr_programacao_chamadas_2022.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao_chamadas_2022/'
        DESTINO = local + '/TVBr_Programacao_Chamadas_2022/'
        SAIDA = lib_dados.getTVBrProgramacaoChamadas2022(dados)

    elif tipo == "TVBr Programacao Agencia":
        ID = 'tvbr_programacao_destaque_agencia_2022'
        JSX = ROOT + 'scripts/tvbr_programacao_destaque_agencia_2022.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao_destaque_agencia_2022/'
        DESTINO = local + '/TVBr_Programacao_Agencia_2022/'
        SAIDA = lib_dados.getTVBrProgramacaoDestaqueAgencia2022(dados)

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
        arquivo = export + render['arquivo']

        print(render)

        retorno = automator.geraArte(projetoAfter, comp, inicio, fim, om, arquivo)
        logger.info("%r - %r - Gerando Arte " + arquivo, titulo, retorno)
        if retorno != 0:
            arq = requests.get(endereco+'/setWorkflowState?acao=erro')
            break

        if 'renomear' in render.keys():
            os.rename(arquivo + '00000', arquivo)

        if 'converter' in render.keys():
            arquivo = automator.converter(render['converter'], arquivo)
            print(arquivo)

        # retorno = automator.enviaCut(arquivo, dest)
        logger.info("%r - %r - Arte copiada para destino: " + arquivo, titulo, retorno)


    # FINALIZA
    arq = requests.get(endereco+'/setWorkflowState?acao=finalizar')
