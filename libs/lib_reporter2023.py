# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json
import requests

import libs.lib_abr as abr

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def baixaFotoAlbum(arquivo, endereco):
    r = requests.get(endereco)
    open(TEMP + arquivo, 'wb').write(r.content)
    return arquivo


def getAlbum(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']
    modelo = variaveis['modelo']

    fotos = []

    foto01_arquivo = variaveis['foto01_arquivo']
    foto01_endereco = variaveis['foto01_endereco']
    foto01_legenda = variaveis['foto01_legenda']
    if foto01_arquivo:
        arq01 = baixaFotoAlbum(foto01_arquivo, foto01_endereco)
        fotos.append([arq01, foto01_legenda])

    foto02_arquivo = variaveis['foto02_arquivo']
    foto02_endereco = variaveis['foto02_endereco']
    foto02_legenda = variaveis['foto02_legenda']
    if foto02_arquivo:
        arq02 = baixaFotoAlbum(foto02_arquivo, foto02_endereco)
        fotos.append([arq02, foto02_legenda])

    foto03_arquivo = variaveis['foto03_arquivo']
    foto03_endereco = variaveis['foto03_endereco']
    foto03_legenda = variaveis['foto03_legenda']
    if foto03_arquivo:
        arq03 = baixaFotoAlbum(foto03_arquivo, foto03_endereco)
        fotos.append([arq03, foto03_legenda])

    foto04_arquivo = variaveis['foto04_arquivo']
    foto04_endereco = variaveis['foto04_endereco']
    foto04_legenda = variaveis['foto04_legenda']
    if foto04_arquivo:
        arq04 = baixaFotoAlbum(foto04_arquivo, foto04_endereco)
        fotos.append([arq04, foto04_legenda])

    foto05_arquivo = variaveis['foto05_arquivo']
    foto05_endereco = variaveis['foto05_endereco']
    foto05_legenda = variaveis['foto05_legenda']
    if foto05_arquivo:
        arq05 = baixaFotoAlbum(foto05_arquivo, foto05_endereco)
        fotos.append([arq05, foto05_legenda])

    foto06_arquivo = variaveis['foto06_arquivo']
    foto06_endereco = variaveis['foto06_endereco']
    foto06_legenda = variaveis['foto06_legenda']
    if foto06_arquivo:
        arq06 = baixaFotoAlbum(foto06_arquivo, foto06_endereco)
        fotos.append([arq06, foto06_legenda])

    foto07_arquivo = variaveis['foto07_arquivo']
    foto07_endereco = variaveis['foto07_endereco']
    foto07_legenda = variaveis['foto07_legenda']
    if foto07_arquivo:
        arq07 = baixaFotoAlbum(foto07_arquivo, foto07_endereco)
        fotos.append([arq07, foto07_legenda])

    foto08_arquivo = variaveis['foto08_arquivo']
    foto08_endereco = variaveis['foto08_endereco']
    foto08_legenda = variaveis['foto08_legenda']
    if foto08_arquivo:
        arq08 = baixaFotoAlbum(foto08_arquivo, foto08_endereco)
        fotos.append([arq08, foto08_legenda])

    foto09_arquivo = variaveis['foto09_arquivo']
    foto09_endereco = variaveis['foto09_endereco']
    foto09_legenda = variaveis['foto09_legenda']
    if foto09_arquivo:
        arq09 = baixaFotoAlbum(foto09_arquivo, foto09_endereco)
        fotos.append([arq09, foto09_legenda])

    foto10_arquivo = variaveis['foto10_arquivo']
    foto10_endereco = variaveis['foto10_endereco']
    foto10_legenda = variaveis['foto10_legenda']
    if foto10_arquivo:
        arq10 = baixaFotoAlbum(foto10_arquivo, foto10_endereco)
        fotos.append([arq10, foto10_legenda])


    variaveis = {}
    variaveis['fotos'] = fotos
    variaveis['modelo'] = modelo

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



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
            "fim": "900",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
