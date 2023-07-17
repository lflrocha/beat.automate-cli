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


def getTempo5Dias(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    data = variaveis['data']
    data1 = datetime.datetime.strptime(data, '%d/%m/%Y')
    data2 = data1 + datetime.timedelta(days=1)
    data3 = data1 + datetime.timedelta(days=2)
    data4 = data1 + datetime.timedelta(days=3)
    data5 = data1 + datetime.timedelta(days=4)

    aux = lib_tempo.getDadosCidade(variaveis['cidade'])
    dia1 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data1.strftime("%d/%m/%Y"))
    dia1['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade'])['dados'][data1.strftime("%d/%m/%Y")]

    dia2 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data2.strftime("%d/%m/%Y"))
    dia2['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade'])['dados'][data2.strftime("%d/%m/%Y")]

    dia3 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data3.strftime("%d/%m/%Y"))
    dia3['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade'])['dados'][data3.strftime("%d/%m/%Y")]

    dia4 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data4.strftime("%d/%m/%Y"))
    dia4['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade'])['dados'][data4.strftime("%d/%m/%Y")]

    dia5 = lib_tempo.getTempoCidadeDia(variaveis['cidade'], data5.strftime("%d/%m/%Y"))
    dia5['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade'])['dados'][data5.strftime("%d/%m/%Y")]

    dia1_semana = automator.DIAS_SEMANA[data1.weekday()]
    dia1['dia_semana'] = dia1_semana.upper()
    dia2_semana = automator.DIAS_SEMANA[data2.weekday()]
    dia2['dia_semana'] = dia2_semana.upper()
    dia3_semana = automator.DIAS_SEMANA[data3.weekday()]
    dia3['dia_semana'] = dia3_semana.upper()
    dia4_semana = automator.DIAS_SEMANA[data4.weekday()]
    dia4['dia_semana'] = dia4_semana.upper()
    dia5_semana = automator.DIAS_SEMANA[data5.weekday()]
    dia5['dia_semana'] = dia5_semana.upper()

    cidade = aux[2] + '-' + aux[3]

    saida = {}
    saida['modelo'] = variaveis['modelo']
    saida['cidade'] = cidade.upper().split('-')[0]
    saida['dia1'] = dia1
    saida['dia2'] = dia2
    saida['dia3'] = dia3
    saida['dia4'] = dia4
    saida['dia5'] = dia5

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
