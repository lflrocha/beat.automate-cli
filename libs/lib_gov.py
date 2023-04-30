# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


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
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4-AUDIO"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
