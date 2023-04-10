# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
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

    print(dados_tabela)
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
