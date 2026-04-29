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


def getInfoSite(link, id):

    req = requests.get(link)
    aux = req.text

    ret = {}
    soup = BeautifulSoup(aux, 'html.parser')

    section_bg_cover = soup.find('section', class_='!bg-cover')
    style_attr = section_bg_cover['style'] if section_bg_cover else ''
    url_match = re.search(r'url\((.*?)\)', style_attr)
    background_url = url_match.group(1) if url_match else ''


    ret['imagem'] = background_url
    ret['credito'] = ""
    ret['editoria'] = ""
    ret['titulo'] = soup.find('h1').get_text().strip().replace('"','\"')
    ret['descricao'] = soup.find('h3').get_text().strip().replace('"','\"')

    arq_imagem = ret['imagem'].rsplit('/',1)[1]
    ext = arq_imagem.rsplit('.',1)[1]
    novo_nome_arq_imagem = id + '.' + ext
    urllib.request.urlretrieve(ret['imagem'], TEMP + novo_nome_arq_imagem)
    resize_and_crop(TEMP + novo_nome_arq_imagem)


    dados = {
        "editoria": "",
        "titulo": ret['titulo'].replace('"','\"'),
        "imagem": novo_nome_arq_imagem,
        "credito": "",
        "descricao": ret['descricao'].replace('"','\"'),
        "link": link
    }

    return dados



def getDestaqueConasems(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    link = variaveis['link']
    dados_noticia = getInfoSite(link, identificador)
    variaveis['editoria'] = dados_noticia['editoria']
    variaveis['titulo'] = dados_noticia['titulo']
    variaveis['imagem'] = dados_noticia['imagem']
    variaveis['credito'] = dados_noticia['credito']
    variaveis['descricao'] = dados_noticia['descricao']




    renders = [
        {
            "comp": "01_render_conasems",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



def getProgramacaoConasems(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    arq1 = variaveis['filename1']
    link1 = variaveis['endereco1']
    arq2 = variaveis['filename2']
    link2 = variaveis['endereco2']
    arq3 = variaveis['filename3']
    link3 = variaveis['endereco3']




    ext = arq1.rsplit('.',1)[1]
    novo_nome_arq_imagem1 = arquivo_saida + '_img1.' + ext
    urllib.request.urlretrieve(link1, TEMP + novo_nome_arq_imagem1)

    ext = arq2.rsplit('.',1)[1]
    novo_nome_arq_imagem2 = arquivo_saida + '_img2.' + ext
    urllib.request.urlretrieve(link2, TEMP + novo_nome_arq_imagem2)

    ext = arq3.rsplit('.',1)[1]
    novo_nome_arq_imagem3 = arquivo_saida + '_img3.' + ext
    urllib.request.urlretrieve(link3, TEMP + novo_nome_arq_imagem3)

    variaveis['img1'] = novo_nome_arq_imagem1
    variaveis['img2'] = novo_nome_arq_imagem2
    variaveis['img3'] = novo_nome_arq_imagem3

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "900",
            "OM": "MOV",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida



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
