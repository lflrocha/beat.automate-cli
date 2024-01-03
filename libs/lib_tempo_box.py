# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_tempo as lib_tempo
import urllib
import os
import json
import requests
import datetime

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'



def getTempoBox(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    data = variaveis['data']

    aux = lib_tempo.getDadosCidade(variaveis['cidade1'])
    cidade1 = lib_tempo.getTempoCidadeDia(variaveis['cidade1'], data)
    cidade1['nome'] = aux[2] + '-' + aux[3]
    cidade1['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade1'])['dados'][data]
    variaveis['cidade1'] = cidade1

    aux = lib_tempo.getDadosCidade(variaveis['cidade2'])
    cidade2 = lib_tempo.getTempoCidadeDia(variaveis['cidade2'], data)
    cidade2['nome'] = aux[2] + '-' + aux[3]
    cidade2['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade2'])['dados'][data]
    variaveis['cidade2'] = cidade2

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

    print(variaveis)
    saida = {"dados": variaveis, "renders": renders}
    return saida



def getTempoBox3Cidades(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    data = variaveis['data']

    aux = lib_tempo.getDadosCidade(variaveis['cidade1'])
    cidade1 = lib_tempo.getTempoCidadeDia(variaveis['cidade1'], data)
    cidade1['nome'] = aux[2] + '-' + aux[3]
    cidade1['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade1'])['dados'][data]
    variaveis['cidade1'] = cidade1

    aux = lib_tempo.getDadosCidade(variaveis['cidade2'])
    cidade2 = lib_tempo.getTempoCidadeDia(variaveis['cidade2'], data)
    cidade2['nome'] = aux[2] + '-' + aux[3]
    cidade2['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade2'])['dados'][data]
    variaveis['cidade2'] = cidade2

    aux = lib_tempo.getDadosCidade(variaveis['cidade3'])
    cidade3 = lib_tempo.getTempoCidadeDia(variaveis['cidade3'], data)
    cidade3['nome'] = aux[2] + '-' + aux[3]
    cidade3['chuva'] = lib_tempo.getInformacoesChuva(variaveis['cidade3'])['dados'][data]
    variaveis['cidade3'] = cidade3

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

    print(variaveis)
    saida = {"dados": variaveis, "renders": renders}
    return saida
