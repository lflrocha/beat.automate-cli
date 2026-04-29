# -*- coding: UTF-8 -*-

import libs.automator as automator

import datetime
import json
import requests
import time
import urllib
from slugify import slugify
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

from bs4 import BeautifulSoup
import re


ROOT = automator.getBase()
ARQS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
DATA_HORA = automator.getDataHora()


def getCongressoProgramacao(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    renders = [
        {
            "comp": "!01_programacao",
            "inicio": "1",
            "fim": "1199",
            "OM": "MP4",
            "arquivo": arquivo_saida + ".mp4",
            # "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
