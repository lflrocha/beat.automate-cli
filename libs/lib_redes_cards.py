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
ARQUIVOS = ROOT + 'arquivos/cards/'
TEMP = ROOT + 'temp/'

boletim_data = ImageFont.truetype(ARQUIVOS + 'fonts/Lato-Regular.ttf', 72)
boletim_texto = ImageFont.truetype(ARQUIVOS + 'fonts/Lato-Regular.ttf', 55)

boletim_fonte_branca = (255, 255, 255, 255)
boletim_fonte_verde = (8, 143, 49, 255)


nota_titulo = ImageFont.truetype(ARQUIVOS + 'fonts/Lato-Black.ttf', 80)
nota_texto = ImageFont.truetype(ARQUIVOS + 'fonts/Lato-Regular.ttf', 50)
nota_link = ImageFont.truetype(ARQUIVOS + 'fonts/Lato-Black.ttf', 65)

nota_fonte_branca = (255, 255, 255, 255)
nota_fonte_verde = (26, 101, 60, 255)

def quebrar_string(string, tamanho_maximo):
    palavras = string.split()
    resultado = []
    atual = ""

    for palavra in palavras:
        if len(atual) + len(palavra) + 1 <= tamanho_maximo:
            if atual:
                atual += " " + palavra
            else:
                atual = palavra
        else:
            resultado.append(atual)
            atual = palavra

    if atual:
        resultado.append(atual)

    return resultado



def gera_modelo_boletim(dados, export):

    # BUSCA DADOS
    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_boletim_'
    variaveis = dados['variaveis']

    data_inicio = variaveis['datainicio']
    data_fim = variaveis['datafim']


    w = 1080
    h = 1080

    base = Image.new('RGBA', (w, h), (255,255,255,0))
    base_img = ImageDraw.Draw(base)
    bg = Image.open(ARQUIVOS + 'bg/boletim01.png').convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)

    data = data_inicio + ' à ' + data_fim
    tamanho = base_img.textlength(data, font=boletim_data)
    aux = (w - tamanho) / 2
    base_img.text((aux, 600), data, font=boletim_data, fill=boletim_fonte_branca)
    base.save(export + nome_arquivo + '1.png')


    foto1 = variaveis['filename1']
    endereco1 = variaveis['endereco1']
    legenda1 = variaveis['legenda1']

    if foto1:

        base = Image.new('RGBA', (w, h), (255,255,255,0))
        base_img = ImageDraw.Draw(base)

        nome_foto1 = slugify(dados['novo_projeto'] + foto1) + '.' + foto1.rsplit('.', 1)[1]
        r = requests.get(endereco1)
        open(TEMP + nome_foto1, 'wb').write(r.content)

        foto = Image.open(TEMP + nome_foto1).convert('RGBA')

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


        textos = quebrar_string(legenda1, 35)
        for i, texto in enumerate(textos):
            delta_y = i * 70 + 720
            largura = base_img.textlength(texto, font=boletim_texto)
            base_img.rounded_rectangle([100, delta_y + 5, 100 + 30 + largura, delta_y + 65], fill="white", radius=10)
            base_img.text((115, delta_y), texto, font=boletim_texto, fill=boletim_fonte_verde)
        base_img.rounded_rectangle([50, 720, 70, 720 + len(textos) * 70], fill=(235, 171, 48), radius=10)

        base.save(export + nome_arquivo + '2.png')



    foto2 = variaveis['filename2']
    endereco2 = variaveis['endereco2']
    legenda2 = variaveis['legenda2']

    if foto2:

        base = Image.new('RGBA', (w, h), (255,255,255,0))
        base_img = ImageDraw.Draw(base)

        nome_foto2 = slugify(dados['novo_projeto'] + foto2) + '.' + foto2.rsplit('.', 1)[1]
        r = requests.get(endereco2)
        open(TEMP + nome_foto2, 'wb').write(r.content)

        foto = Image.open(TEMP + nome_foto2).convert('RGBA')

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


        textos = quebrar_string(legenda2, 35)
        for i, texto in enumerate(textos):
            delta_y = i * 70 + 720
            largura = base_img.textlength(texto, font=boletim_texto)
            base_img.rounded_rectangle([100, delta_y + 5, 100 + 30 + largura, delta_y + 65], fill="white", radius=10)
            base_img.text((115, delta_y), texto, font=boletim_texto, fill=boletim_fonte_verde)
        base_img.rounded_rectangle([50, 720, 70, 720 + len(textos) * 70], fill=(235, 171, 48), radius=10)

        base.save(export + nome_arquivo + '3.png')




    foto3 = variaveis['filename3']
    endereco3 = variaveis['endereco3']
    legenda3 = variaveis['legenda3']

    if foto3:

        base = Image.new('RGBA', (w, h), (255,255,255,0))
        base_img = ImageDraw.Draw(base)

        nome_foto3 = slugify(dados['novo_projeto'] + foto3) + '.' + foto3.rsplit('.', 1)[1]
        r = requests.get(endereco3)
        open(TEMP + nome_foto3, 'wb').write(r.content)

        foto = Image.open(TEMP + nome_foto3).convert('RGBA')

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


        textos = quebrar_string(legenda3, 35)
        for i, texto in enumerate(textos):
            delta_y = i * 70 + 720
            largura = base_img.textlength(texto, font=boletim_texto)
            base_img.rounded_rectangle([100, delta_y + 5, 100 + 30 + largura, delta_y + 65], fill="white", radius=10)
            base_img.text((115, delta_y), texto, font=boletim_texto, fill=boletim_fonte_verde)
        base_img.rounded_rectangle([50, 720, 70, 720 + len(textos) * 70], fill=(235, 171, 48), radius=10)

        base.save(export + nome_arquivo + '4.png')




    foto4 = variaveis['filename4']
    endereco4 = variaveis['endereco4']
    legenda4 = variaveis['legenda4']

    if foto4:

        base = Image.new('RGBA', (w, h), (255,255,255,0))
        base_img = ImageDraw.Draw(base)

        nome_foto4 = slugify(dados['novo_projeto'] + foto4) + '.' + foto4.rsplit('.', 1)[1]
        r = requests.get(endereco4)
        open(TEMP + nome_foto4, 'wb').write(r.content)

        foto = Image.open(TEMP + nome_foto4).convert('RGBA')

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

        textos = quebrar_string(legenda4, 35)
        for i, texto in enumerate(textos):
            delta_y = i * 70 + 720
            largura = base_img.textlength(texto, font=boletim_texto)
            base_img.rounded_rectangle([100, delta_y + 5, 100 + 30 + largura, delta_y + 65], fill="white", radius=10)
            base_img.text((115, delta_y), texto, font=boletim_texto, fill=boletim_fonte_verde)
        base_img.rounded_rectangle([50, 720, 70, 720 + len(textos) * 70], fill=(235, 171, 48), radius=10)

        base.save(export + nome_arquivo + '5.png')




    foto5 = variaveis['filename5']
    endereco5 = variaveis['endereco5']
    legenda5 = variaveis['legenda5']

    if foto5:

        base = Image.new('RGBA', (w, h), (255,255,255,0))
        base_img = ImageDraw.Draw(base)

        nome_foto5 = slugify(dados['novo_projeto'] + foto5) + '.' + foto5.rsplit('.', 1)[1]
        r = requests.get(endereco5)
        open(TEMP + nome_foto5, 'wb').write(r.content)

        foto = Image.open(TEMP + nome_foto5).convert('RGBA')

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


        textos = quebrar_string(legenda5, 35)
        for i, texto in enumerate(textos):
            delta_y = i * 70 + 720
            largura = base_img.textlength(texto, font=boletim_texto)
            base_img.rounded_rectangle([100, delta_y + 5, 100 + 30 + largura, delta_y + 65], fill="white", radius=10)
            base_img.text((115, delta_y), texto, font=boletim_texto, fill=boletim_fonte_verde)
        base_img.rounded_rectangle([50, 720, 70, 720 + len(textos) * 70], fill=(235, 171, 48), radius=10)


        base.save(export + nome_arquivo + '6.png')




