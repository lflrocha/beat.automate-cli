# -*- coding: UTF-8 -*-

import libs.automator as automator

import datetime
import json
import requests
import time
import urllib

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

from bs4 import BeautifulSoup


ROOT = automator.getBase()
ARQS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
DATA_HORA = automator.getDataHora()


def getDestaqueAgencia(link, id):
    categoria = link.split('/')[3]
    req = requests.get(link)
    aux = req.text

    ret = {}
    soup = BeautifulSoup(aux, 'html.parser')
    ret['imagem'] = soup.find('meta', property="og:image")['content']
    ret['credito'] = soup.find('figcaption').get_text().strip().replace('"','\"')
    ret['editoria'] = soup.find('span', 'badge badge-pill badge-warning').get_text().strip().replace('"','\"')
    ret['titulo'] = soup.find('meta', property="og:title")['content'].replace('"','\"')
    ret['descricao'] = soup.find('meta', property="og:description")['content'].replace('"','\"')

    arq_imagem = ret['imagem'].rsplit('?',1)
    arq_imagem = arq_imagem[0].rsplit('/',1)[1]
    ext = arq_imagem.rsplit('.',1)[1]
    novo_nome_arq_imagem = 'imagem' + DATA_HORA + '-' + id + '.' + ext
    urllib.request.urlretrieve(ret['imagem'], TEMP + novo_nome_arq_imagem)

    dados = {
        "editoria": ret['editoria'].replace('"','\"'),
        "titulo": ret['titulo'].replace('"','\"'),
        "imagem": novo_nome_arq_imagem,
        "credito": ret['credito'].replace('"','\"'),
        "descricao": ret['descricao'].replace('"','\"'),
        "link": link
    }

    return dados
