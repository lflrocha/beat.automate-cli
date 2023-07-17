# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json
import requests
import datetime
import xml.etree.ElementTree as ET
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'

def geraMapaAlertas(codigo, xml):
    # header = { 'Accept': 'application/xml' }
    # r = requests.get(url, headers=header)
    dados_inmet = xml
    dados_inmet = dados_inmet.replace(' xmlns="urn:oasis:names:tc:emergency:cap:1.2"', '')
    tree = ET.ElementTree(ET.fromstring(dados_inmet))
    root = tree.getroot()
    for child in root.iter():
        if child.tag == "severity":
            severidade = child.text
        if child.tag == "polygon":
            poligono = child.text
        if child.tag == "event":
            evento = child.text
        if child.tag == "web":
            web = child.text
            codigo = web.rsplit('/', 1)
            codigo = codigo[1]
        if child.tag == "area":
            area = child[1].text
    pontos = area.split(" ")
    poligono = []
    for ponto in pontos:
        aux = ponto.split(',')
        if len(aux) == 2:
            poligono.append( ( float(aux[0]), float(aux[1]) ) )
    print(poligono)
    aux = root.findall('info/parameter')
    for item in aux:
        item2 = item.findall('valueName')
        if item2[0].text == "Municipios":
            item3 = item.findall('value')
            municipios = item3[0].text
    cor = "#C10000"
    if severidade == "Severe":
        cor = "#FF8500"
    elif severidade == "Moderate":
        cor = "#FFCF38"

    # poligonos = cidades_poligonos
    image = Image.new("RGBA", (2000, 2000))
    draw = ImageDraw.Draw(image)
    # poligonos = cidades_poligonos[cidade]

    points = []
    for pontos in poligono:
        x = (pontos[1] + 75) * 40
        y = (pontos[0] + 35) * 40

        points.append((x, y))
    draw.line(points, fill=cor, width=2)
    draw.polygon((points), fill=cor, outline=cor)
    transposed = image.transpose(Image.FLIP_TOP_BOTTOM)
    data_hora = datetime.datetime.now()
    data_hora = data_hora.strftime("%Y%m%d-%H%M%S")
    arquivo = TEMP + "%s_alerta_%s.png" % (data_hora, codigo)
    transposed.save(arquivo)
    return arquivo


def getDadosAlertas(url):
    id = url.rsplit('/', 1)
    id = id[1]
    url = "https://apiprevmet3.inmet.gov.br/avisos/rss/%s" % id
    r = requests.get(url)
    dados_inmet = r.text
    return (id, dados_inmet)


def getTempoAlertas(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    alertas = variaveis['alertas']
    arquivos = []
    for alerta in alertas:
        codigo, xml = getDadosAlertas(alerta['endereco'])
        arquivo = geraMapaAlertas(codigo, xml)
        arquivos.append(arquivo)

    variaveis['arquivos'] = arquivos

    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
