# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json
from PIL import Image

import libs.lib_agov as agov
from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def resize_image_twitter(image_path):
    max_width = 1550
    max_height = 690

    with Image.open(image_path) as img:
        original_width, original_height = img.size

        ratio = min(max_width / original_width, max_height / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        if (new_width, new_height) != (original_width, original_height):
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(image_path)



def getGovInforma(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    arq_imagem1 = variaveis['foto_arquivo']
    end_imagem1 = variaveis['foto_endereco']

    download = [
        (end_imagem1, arq_imagem1)
    ]

    automator.baixaArquivos(download)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "450",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida




def getGovTwitter(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    arq_imagem1 = variaveis['foto_arquivo']
    end_imagem1 = variaveis['foto_endereco']

    download = [
        (end_imagem1, arq_imagem1)
    ]

    automator.baixaArquivos(download)
    resize_image_twitter(TEMP + arq_imagem1)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovInstagram(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    arq_imagem1 = variaveis['foto_arquivo']
    end_imagem1 = variaveis['foto_endereco']

    download = [
        (end_imagem1, arq_imagem1)
    ]

    automator.baixaArquivos(download)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MXF"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida




def getGovDestaqueAgGov(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    link = variaveis['link']
    dados_noticia = agov.getDestaqueAgenciaGov(link, identificador)
    variaveis['editoria'] = dados_noticia['editoria']
    variaveis['titulo'] = dados_noticia['titulo']
    variaveis['imagem'] = dados_noticia['imagem']
    variaveis['credito'] = dados_noticia['credito']
    variaveis['descricao'] = dados_noticia['descricao']

    renders = [
        {
            "comp": "01_render_agov",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovDestaqueABr(dados):
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
            "comp": "02_render_abr",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida





def getGovOnAirDaquiAPouco(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "150",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida


def getGovOnAirASeguir(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "150",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida


def getGovOnAirBussola1(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "150",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovOnAirBussola2(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovOnAirBussola3(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "450",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovOnAirHorarioAlternativo(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "450",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getGovOnAirCitacao(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']

    codigo = variaveis['codigo']
    arquivo_saida = slugify(novo_projeto + '-' + codigo)

    arq_imagem1 = variaveis['arquivo']
    end_imagem1 = variaveis['endereco']

    download = [
        (end_imagem1, arq_imagem1)
    ]

    automator.baixaArquivos(download)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "450",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
