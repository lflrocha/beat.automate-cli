#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import libs.lib_dados as lib_dados
import libs.lib_esportes2023 as lib_esportes

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
# CUT = './Automator/'

if not os.path.isdir(CUT):
    script = ROOT + 'scripts/mountCut.scpt'
    parametros = ['osascript', script ]
    retorno = subprocess.call(parametros)

receivers = ['luis.rocha@ebc.com.br']

listas = [
    'http://automator-prod01.ebc:8080/automator/getTVBrRadiosChamadaPendentes',
    'http://automator-prod01.ebc:8080/automator/getMarketingPendentes',
    'http://automator-prod01.ebc:8080/automator/getTVBrProgramacaoAgenciaPendentes',
    'http://automator-prod01.ebc:8080/automator/getTVBrProgramacao2022Pendentes',
    'http://automator-prod01.ebc:8080/automator/getRedesTiktokPendentes',
    'http://vmebc:8080/automator/getEsportes2023Pendentes',
    'http://vmebc:8080/automator/getGovInformaPendentes',

]

itens = []
for lista in listas:
    itens = itens + automator.baixaLista(lista)

print(itens)
print(len(itens))

for item in itens:
    endereco = item['endereco']
    # arq = automator.alteraStatus(endereco, 'gerar')

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

    # arq = automator.alteraStatus(endereco, 'gerar')
    logger.info("%r - Setando status para 'gerando'", titulo)

    dados = automator.buscaDados(endereco)
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    local = CUT + dados['local']
    logger.info("%r - Baixando dados do item", titulo)

    if tipo == "MKT Midia Indoor Agencia 2022":
        ID = 'mkt_midia_indoor_agencia_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_agencia_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_agencia_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_dados.getMktMidiaIndoorAgencia2022(dados)

    elif tipo == "MKT Midia Indoor TVBrasil 2022":
        ID = 'mkt_midia_indoor_tvbrasil_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_tvbrasil_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_tvbrasil_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_dados.getMktMidiaIndoorTVBrasil2022(dados)

    elif tipo == "MKT Midia Indoor TVBrasilPlay 2022":
        ID = 'mkt_midia_indoor_tvbrasilplay_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_tvbrasilplay_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_tvbrasilplay_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_dados.getMktMidiaIndoorTVBrasilPlay2022(dados)

    elif tipo == "MKT Midia Indoor RadioNacional 2022":
        ID = 'mkt_midia_indoor_radionacional_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_radionacional_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_radionacional_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_dados.getMktMidiaIndoorRadioNacional2022(dados)

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

    elif tipo == "TVBr Radios Chamada":
        ID = 'tvbr_radios_chamada'
        JSX = ROOT + 'scripts/tvbr_radios_chamada.jsx'
        EXPORT = ROOT + 'export/tvbr_radios_chamada/'
        DESTINO = local + '/TVBr_Radios_Chamada/'
        SAIDA = lib_dados.getTVBrRadiosChamada(dados)

    elif tipo == "Redes TikTok":
        ID = 'redes_tiktok'
        JSX = ROOT + 'scripts/redes_tiktok_vertical.jsx'
        EXPORT = ROOT + 'export/redes_tiktok/'
        DESTINO = local + '/Redes_Tiktok/'
        SAIDA = lib_dados.getRedesTiktok(dados)

    elif tipo == "Gov Informa Cor":
        ID = 'gov_informa_cor'
        JSX = ROOT + 'scripts/gov_informa_cor.jsx'
        EXPORT = ROOT + 'export/gov_informa_cor/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_dados.getGovInforma(dados)

    elif tipo == "Gov Informa PB":
        ID = 'gov_informa_pb'
        JSX = ROOT + 'scripts/gov_informa_pb.jsx'
        EXPORT = ROOT + 'export/gov_informa_pb/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_dados.getGovInforma(dados)

    elif tipo == "Esportes2023 Tabela Futebol":
        ID = 'esportes2023_tabela_futebol'
        JSX = ROOT + 'scripts/esportes2023_tabela_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_tabela_futebol/'
        DESTINO = local + '/Esportes2023/'
        SAIDA = lib_esportes.getEsportes2023TabelaFutebol(dados)


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
            # arq = requests.get(endereco+'/setWorkflowState?acao=erro')
            break

        if 'renomear' in render.keys():
            os.rename(arquivo + '00000', arquivo)

        if 'converter' in render.keys():
            arquivo = automator.converter(render['converter'], arquivo)

        origem_aux = arquivo
        destino_aux = dest
        retorno = os.system("cp  %s  %s" % (origem_aux,  destino_aux))
        # retorno = automator.enviaCut(arquivo, dest + nome_arquivo)
        logger.info("%r - %r - Arte copiada para destino: " + arquivo, titulo, retorno)


    # FINALIZA
    # arq = requests.get(endereco+'/setWorkflowState?acao=finalizar')
