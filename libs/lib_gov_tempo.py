# -*- coding: UTF-8 -*-

import libs.automator as automator
import requests
import os
import json
import random
import datetime
from PIL import Image


import libs.lib_tempo as lib_tempo

import xml.etree.ElementTree as ET
from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'




def getDadosTempo(hoje, amanha, cidades):
    # 2024-05-22
    saida = []
    for cidade in cidades:
        cod_ibge = cidade[0]
        nome = cidade[2]
        uf = cidade[3]
        # coordenadas = cidade[4]
        dados_chuva = lib_tempo.getInformacoesChuva(cod_ibge)
        dados_tempo_hoje = lib_tempo.getTempoCidadeDia(cod_ibge, hoje)
        dados_tempo_amanha = lib_tempo.getTempoCidadeDia(cod_ibge, amanha)

        chuva_hoje = dados_chuva['dados'][hoje]
        chuva_amanha = dados_chuva['dados'][amanha]

        aux = {}
        aux['cidade'] = nome
        aux['uf'] = uf
        aux['icone_hoje'] = dados_tempo_hoje['icone']
        aux['min_hoje'] = dados_tempo_hoje['minima']
        aux['max_hoje'] = dados_tempo_hoje['maxima']
        aux['chuva_hoje'] = chuva_hoje
        aux['icone_amanha'] = dados_tempo_amanha['icone']
        aux['min_amanha'] = dados_tempo_amanha['minima']
        aux['max_amanha'] = dados_tempo_amanha['maxima']
        aux['chuva_amanha'] = chuva_amanha
        saida.append(aux)
    return saida


def getGovOnAirTempo(data, novo_projeto, cidades):

    identificador = novo_projeto
    arquivo_saida = slugify(novo_projeto)

    str_hoje = data.strftime("%d/%m/%Y")
    amanha = data + datetime.timedelta(days=1)
    str_amanha = amanha.strftime("%d/%m/%Y")

    variaveis = getDadosTempo(str_hoje, str_amanha, cidades)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "900",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
