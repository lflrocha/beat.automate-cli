#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json
import requests
import datetime
import time
import numpy

from slugify import slugify
from PIL import Image, ImageDraw, ImageFont
from blend_modes import overlay, multiply

ROOT = automator.getBase()
ARQUIVOS = ROOT + 'arquivos/abr-cards/'
TEMP = ROOT + 'temp/'

fonte_link_texto = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-600Medium.otf', 72)
fonte_link_texto2 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 54)
fonte_link_texto3 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 72)
fonte_link_texto4 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bold.otf', 56)
fonte_link_credito = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 24)
fonte_link_editoria = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bolditalic.otf', 28)


fonte_square_texto = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-600Medium.otf', 56)
fonte_square_texto2 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 54)
fonte_square_texto3 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 72)
fonte_square_texto4 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bold.otf', 56)
fonte_square_credito = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 14)
fonte_square_editoria = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bolditalic.otf', 24)

fonte_stories_texto = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-600Medium.otf', 72)
fonte_stories_texto2 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 54)
fonte_stories_texto3 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 72)
fonte_stories_texto4 = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bold.otf', 56)
fonte_stories_credito = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-400Regular.otf', 24)
fonte_stories_editoria = ImageFont.truetype(ARQUIVOS + 'fonts/TipoBrasilRounded-850Bolditalic.otf', 28)



fonte_branca = (255, 255, 255, 255)
fonte_verde = (215, 235, 47, 255)
fonte_verde_escuro = (12, 26, 61, 255)




################################################################################
# Link
################################################################################

def gera_modelo_link01(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_link.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)


    # GERA ARTE
    w = 1200
    h = 628
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (968/1192):
        novo_w = 968 * (f_h / 1192.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1192 * (f_w / 968.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((969,1192), Image.Resampling.LANCZOS)
    base.paste(foto, (111, 0), mask=foto)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_1.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 80
    textoY = 1400

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_link_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_link_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_link_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_link_editoria)
    creditoX = int((1080 - tamanho) / 2)
    creditoY = 1152

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 58), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 40, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_link_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo


def gera_modelo_link02(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_link.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1200
    h = 628
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (827/1177):
        novo_w = 827 * (f_h / 1177.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1177 * (f_w / 827.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((827,1177), Image.Resampling.LANCZOS)
    base.paste(foto, (253, 0), mask=foto)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_2.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1320

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_link_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_link_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_link_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo

def gera_modelo_link03(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_link.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1200
    h = 628
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')
    # 968 x 1192

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1730):
        novo_w = 1080 * (f_h / 1730.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1730 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1730), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_3.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1300

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_link_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_link_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_link_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo


def gera_modelo_link04(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_link.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1200
    h = 628
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1920):
        novo_w = 1080 * (f_h / 1920.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1920 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1920), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_4.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1375

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_link_texto, fill=fonte_branca)

    texto2X = 825
    texto2Y = 240

    # linha1X = texto2X
    # linha1Y = texto2Y
    # base_img.text((linha1X, linha1Y), texto2[0].strip(), font=fonte_link_texto2, fill=fonte_verde)
    #
    # linha2X = texto2X
    # linha2Y = linha1Y + 60
    # base_img.text((linha2X, linha2Y), texto2[1].strip(), font=fonte_link_texto2, fill=fonte_verde)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_link_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_link_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_link_editoria)
    creditoX = 100
    creditoY = 1290

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 58), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 40, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_link_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo


def gera_modelo_link05(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_link.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1200
    h = 628
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1920):
        novo_w = 1080 * (f_h / 1920.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1920 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1920), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Link-AgenciaBrasil_5.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1440

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_link_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_link_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_link_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_link_credito, fill=fonte_branca)

    base.save(export + nome_arquivo)
    return export + nome_arquivo









################################################################################
# Square
################################################################################

