#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import libs.lib_educacao as lib_educacao
import libs.lib_esportes as lib_esportes
import libs.lib_gov as lib_gov
import libs.lib_marketing as lib_marketing
import libs.lib_programacao as lib_programacao
import libs.lib_redes as lib_redes
import libs.lib_reporter2023 as lib_reporter2023
import libs.lib_tempo_alertas as lib_tempo_alertas
import libs.lib_tempo_lista as lib_tempo_lista
import libs.lib_tempo_box as lib_tempo_box
import libs.lib_tempo_3dias as lib_tempo_3dias
import libs.lib_tempo_5dias as lib_tempo_5dias
import libs.lib_tempo_mapa as lib_tempo_mapa
import libs.lib_programacao2023 as lib_programacao2023
import libs.lib_canalgovprogramacao2023 as lib_canalgovprogramacao2023

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
    # 'http://automator-prod01.ebc:8080/automator/getMarketingPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrProgramacaoAgenciaPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrProgramacao2022Pendentes',
    # 'http://automator-prod01.ebc:8080/automator/getRedesTiktokPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getEsportes2023Pendentes',
    # 'http://automator-prod01.ebc:8080/automator/getEducacaoPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrRadiosChamadaPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getGovInformaPendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrTempo2023Pendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrRB2023Pendentes',
    # 'http://automator-prod01.ebc:8080/automator/getTVBrProgramacao2023Pendentes',
    #
    # 'http://automator-prod01.ebc:8080/automator2023/getTVBrReporterBrasilPendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getTVBrStadiumPendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getTVBrMDBPendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getTVBrProgramacao2023Pendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getCanalGov2023Pendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getCanalGovBrasilEmDiaPendentes',
    # 'http://automator-prod01.ebc:8080/automator2023/getMarketingPendentes',
    #

    'http://vmebc:8080/automator2023/getTVBrReporterBrasilPendentes',
    # 'http://vmebc:8080/automator2023/getTVBrStadiumPendentes',
    # 'http://vmebc:8080/automator2023/getCanalGovBrasilEmDiaPendentes',
    # 'http://vmebc:8080/automator2023/getTVBrReporterBrasilPendentes',


    # 'http://vmebc:8080/automator2023/getCanalGovOnAirPendentes',

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
    local = CUT + dados['local']
    logger.info("%r - Baixando dados do item", titulo)

    if tipo == "MKT Midia Indoor Agencia 2022":
        ID = 'mkt_midia_indoor_agencia_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_agencia_2023.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_agencia_2023/'
        DESTINO = local + '/Marketing/'
        SAIDA = lib_marketing.getMktMidiaIndoorAgencia2023(dados)

    elif tipo == "MKT Midia Indoor TVBrasil 2022":
        ID = 'mkt_midia_indoor_tvbrasil_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_tvbrasil_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_tvbrasil_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_marketing.getMktMidiaIndoorTVBrasil2022(dados)

    elif tipo == "MKT Midia Indoor TVBrasilPlay 2022":
        ID = 'mkt_midia_indoor_tvbrasilplay_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_tvbrasilplay_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_tvbrasilplay_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_marketing.getMktMidiaIndoorTVBrasilPlay2022(dados)

    elif tipo == "MKT Midia Indoor RadioNacional 2022":
        ID = 'mkt_midia_indoor_radionacional_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_radionacional_2022.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_radionacional_2022/'
        DESTINO = local + '/Marketing2/'
        SAIDA = lib_marketing.getMktMidiaIndoorRadioNacional2022(dados)

    elif tipo == "TVBr Programacao Chamadas 2022":
        ID = 'tvbr_programacao_chamadas_2022'
        JSX = ROOT + 'scripts/tvbr_programacao_chamadas_2022.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao_chamadas_2022/'
        DESTINO = local + '/TVBr_Programacao_Chamadas_2022/'
        SAIDA = lib_programacao.getTVBrProgramacaoChamadas2022(dados)

    elif tipo == "TVBr Programacao Agencia":
        ID = 'tvbr_programacao_destaque_agencia_2022'
        JSX = ROOT + 'scripts/tvbr_programacao_destaque_agencia_2022.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao_destaque_agencia_2022/'
        DESTINO = local + '/TVBr_Programacao_Agencia_2022/'
        SAIDA = lib_programacao.getTVBrProgramacaoDestaqueAgencia2022(dados)

    elif tipo == "TVBr Radios Chamada":
        ID = 'tvbr_radios_chamada'
        JSX = ROOT + 'scripts/tvbr_radios_chamada.jsx'
        EXPORT = ROOT + 'export/tvbr_radios_chamada/'
        DESTINO = local + '/TVBr_Radios_Chamada/'
        SAIDA = lib_programacao.getTVBrRadiosChamada(dados)

    elif tipo == "Redes TikTok":
        ID = 'redes_tiktok'
        JSX = ROOT + 'scripts/redes_tiktok_vertical.jsx'
        EXPORT = ROOT + 'export/redes_tiktok/'
        DESTINO = local + '/Redes_Tiktok/'
        SAIDA = lib_redes.getRedesTiktok(dados)

    elif tipo == "Gov Informa Cor":
        ID = 'gov_informa_cor'
        JSX = ROOT + 'scripts/gov_informa_cor.jsx'
        EXPORT = ROOT + 'export/gov_informa_cor/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_gov.getGovInforma(dados)

    elif tipo == "Gov Informa PB":
        ID = 'gov_informa_pb'
        JSX = ROOT + 'scripts/gov_informa_pb.jsx'
        EXPORT = ROOT + 'export/gov_informa_pb/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_gov.getGovInforma(dados)

    elif tipo == "Esportes2023 Tabela Futebol":
        ID = 'esportes2023_tabela_futebol'
        JSX = ROOT + 'scripts/esportes2023_tabela_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_tabela_futebol/'
        DESTINO = local + '/Esportes2023/'
        SAIDA = lib_esportes.getEsportes2023TabelaFutebol(dados)

    elif tipo == "Esportes2023 Confrontos Futebol":
        ID = 'esportes2023_confrontos_futebol'
        JSX = ROOT + 'scripts/esportes2023_confrontos_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/Esportes2023/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosFutebol(dados)

    elif tipo == "Esportes2023 Resultados Futebol":
        ID = 'esportes2023_resultados_futebol'
        JSX = ROOT + 'scripts/esportes2023_resultados_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_futebol/'
        DESTINO = local + '/Esportes2023/'
        SAIDA = lib_esportes.getEsportes2023ResultadosFutebol(dados)

    elif tipo == "Educacao Bussola Hoje":
        ID = 'educacao_bussola_hoje'
        JSX = ROOT + 'scripts/educacao_bussola_hoje.jsx'
        EXPORT = ROOT + 'export/educacao_bussola_hoje/'
        DESTINO = local + '/CanalEducacao/'
        SAIDA = lib_educacao.getEducacaoBussolaHoje(dados)

    elif tipo == "Educacao Bussola Assista":
        ID = 'educacao_bussola_assista'
        JSX = ROOT + 'scripts/educacao_bussola_assista.jsx'
        EXPORT = ROOT + 'export/educacao_bussola_assista/'
        DESTINO = local + '/CanalEducacao/'
        SAIDA = lib_educacao.getEducacaoBussolaAssista(dados)

    elif tipo == "Educacao Chamada Simples":
        ID = 'educacao_chamada_simples'
        JSX = ROOT + 'scripts/educacao_chamada_simples.jsx'
        EXPORT = ROOT + 'export/educacao_chamada_simples/'
        DESTINO = local + '/CanalEducacao/'
        SAIDA = lib_educacao.getEducacaoChamadaSimples(dados)

    elif tipo == "TVBr Tempo2023 Alerta":
        ID = 'tvbr_tempo2023_alerta'
        JSX = ROOT + 'scripts/tvbr_tempo2023_alerta.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_alerta/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_alertas.getTempoAlertas(dados)

    elif tipo == "TVBr Tempo2023 Lista":
        ID = 'tvbr_tempo2023_lista'
        JSX = ROOT + 'scripts/tvbr_tempo2023_lista.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_lista/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_lista.getTempoLista(dados)

    elif tipo == "TVBr Tempo2023 Box":
        ID = 'tvbr_tempo2023_box'
        JSX = ROOT + 'scripts/tvbr_tempo2023_box.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_box/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_box.getTempoBox(dados)

    elif tipo == "TVBr Tempo2023 3Dias":
        ID = 'tvbr_tempo2023_3dias'
        JSX = ROOT + 'scripts/tvbr_tempo2023_3dias.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_3dias/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_3dias.getTempo3Dias(dados)

    elif tipo == "TVBr Tempo2023 5Dias":
        ID = 'tvbr_tempo2023_5dias'
        JSX = ROOT + 'scripts/tvbr_tempo2023_5dias.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_5dias/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_5dias.getTempo5Dias(dados)

    elif tipo == "TVBr Tempo2023 Mapa":
        ID = 'tvbr_tempo2023_mapa'
        JSX = ROOT + 'scripts/tvbr_tempo2023_mapa.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_mapa/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_mapa.getTempoMapa(dados)

    elif tipo == "TVBr Reporter2023 Focus":
        ID = 'tvbr_reporter2023_focus'
        JSX = ROOT + 'scripts/tvbr_reporter2023_focus.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_focus/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getFocus(dados)

    elif tipo == "TVBr Reporter2023 Lista":
        ID = 'tvbr_reporter2023_lista'
        JSX = ROOT + 'scripts/tvbr_reporter2023_lista.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_lista/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getLista(dados)

    elif tipo == "TVBr Reporter2023 Destaque Agencia":
        ID = 'tvbr_reporter2023_destaque_agencia'
        JSX = ROOT + 'scripts/tvbr_reporter2023_destaque_agencia.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_destaque_agencia/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getDestaqueAgencia(dados)

    elif tipo == "TVBr Programacao2023 Bussola":
        ID = 'tvbr_programacao2023_bussola'
        JSX = ROOT + 'scripts/tvbr_programacao2023_bussolas.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao2023_bussola/'
        DESTINO = local + '/TVBr_Programacao2023/'
        SAIDA = lib_programacao2023.getBussolas(dados)

    elif tipo == "CanalGov Twitter 2023":
        ID = 'canalgov_programacao2023_twitter'
        JSX = ROOT + 'scripts/canalgov_programacao2023_twitter.jsx'
        EXPORT = ROOT + 'export/canalgov_programacao2023_twitter/'
        DESTINO = local + '/CanalGov_Programacao2023/'
        SAIDA = lib_canalgovprogramacao2023.getTwitter2023(dados)


    ###############################################################################
    # NOVOS
    ###############################################################################



    elif tipo == "MidiaIndoor Agencia Brasil":
        ID = 'mkt_midia_indoor_agencia_2022'
        JSX = ROOT + 'scripts/mkt_midia_indoor_agencia_2023.jsx'
        EXPORT = ROOT + 'export/mkt_midia_indoor_agencia_2023/'
        DESTINO = local + '/Marketing/'
        SAIDA = lib_marketing.getMktMidiaIndoorAgencia2023(dados)

    elif tipo == "RB2023 Album":
        print("entrou")
        ID = 'tvbr_reporter2023_album'
        JSX = ROOT + 'scripts/tvbr_reporter2023_album.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_album/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getAlbum(dados)

    elif tipo == "RB2023 Boletim Focus":
        ID = 'tvbr_reporter2023_focus'
        JSX = ROOT + 'scripts/tvbr_reporter2023_focus.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_focus/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getFocus(dados)

    elif tipo == "RB2023 Lista":
        ID = 'tvbr_reporter2023_lista'
        JSX = ROOT + 'scripts/tvbr_reporter2023_lista.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_lista/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getLista(dados)

    elif tipo == "RB2023 Destaque Agencia Brasil":
        ID = 'tvbr_reporter2023_destaque_agencia'
        JSX = ROOT + 'scripts/tvbr_reporter2023_destaque_agencia.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_destaque_agencia/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_reporter2023.getDestaqueAgencia(dados)

    elif tipo == "RB2023 Tempo Alerta":
        ID = 'tvbr_tempo2023_alerta'
        JSX = ROOT + 'scripts/tvbr_tempo2023_alerta.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_alerta/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_alertas.getTempoAlertas(dados)

    elif tipo == "RB2023 Tempo Lista":
        ID = 'tvbr_tempo2023_lista'
        JSX = ROOT + 'scripts/tvbr_tempo2023_lista.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_lista/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_lista.getTempoLista(dados)

    elif tipo == "RB2023 Tempo Box":
        ID = 'tvbr_tempo2023_box'
        JSX = ROOT + 'scripts/tvbr_tempo2023_box.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_box/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_box.getTempoBox(dados)

    elif tipo == "RB2023 Tempo Box 3 Cidades":
        ID = 'tvbr_tempo2023_box_3cidades'
        JSX = ROOT + 'scripts/tvbr_tempo2023_box_3cidades.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_box_3cidades/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_box.getTempoBox3Cidades(dados)

    elif tipo == "RB2023 Tempo 3Dias":
        ID = 'tvbr_tempo2023_3dias'
        JSX = ROOT + 'scripts/tvbr_tempo2023_3dias.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_3dias/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_3dias.getTempo3Dias(dados)

    elif tipo == "RB2023 Tempo 3Dias 2Cidades":
        ID = 'tvbr_tempo2023_3dias_2cidades'
        JSX = ROOT + 'scripts/tvbr_tempo2023_3dias_2cidades.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_3dias_2cidades/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_3dias.getTempo3Dias2Cidades(dados)

    elif tipo == "RB2023 Tempo 5Dias":
        ID = 'tvbr_tempo2023_5dias'
        JSX = ROOT + 'scripts/tvbr_tempo2023_5dias.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_5dias/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_5dias.getTempo5Dias(dados)

    elif tipo == "RB2023 Tempo Mapa":
        ID = 'tvbr_tempo2023_mapa'
        JSX = ROOT + 'scripts/tvbr_tempo2023_mapa.jsx'
        EXPORT = ROOT + 'export/tvbr_tempo2023_mapa/'
        DESTINO = local + '/TVBr_Tempo2023/'
        SAIDA = lib_tempo_mapa.getTempoMapa(dados)

    elif tipo == "RB2023 Futebol Confrontos Feminino":
        ID = 'tvbr_reporter2023_futebol_confrontos_feminino'
        JSX = ROOT + 'scripts/tvbr_reporter2023_confrontos_manual_futebol.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_futebol_confrontos/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_esportes.getRB2023ResultadosManualFutebol(dados)

    elif tipo == "RB2023 Futebol Confrontos Masculino":
        ID = 'tvbr_reporter2023_futebol_confrontos_masculino'
        JSX = ROOT + 'scripts/tvbr_reporter2023_confrontos_manual_futebol.jsx'
        EXPORT = ROOT + 'export/tvbr_reporter2023_futebol_confrontos/'
        DESTINO = local + '/TVBr_Reporter2023/'
        SAIDA = lib_esportes.getRB2023ResultadosManualFutebol(dados)





    elif tipo == "Stadium Tabelas":
        ID = 'esportes2023_tabela_futebol'
        JSX = ROOT + 'scripts/esportes2023_tabela_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_tabela_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023TabelaFutebol(dados)

    elif tipo == "Stadium Confrontos":
        ID = 'esportes2023_confrontos_futebol'
        JSX = ROOT + 'scripts/esportes2023_confrontos_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosFutebol(dados)

    elif tipo == "Stadium Confrontos Manual Volei":
        ID = 'esportes2023_confrontos_manual_volei'
        JSX = ROOT + 'scripts/esportes2023_confrontos_manual_volei.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_volei/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosManualVolei(dados)

    elif tipo == "Stadium Confrontos Manual Futebol Brasil":
        ID = 'esportes2023_confrontos_manual_futebol_brasil'
        JSX = ROOT + 'scripts/esportes2023_confrontos_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosManualFutebol(dados)

    elif tipo == "Stadium Confrontos Manual Futebol Feminino":
        ID = 'esportes2023_confrontos_manual_futebol_feminino'
        JSX = ROOT + 'scripts/esportes2023_confrontos_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosManualFutebol(dados)

    elif tipo == "Stadium Confrontos Manual Futebol America":
        ID = 'esportes2023_confrontos_manual_futebol_america'
        JSX = ROOT + 'scripts/esportes2023_confrontos_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosManualFutebol(dados)

    elif tipo == "Stadium Confrontos Manual NBA":
        ID = 'esportes2023_confrontos_manual_nba'
        JSX = ROOT + 'scripts/esportes2023_confrontos_manual_nba.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_nba/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosManualNBA(dados)


    elif tipo == "Stadium Resultados":
        ID = 'esportes2023_resultados_futebol'
        JSX = ROOT + 'scripts/esportes2023_resultados_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_futebol/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosFutebol(dados)

    elif tipo == "Stadium Resultados Manual NBA":
        ID = 'esportes2023_resultados_manual_nba'
        JSX = ROOT + 'scripts/esportes2023_resultados_manual_nba.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_manual_nba/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosManualNBA(dados)

    elif tipo == "Stadium Resultados Manual Volei":
        ID = 'esportes2023_resultados_manual_volei'
        JSX = ROOT + 'scripts/esportes2023_resultados_manual_volei.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_manual_volei/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosManualVolei(dados)

    elif tipo == "Stadium Resultados Manual Futebol Brasil":
        ID = 'esportes2023_resultados_manual_futebol_brasil'
        JSX = ROOT + 'scripts/esportes2023_resultados_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_manual_futebol_brasil/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosManualFutebol(dados)

    elif tipo == "Stadium Resultados Manual Futebol Feminino":
        ID = 'esportes2023_resultados_manual_futebol_feminino'
        JSX = ROOT + 'scripts/esportes2023_resultados_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_manual_futebol_feminino/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosManualFutebol(dados)

    elif tipo == "Stadium Resultados Manual Futebol America":
        ID = 'esportes2023_resultados_manual_futebol_america'
        JSX = ROOT + 'scripts/esportes2023_resultados_manual_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_manual_futebol_america/'
        DESTINO = local + '/TVBr_Stadium/'
        SAIDA = lib_esportes.getEsportes2023ResultadosManualFutebol(dados)

    elif tipo == "MDB Tabela":
        ID = 'esportes2023_tabela_futebol'
        JSX = ROOT + 'scripts/esportes2023_tabela_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_tabela_futebol/'
        DESTINO = local + '/TVBr_MDB/'
        SAIDA = lib_esportes.getEsportes2023TabelaFutebol(dados)

    elif tipo == "MDB Confrontos":
        ID = 'esportes2023_confrontos_futebol'
        JSX = ROOT + 'scripts/esportes2023_confrontos_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_confrontos_futebol/'
        DESTINO = local + '/TVBr_MDB/'
        SAIDA = lib_esportes.getEsportes2023ConfrontosFutebol(dados)

    elif tipo == "MDB Resultados":
        ID = 'esportes2023_resultados_futebol'
        JSX = ROOT + 'scripts/esportes2023_resultados_futebol.jsx'
        EXPORT = ROOT + 'export/esportes2023_resultados_futebol/'
        DESTINO = local + '/TVBr_MDB/'
        SAIDA = lib_esportes.getEsportes2023ResultadosFutebol(dados)

    elif tipo == "Programacao Bussolas":
        ID = 'tvbr_programacao2023_bussola'
        JSX = ROOT + 'scripts/tvbr_programacao2023_bussolas.jsx'
        EXPORT = ROOT + 'export/tvbr_programacao2023_bussola/'
        DESTINO = local + '/TVBr_Programacao/'
        SAIDA = lib_programacao2023.getBussolas(dados)

    elif tipo == "GovInforma Cor":
        ID = 'gov_informa_cor'
        JSX = ROOT + 'scripts/gov_informa_cor.jsx'
        EXPORT = ROOT + 'export/gov_informa_cor/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_gov.getGovInforma(dados)

    elif tipo == "GovInforma PB":
        ID = 'gov_informa_pb'
        JSX = ROOT + 'scripts/gov_informa_pb.jsx'
        EXPORT = ROOT + 'export/gov_informa_pb/'
        DESTINO = local + '/GovInforma/'
        SAIDA = lib_gov.getGovInforma(dados)

    elif tipo == "Gov Twitter":
        ID = 'gov_twitter'
        JSX = ROOT + 'scripts/gov_twitter.jsx'
        EXPORT = ROOT + 'export/gov_twitter/'
        DESTINO = local + '/GovBrasilEmDia/'
        SAIDA = lib_gov.getGovTwitter(dados)

    elif tipo == "Gov Instagram":
        ID = 'gov_instagram'
        JSX = ROOT + 'scripts/gov_instagram.jsx'
        EXPORT = ROOT + 'export/gov_instagram/'
        DESTINO = local + '/GovBrasilEmDia/'
        SAIDA = lib_gov.getGovInstagram(dados)

    elif tipo == "Gov Destaque ABr":
        ID = 'gov_destaque_abr'
        JSX = ROOT + 'scripts/gov_destaque_abr.jsx'
        EXPORT = ROOT + 'export/gov_destaque_abr/'
        DESTINO = local + '/GovBrasilEmDia/'
        SAIDA = lib_gov.getGovDestaqueABr(dados)

    elif tipo == "Gov Destaque AgGov":
        ID = 'gov_destaque_aggov'
        JSX = ROOT + 'scripts/gov_destaque_aggov.jsx'
        EXPORT = ROOT + 'export/gov_destaque_aggov/'
        DESTINO = local + '/GovBrasilEmDia/'
        SAIDA = lib_gov.getGovDestaqueAgGov(dados)


    elif tipo == "Gov OnAir DaquiAPouco":
        ID = 'gov2024_onair_daquiapouco'
        JSX = ROOT + 'scripts/gov2024_onair_daquiapouco.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_daquiapouco/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirDaquiAPouco(dados)

    elif tipo == "Gov OnAir ASeguir":
        ID = 'gov2024_onair_aseguir'
        JSX = ROOT + 'scripts/gov2024_onair_aseguir.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_aseguir/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirASeguir(dados)

    elif tipo == "Gov OnAir Bussola1":
        ID = 'gov2024_onair_bussola1'
        JSX = ROOT + 'scripts/gov2024_onair_bussola1.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_bussola1/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirBussola1(dados)

    elif tipo == "Gov OnAir Bussola2":
        ID = 'gov2024_onair_bussola2'
        JSX = ROOT + 'scripts/gov2024_onair_bussola2.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_bussola2/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirBussola2(dados)


    elif tipo == "Gov OnAir Bussola3":
        ID = 'gov2024_onair_bussola3'
        JSX = ROOT + 'scripts/gov2024_onair_bussola3.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_bussola3/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirBussola3(dados)

    elif tipo == "Gov OnAir HorarioAlternativo":
        ID = 'gov2024_onair_horarioalternativo'
        JSX = ROOT + 'scripts/gov2024_onair_horarioalternativo.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_horarioalternativo/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirHorarioAlternativo(dados)

    elif tipo == "Gov OnAir Citacao":
        ID = 'gov2024_onair_citacao'
        JSX = ROOT + 'scripts/gov2024_onair_citacao.jsx'
        EXPORT = ROOT + 'export/gov2024_onair_citacao/'
        DESTINO = local + '/GovOnAir/'
        SAIDA = lib_gov.getGovOnAirCitacao(dados)






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
