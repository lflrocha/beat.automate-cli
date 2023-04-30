# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def getRedesTiktok(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    arq_imagem1 = variaveis['arq_background']
    end_imagem1 = variaveis['end_background']
    arquivo_video = variaveis['arquivo']

    download = [
        (end_imagem1, arq_imagem1)
    ]

    automator.baixaArquivos(download)
    automator.resizeImage1080X1920(TEMP + arq_imagem1)

    caminho_video = "/Volumes/Automator_Envios/Redes/"
    if not os.path.isdir(caminho_video):
        retorno = os.system('osascript '+ROOT+'scripts/mountEnvio.scpt')
    retorno = os.system('cp "' + caminho_video + arquivo_video + '" "' + TEMP + '"')

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + "_tiktok.mov",
            "converter": "MP4-AUDIO"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