def gera_modelo_square01(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_square.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)


    w = 1080
    h = 1080
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (971/653):
        novo_w = 971 * (f_h / 653.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 653 * (f_w / 971.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((971,653), Image.Resampling.LANCZOS)
    base.paste(foto, (109, 0), mask=foto)


    bg = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_1.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 750

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 60
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 60
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 60
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_square_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_square_credito)
    creditoX = 1000 - tamanho
    creditoY = 1040
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_square_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_square_editoria)
    creditoX = int((1080 - tamanho) / 2)
    creditoY = 635

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq-square.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen-square.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 50), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir-square.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 35, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_square_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_square02(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_square.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1080
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (624/784):
        novo_w = 624 * (f_h / 784.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 784 * (f_w / 624.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((624,784), Image.Resampling.LANCZOS)
    base.paste(foto, (456, 0), mask=foto)

    bg = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_2.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 420

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 60
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 60
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 60
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_square_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_square_credito)
    creditoX = 1000 - tamanho
    creditoY = 1040
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_square_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_square03(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_square.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)


    w = 1080
    h = 1080
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')
    # 968 x 1192

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (923/1025):
        novo_w = 923 * (f_h / 1025.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1025 * (f_w / 923.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((923,1025), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_3.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 680

    logo = Image.open(ARQUIVOS + "bg/logo.png").convert('RGBA')
    base.paste(logo, (60, 60), mask=logo)


    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 60
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 60
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 60
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_square_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_square_credito)
    creditoX = 1000 - tamanho
    creditoY = 1040
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_square_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_square04(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_square.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)


    w = 1080
    h = 1080
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1080):
        novo_w = 1080 * (f_h / 1080.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1080 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1080), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_4.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)


    logo = Image.open(ARQUIVOS + "bg/logo.png").convert('RGBA')
    base.paste(logo, (60, 60), mask=logo)

    textoX = 60
    textoY = 680

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 60
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 60
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 60
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_square_texto, fill=fonte_branca)

    texto2X = 825
    texto2Y = 815

    # linha1X = texto2X
    # linha1Y = texto2Y
    # base_img.text((linha1X, linha1Y), texto2[0].strip(), font=fonte_texto2, fill=fonte_verde)
    #
    # linha2X = texto2X
    # linha2Y = linha1Y + 50
    # base_img.text((linha2X, linha2Y), texto2[1].strip(), font=fonte_texto2, fill=fonte_verde)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_square_credito)
    creditoX = 1000 - tamanho
    creditoY = 1040
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_square_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_square_editoria)
    creditoX = 100
    creditoY = 600

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq-square.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen-square.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 50), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir-square.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 35, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_square_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_square05(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_square.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)


    w = 1080
    h = 1080
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1080):
        novo_w = 1080 * (f_h / 1080.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1080 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1080), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Square-AgenciaBrasil_5.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    logo = Image.open(ARQUIVOS + "bg/logo.png").convert('RGBA')
    base.paste(logo, (60, 60), mask=logo)

    textoX = 60
    textoY = 790

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 60
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 60
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_square_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 60
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_square_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_square_credito)
    creditoX = 1000 - tamanho
    creditoY = 1040
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_square_credito, fill=fonte_branca)

    base.save(export + nome_arquivo)
    return export + nome_arquivo






def gera_modelo_stories01(dados, export):


    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_stories.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1920
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (968/1192):
        novo_w = 968 * (f_h / 1192.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1192 * (f_w / 968.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((969,1192), Image.Resampling.LANCZOS)
    base.paste(foto, (111, 0), mask=foto)


    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_1.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 80
    textoY = 1400

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_stories_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_stories_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_stories_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_stories_editoria)
    creditoX = int((1080 - tamanho) / 2)
    creditoY = 1152

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 58), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 40, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_stories_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo


