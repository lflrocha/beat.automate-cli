# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json

import libs.lib_abr as abr

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def getFocus(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "900",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida


def getLista(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "900",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida


def getDestaqueAgencia(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    link = variaveis['link']
    dados_noticia = abr.getDestaqueAgencia(link, identificador)
    variaveis['editoria'] = dados_noticia['editoria']
    variaveis['titulo'] = dados_noticia['titulo']
    variaveis['imagem'] = dados_noticia['imagem']
    variaveis['credito'] = dados_noticia['credito']
    variaveis['descricao'] = dados_noticia['descricao']

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
