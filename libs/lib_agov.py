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


def resize_and_fill_same_file(image_path, size=(1920, 1080), background_color=(255, 255, 255)):
    image = Image.open(image_path)
    ratio = min(size[0] / image.width, size[1] / image.height)
    new_dimensions = (int(image.width * ratio), int(image.height * ratio))
    resized_image = image.resize(new_dimensions, Image.Resampling.LANCZOS)
    new_image = Image.new("RGB", size, background_color)
    upper_left = ((size[0] - new_dimensions[0]) // 2, (size[1] - new_dimensions[1]) // 2)
    new_image.paste(resized_image, upper_left)
    new_image.save(image_path)



def resize_and_crop(image_path, size=(1920, 1080)):
    image = Image.open(image_path)

    # Calcula a nova dimensão para cobrir completamente o tamanho desejado
    img_ratio = image.width / image.height
    target_ratio = size[0] / size[1]
    if target_ratio > img_ratio:
        # Largura da imagem é o limitante
        new_height = int(size[0] / img_ratio)
        image = image.resize((size[0], new_height), Image.Resampling.LANCZOS)
    else:
        # Altura da imagem é o limitante
        new_width = int(size[1] * img_ratio)
        image = image.resize((new_width, size[1]), Image.Resampling.LANCZOS)

    # Calcula o ponto de corte
    left = (image.width - size[0]) / 2
    top = (image.height - size[1]) / 2
    right = (image.width + size[0]) / 2
    bottom = (image.height + size[1]) / 2

    # Corta a imagem
    image = image.crop((left, top, right, bottom))

    # Salva a imagem resultante sobrepondo a original
    image.save(image_path)


def getDestaqueAgenciaGov(link, id):
    req = requests.get(link)
    aux = req.text

    ret = {}
    soup = BeautifulSoup(aux, 'html.parser')
    ret['imagem'] = soup.find('div',  class_='foto-com-creditos').find('img')['src']
    ret['credito'] = ""
    ret['editoria'] = soup.find('div', class_='tema-noticia').get_text().strip().replace('"','\"')
    ret['titulo'] = soup.find('h1').get_text().strip().replace('"','\"')
    ret['descricao'] = soup.find('p', class_="resumo-noticia-conteudo").get_text().strip().replace('"','\"')

    arq_imagem = ret['imagem'].rsplit('/',1)[1]
    ext = arq_imagem.rsplit('.',1)[1]
    novo_nome_arq_imagem = 'imagem' + DATA_HORA + '-' + id + '.' + ext
    urllib.request.urlretrieve(ret['imagem'], TEMP + novo_nome_arq_imagem)

    resize_and_crop(TEMP + novo_nome_arq_imagem)


    dados = {
        "editoria": ret['editoria'].replace('"','\"'),
        "titulo": ret['titulo'].replace('"','\"'),
        "imagem": novo_nome_arq_imagem,
        "credito": ret['credito'].replace('"','\"'),
        "descricao": ret['descricao'].replace('"','\"'),
        "link": link
    }

    return dados