def gera_modelo_stories02(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_stories.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1920
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (827/1177):
        novo_w = 827 * (f_h / 1177.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1177 * (f_w / 827.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((827,1177), Image.Resampling.LANCZOS)
    base.paste(foto, (253, 0), mask=foto)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_2.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1320

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_stories_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_stories_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_stories_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo


def gera_modelo_stories03(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_stories.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1920
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')
    # 968 x 1192

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1730):
        novo_w = 1080 * (f_h / 1730.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1730 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1730), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_3.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1300

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_stories_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_stories_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_stories_credito, fill=fonte_verde_escuro)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_stories04(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_stories.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1920
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1920):
        novo_w = 1080 * (f_h / 1920.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1920 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1920), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_4.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1375

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_stories_texto, fill=fonte_branca)

    texto2X = 825
    texto2Y = 240

    # linha1X = texto2X
    # linha1Y = texto2Y
    # base_img.text((linha1X, linha1Y), texto2[0].strip(), font=fonte_texto2, fill=fonte_verde)
    #
    # linha2X = texto2X
    # linha2Y = linha1Y + 60
    # base_img.text((linha2X, linha2Y), texto2[1].strip(), font=fonte_texto2, fill=fonte_verde)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_stories_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_stories_credito, fill=fonte_branca)

    tamanho = base_img.textlength(editoria.strip().upper(), font=fonte_stories_editoria)
    creditoX = 100
    creditoY = 1290

    tarja_esq = Image.open(ARQUIVOS + "bg/tarja-esq.png").convert('RGBA')
    tarja_cen = Image.open(ARQUIVOS + "bg/tarja-cen.png").convert('RGBA')
    tarja_cen = tarja_cen.resize((int(tamanho) + 40, 58), Image.Resampling.LANCZOS)
    tarja_dir = Image.open(ARQUIVOS + "bg/tarja-dir.png").convert('RGBA')
    base.paste(tarja_esq, (creditoX - 40, creditoY -10), mask=tarja_esq)
    base.paste(tarja_cen, (creditoX - 20, creditoY -10), mask=tarja_cen)
    base.paste(tarja_dir, (creditoX + int(tamanho) + 20, creditoY -10), mask=tarja_dir)

    base_img.text((creditoX, creditoY), editoria.strip().upper(), font=fonte_stories_editoria, fill=fonte_verde)

    base.save(export + nome_arquivo)
    return export + nome_arquivo



def gera_modelo_stories05(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_stories.png'
    variaveis = dados['variaveis']
    credito = variaveis['credito']
    foto = variaveis['arquivo']
    endereco = variaveis['endereco']
    editoria = variaveis['editoria']
    texto = [variaveis['linha1'], variaveis['linha2'], variaveis['linha3'], variaveis['linha4']]
    nome_foto = slugify(dados['novo_projeto'] + foto) + '.' + foto.rsplit('.', 1)[1]
    foto = nome_foto
    r = requests.get(endereco)
    open(TEMP + foto, 'wb').write(r.content)

    w = 1080
    h = 1920
    base = Image.new('RGBA', (w, h), (255,255,255,0))

    base_img = ImageDraw.Draw(base)
    foto = Image.open(TEMP + foto).convert('RGBA')

    f_w = foto.size[0]
    f_h = foto.size[1]
    if  (f_w / f_h) > (1080/1920):
        novo_w = 1080 * (f_h / 1920.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1920 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1920), Image.Resampling.LANCZOS)
    base.paste(foto, (0, 0), mask=foto)

    background_img = numpy.array(base)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.
    middle_img_raw = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_shadow.png")  # RGBA image
    middle_img = numpy.array(middle_img_raw)  # Inputs to blend_modes need to be numpy arrays.
    middle_img_float = middle_img.astype(float)  # Inputs to blend_modes need to be floats.
    opacity = .9  # The opacity of the foreground that is blended onto the background is 70 %.
    blended1_img_float = multiply(background_img_float, middle_img_float, opacity)
    blended_img = numpy.uint8(blended1_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    shape = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
    base.paste(shape, (0, 0), mask=shape)

    bg = Image.open(ARQUIVOS + "bg/Stories-AgenciaBrasil_5.png").convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    textoX = 60
    textoY = 1440

    linha1X = textoX
    linha1Y = textoY
    base_img.text((linha1X, linha1Y), texto[0].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha2X = textoX
    linha2Y = linha1Y + 80
    base_img.text((linha2X, linha2Y), texto[1].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha3X = textoX
    linha3Y = linha2Y + 80
    base_img.text((linha3X, linha3Y), texto[2].strip(), font=fonte_stories_texto, fill=fonte_branca)

    linha4X = textoX
    linha4Y = linha3Y + 80
    base_img.text((linha4X, linha4Y), texto[3].strip(), font=fonte_stories_texto, fill=fonte_branca)

    tamanho = base_img.textlength("Foto: " + credito.strip(), font=fonte_stories_credito)
    creditoX = 1000 - tamanho
    creditoY = 1760
    base_img.text((creditoX, creditoY), "Foto: " + credito.strip(), font=fonte_stories_credito, fill=fonte_branca)

    base.save(export + nome_arquivo)
    return export + nome_arquivo