def gera_modelo_nota(dados, export):

    nome_arquivo = slugify(dados['novo_projeto'] + '_' + dados['identificador']) + '_nota_'
    variaveis = dados['variaveis']

    titulo = variaveis['titulo']
    link = variaveis['link']
    mensagem = variaveis['texto']
    descricao = variaveis['descricao']

    w = 1080
    h = 1080

    base = Image.new('RGBA', (w, h), (255,255,255,0))
    base_img = ImageDraw.Draw(base)
    bg = Image.open(ARQUIVOS + 'bg/bg_nota.png').convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)
    base_img.rounded_rectangle([20, 150, 820, 350], fill=(255, 255, 255), radius=20)
    textos = quebrar_string(titulo, 16)
    for i, texto in enumerate(textos):
        y = 160 + i * 80
        w_texto = base_img.textlength(texto, font=nota_titulo)
        x = 800 - w_texto
        base_img.text((x, y), texto, font=nota_titulo, fill=nota_fonte_verde)


    textos = quebrar_string(descricao, 38)
    for i, texto in enumerate(textos):
        y = 450 + i * 60
        w_texto = base_img.textlength(texto, font=nota_texto)
        x = (1080 - w_texto) / 2
        base_img.text((x, y), texto, font=nota_texto, fill=nota_fonte_branca)

    base.save(export + nome_arquivo + '1.png')




    base = Image.new('RGBA', (w, h), (255,255,255,0))
    base_img = ImageDraw.Draw(base)
    bg = Image.open(ARQUIVOS + 'bg/bg_nota.png').convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)


    textos = quebrar_string(mensagem, 40)
    y_original = (1080 - (len(textos) * 60)) / 2

    y1 = y_original - 20
    y2 = y_original + len(textos) * 60 + 20
    base_img.rounded_rectangle([40, y1, 1040, y2], outline=(255,255,255), width=1, radius=20)

    for i, texto in enumerate(textos):
        y = y_original + i * 60
        w_texto = base_img.textlength(texto, font=nota_texto)
        x = (1080 - w_texto) / 2
        base_img.text((x, y), texto, font=nota_texto, fill=nota_fonte_branca)

    base.save(export + nome_arquivo + '2.png')



    base = Image.new('RGBA', (w, h), (255,255,255,0))
    base_img = ImageDraw.Draw(base)
    bg = Image.open(ARQUIVOS + 'bg/bg_nota.png').convert('RGBA')
    base.paste(bg, (0, 0), mask=bg)


    w_texto = base_img.textlength(link, font=nota_link)
    x = (1080 - w_texto) / 2
    base_img.text((x, 500), link, font=nota_link, fill=nota_fonte_branca)

    x1 = x - 20
    x2 = x + w_texto + 20
    base_img.rounded_rectangle([x1, 500, x2, 590], outline=(255,255,255), width=1, radius=20)


    base.save(export + nome_arquivo + '3.png')
