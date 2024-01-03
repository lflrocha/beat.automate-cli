# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_tempo as lib_tempo
import urllib
import os
import json
import requests
import datetime
import xml.etree.ElementTree as ET
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def getTempo3Dias(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    data = variaveis['data']
    data1 = datetime.datetime.strptime(data, '%d/%m/%Y')
    data2 = data1 + datetime.timedelta(days=1)
    data3 = data1 + datetime.timedelta(days=2)

    aux = lib_tempo.getDadosCidade(variaveis['cidade'])
    dia1 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data1.strftime("%d/%m/%Y"))
    dia2 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data2.strftime("%d/%m/%Y"))
    dia3 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data3.strftime("%d/%m/%Y"))

    dia1_semana = automator.DIAS_SEMANA[data1.weekday()]
    dia1['dia_semana'] = dia1_semana.upper()
    dia2_semana = automator.DIAS_SEMANA[data2.weekday()]
    dia2['dia_semana'] = dia2_semana.upper()
    dia3_semana = automator.DIAS_SEMANA[data3.weekday()]
    dia3['dia_semana'] = dia3_semana.upper()

    cidade = aux[2] + '-' + aux[3]

    saida = {}
    saida['modelo'] = variaveis['modelo']
    saida['cidade'] = cidade.upper()
    saida['dia1'] = dia1
    saida['dia2'] = dia2
    saida['dia3'] = dia3

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": saida, "renders": renders}
    return saida




def getTempo3Dias2Cidades(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    data = variaveis['data']
    data1 = datetime.datetime.strptime(data, '%d/%m/%Y')
    data2 = data1 + datetime.timedelta(days=1)
    data3 = data1 + datetime.timedelta(days=2)

    aux = lib_tempo.getDadosCidade(variaveis['cidade1'])
    c1dia1 = lib_tempo.getTempoCidadeDia(variaveis['cidade1'], data1.strftime("%d/%m/%Y"))
    c1dia2 = lib_tempo.getTempoCidadeDia(variaveis['cidade1'], data2.strftime("%d/%m/%Y"))
    c1dia3 = lib_tempo.getTempoCidadeDia(variaveis['cidade1'], data3.strftime("%d/%m/%Y"))

    c1dia1_semana = automator.DIAS_SEMANA[data1.weekday()]
    c1dia1['dia_semana'] = c1dia1_semana.upper()
    c1dia2_semana = automator.DIAS_SEMANA[data2.weekday()]
    c1dia2['dia_semana'] = c1dia2_semana.upper()
    c1dia3_semana = automator.DIAS_SEMANA[data3.weekday()]
    c1dia3['dia_semana'] = c1dia3_semana.upper()

    cidade1 = aux[2] + '-' + aux[3]



    aux = lib_tempo.getDadosCidade(variaveis['cidade2'])
    c2dia1 = lib_tempo.getTempoCidadeDia(variaveis['cidade2'], data1.strftime("%d/%m/%Y"))
    c2dia2 = lib_tempo.getTempoCidadeDia(variaveis['cidade2'], data2.strftime("%d/%m/%Y"))
    c2dia3 = lib_tempo.getTempoCidadeDia(variaveis['cidade2'], data3.strftime("%d/%m/%Y"))

    c2dia1_semana = automator.DIAS_SEMANA[data1.weekday()]
    c2dia1['dia_semana'] = c2dia1_semana.upper()
    c2dia2_semana = automator.DIAS_SEMANA[data2.weekday()]
    c2dia2['dia_semana'] = c2dia2_semana.upper()
    c2dia3_semana = automator.DIAS_SEMANA[data3.weekday()]
    c2dia3['dia_semana'] = c2dia3_semana.upper()

    cidade2 = aux[2] + '-' + aux[3]



    saida = {}
    saida['modelo'] = variaveis['modelo']
    saida['cidade1'] = cidade1.upper()
    saida['c1dia1'] = c1dia1
    saida['c1dia2'] = c1dia2
    saida['c1dia3'] = c1dia3

    saida['cidade2'] = cidade2.upper()
    saida['c2dia1'] = c2dia1
    saida['c2dia2'] = c2dia2
    saida['c2dia3'] = c2dia3

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": saida, "renders": renders}
    return saida
