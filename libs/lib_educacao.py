# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def getEducacaoBussolaHoje(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida

def getEducacaoBussolaAssista(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    codigo1 = variaveis['codigo']
    codigo2 = variaveis['codigo2']

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "150",
            "OM": "MAM",
            "arquivo": arquivo_saida + '_' + codigo1 + ".mov",
            "converter": "MXF"
        },
        {
            "comp": "02_render",
            "inicio": "1",
            "fim": "150",
            "OM": "MAM",
            "arquivo": arquivo_saida + '_' + codigo2 + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida


def getEducacaoChamadaSimples(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    video = variaveis['video']

    caminho_video = "/Volumes/Automator_Envios/Educacao/"
    if not os.path.isdir(caminho_video):
        retorno = os.system('osascript '+ROOT+'scripts/mountEnvio.scpt')
    retorno = os.system('cp "' + caminho_video + video + '" "' + TEMP + '"')

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
