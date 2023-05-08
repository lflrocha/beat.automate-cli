# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json
import requests
import numpy as np

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def getEsportes2023TabelaFutebol(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    campeonato_id = variaveis['campeonato_id']
    campeonato_nome = variaveis['campeonato_nome']
    programa = variaveis['programa']

    r = requests.get('http://api-abtabelas.devel.ebc/?campeonato=' + campeonato_id)
    dados_tabela = r.json()

    tabela = dados_tabela['fases'][0]['dados'][0]['grupos']['Único']

    num_telas = int(len(tabela) / 10)
    if len(tabela) % 10 > 0:
        num_telas = num_telas + 1

    aux = np.array_split(tabela, num_telas)
    telas = []
    for grupo in aux:
        telas.append(grupo.tolist())

    aux_dados = {
        'programa': programa,
        'campeonato_id': campeonato_id,
        'campeonato_nome': campeonato_nome,
        'telas': telas
    }

    renders = []
    for tela in range(num_telas):
        renders.append(
        {
            "comp": "!render_%s" % str(tela),
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_%s.mov"  % str(tela + 1),
            # "converter": "MP4"
        })

    saida = {"dados": aux_dados, "renders": renders}
    return saida



def getEsportes2023ConfrontosFutebol(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    campeonato_id = variaveis['campeonato_id']
    campeonato_nome = variaveis['campeonato_nome']
    programa = variaveis['programa']
    data_inicio = variaveis['data_inicial'].split('-')
    data_inicio = data_inicio[2] + '/' + data_inicio[1] + '/' + data_inicio[0]
    data_fim = variaveis['data_final'].split('-')
    data_fim = data_fim[2] + '/' + data_fim[1] + '/' + data_fim[0]

    r = requests.get('http://api-jogosbrasileirao.devel.ebc/confrontos?data=%s&data_final=%s' % (data_inicio, data_fim))
    dados_tabela = r.json()

    subtitulo = ""
    dados = []
    for dado in dados_tabela:
        if dado['campeonato'] == campeonato_id:
            dados.append(dado)
            rodada = dado['rodada']
    if rodada:
        subtitulo = rodada

    num_telas = int(len(dados) / 4)
    if len(dados) % 4 > 0:
        num_telas = num_telas + 1

    aux = np.array_split(dados, num_telas)
    telas = []
    for grupo in aux:
        telas.append(grupo.tolist())

    aux_dados = {
        'programa': programa,
        'campeonato_id': campeonato_id,
        'campeonato_nome': campeonato_nome,
        'subtitulo': subtitulo,
        'jogos': telas
    }

    renders = []
    for tela in range(num_telas):
        renders.append(
        {
            "comp": "!render_%s" % str(tela),
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_%s.mov"  % str(tela + 1),
            # "converter": "MP4"
        })

    saida = {"dados": aux_dados, "renders": renders}
    return saida



def getEsportes2023ResultadosFutebol(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    campeonato_id = variaveis['campeonato_id']
    campeonato_nome = variaveis['campeonato_nome']
    programa = variaveis['programa']
    data_inicio = variaveis['data_inicial'].split('-')
    data_inicio = data_inicio[2] + '/' + data_inicio[1] + '/' + data_inicio[0]
    data_fim = variaveis['data_final'].split('-')
    data_fim = data_fim[2] + '/' + data_fim[1] + '/' + data_fim[0]


    r = requests.get('http://api-jogosbrasileirao.devel.ebc/confrontos?data=%s&data_final=%s' % (data_inicio, data_fim))
    dados_tabela = r.json()


    subtitulo = ""
    dados = []
    for dado in dados_tabela:
        if dado['campeonato'] == campeonato_id:
            dados.append(dado)
            rodada = dado['rodada']
    if rodada:
        subtitulo = rodada

    num_telas = int(len(dados) / 4)
    if len(dados) % 4 > 0:
        num_telas = num_telas + 1

    aux = np.array_split(dados, num_telas)
    telas = []
    for grupo in aux:
        telas.append(grupo.tolist())

    aux_dados = {
        'programa': programa,
        'campeonato_id': campeonato_id,
        'campeonato_nome': campeonato_nome,
        'subtitulo': subtitulo,
        'jogos': telas
    }

    renders = []
    for tela in range(num_telas):
        renders.append(
        {
            "comp": "!render_%s" % str(tela),
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_%s.mov"  % str(tela + 1),
            # "converter": "MP4"
        })

    saida = {"dados": aux_dados, "renders": renders}
    return saida
