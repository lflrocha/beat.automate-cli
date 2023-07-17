# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_tempo as lib_tempo
import urllib
import os
import json
import requests
import datetime
import xml.etree.ElementTree as ET
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import colorsys


from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'
ARQUIVOS = ROOT + 'arquivos/'



conversao_cores = {
    (0, 91, 7): "#006A4C",
    (0, 102, 8): "#006A4C",
    (0, 122, 10): "#006A4C",
    (0, 142, 11): "#018E0B",
    (0, 163, 13): "#0E9D49",
    (0, 173, 14): "#0E9D49",
    (0, 193, 16): "#0E9D49",
    (0, 214, 17): "#0E9D49",
    (0, 224, 18): "#0E9D49",
    (0, 204, 17): "#0E9D49",
    (0, 255, 0): "#74C044",
    (30, 255, 49): "#74C044",
    (33, 48, 62): "#1366B2",
    (40, 255, 58): "#74C044",
    (50, 255, 67): "#74C044",
    (50, 255, 68): "#74C044",
    (61, 255, 77): "#74C044",
    (71, 255, 86): "#74C044",
    (81, 255, 96): "#74C044",
    (101, 255, 114): "#74C044",
    (107, 121, 137): "#7F878B",
    (112, 255, 124): "#74C044",
    (132, 255, 142): "#74C044",
    (142, 255, 152): "#74C044",
    (153, 255, 161): "#74C044",
    (232, 232, 98): "#E5AD17",
    (242, 242, 165): "#F2BD00",
    (245, 247, 120): "#E5AD17",
    (248, 191, 57): "#F2BD00",
    (248, 191, 57): "#F2BD00",
    (245, 245, 188): "#F2BD00",
    (248, 248, 210): "#FFD200",
    (251, 251, 232): "#FFD200",
    (255, 255, 255): "#91E5FF",
    (0, 112, 9): "#006A4C",
}

def converteCor(cor):
    cor = cor.split('(')
    cor = cor[1].split(',')
    h = int(cor[0]) / 360
    s = int(cor[1][:-1]) / 100
    l = int(cor[2][:-1]) / 100
    aux = colorsys.hls_to_rgb(h, l, s)
    r = int(aux[0] * 255)
    g = int(aux[1] * 255)
    b = int(aux[2] * 255)
    aux = (r, g, b)
    return aux

def getCidades():
    with open(ARQUIVOS + "previsao-tempo/CidadesTempo.js") as f:
        dados = f.read()
    dados = eval(dados)
    cidades_poligonos = {}
    for dado in dados:
        codigo = dado[0]
        poligonos = dado[1]
        cidades_poligonos[codigo] = poligonos
    return cidades_poligonos


def geraMapaTempo(data, novo_projeto, turno):
    data_hora = datetime.datetime.now()
    data_hora = data_hora.strftime("%Y%m%d-%H%M%S")


    arquivos_gerados = []
    url = 'https://apiprevmet3.inmet.gov.br/Previsao_Portal'
    headers = {'Content-type': 'application/json'}

    hoje = datetime.datetime.now()
    amanha = hoje + datetime.timedelta(days = 1)
    hoje = hoje.strftime("%Y-%m-%d")
    amanha = amanha.strftime("%Y-%m-%d")

    tipo = "diaria"
    if data == hoje or data == amanha:
        tipo = "turno"
        if turno not in ['manha', 'tarde', 'noite']:
            turno = "tarde"
    else:
        tipo = "diaria"
        turno = "tarde"

    print(url)
    r = requests.post(url, json={"data": data, "tipo": tipo, "turno": turno}, headers=headers)
    dados_inmet = r.json()
    with open(TEMP + "inmet.json", "w") as f:
        f.write(json.dumps(dados_inmet, indent=4) )
    cores = []
    grupos_por_cor = {}
    for cidade in dados_inmet:
        codigo = str(cidade['geocode'])
        cor = converteCor(cidade['cor'])

        if cor in conversao_cores.keys():
            cor = conversao_cores[cor]
        else:
            print(cor)
        cores.append(cor)
        if cor in grupos_por_cor.keys():
            grupos_por_cor[cor].append(codigo)
        else:
            grupos_por_cor[cor] = [codigo]

    cores = set(cores)
    cidades_poligonos = getCidades()

    image2 = Image.new("RGBA", (2000, 2000))
    draw2 = ImageDraw.Draw(image2)

    for i, cor in enumerate(grupos_por_cor):
        image = Image.new("RGBA", (2000, 2000))
        draw = ImageDraw.Draw(image)

        cidades = grupos_por_cor[cor]
        for cidade in cidades:
            poligonos = cidades_poligonos[cidade]
            for poligono in poligonos:
                points = []
                for pontos in poligono:
                    x = (pontos[0] + 75) * 40
                    y = (pontos[1] + 35) * 40
                    points.append((x, y))

                draw.line(points, fill=cor, width=2)
                draw.polygon((points), fill=cor, outline=cor)
                draw2.line(points, fill=cor, width=2)
                draw2.polygon((points), fill=cor, outline=cor)

        transposed = image.transpose(Image.FLIP_TOP_BOTTOM)
        transposed.save(TEMP + "%s_%s_%s.png" % (data_hora, novo_projeto, str(i)))
        arquivos_gerados.append("%s_%s_%s.png" % (data_hora, novo_projeto, str(i)))
    transposed2 = image2.transpose(Image.FLIP_TOP_BOTTOM)
    transposed2.save(TEMP + "%s_%s.png" % (data_hora, novo_projeto))
    return arquivos_gerados



def getTempoCidades(cidades, data, tipo):
    dados = {}
    for i, cidade in enumerate(cidades):
        aux = lib_tempo.getTempoCidadeDia(cidade, data)

        if tipo == "tempo":
            icone = aux['icone']
            uf = lib_tempo.codigo_estados[cidade[:2]]
            dados[uf] = icone
        elif tipo == "minima":
            minima = aux['minima']
            uf = lib_tempo.codigo_estados[cidade[:2]]
            dados[uf] = str(minima) + "º"
        elif tipo == "maxima":
            maxima = aux['maxima']
            uf = lib_tempo.codigo_estados[cidade[:2]]
            dados[uf] = str(maxima) + "º"

    return dados




def getTempoMapa(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    titulo = variaveis['titulo']
    data = variaveis['data']
    turno = variaveis['turno']
    cidades = variaveis['cidades']
    tipo_mapa = variaveis['tipo_mapa']
    regiao = variaveis['regiao']


    arquivos = geraMapaTempo(data, novo_projeto, turno)
    dados_tempo = getTempoCidades(cidades, data, tipo_mapa)

    variaveis['dados_tempo'] = dados_tempo
    print(dados_tempo)


    if tipo_mapa == "tempo":
        if regiao == "brasil":
            comp = "!02_render_br_tempo"
        elif regiao == "norte":
            comp = "!06_render_n_tempo"
        elif regiao == "nordeste":
            comp = "!08_render_ne_tempo"
        elif regiao == "centro-oeste":
            comp = "!04_render_co_tempo"
        elif regiao == "sudeste":
            comp = "!12_render_se_tempo"
        elif regiao == "sul":
            comp = "!10_render_s_tempo"

    else:
        if regiao == "brasil":
            comp = "!01_render_br_temperatura"
        elif regiao == "norte":
            comp = "!05_render_n_temperatura"
        elif regiao == "nordeste":
            comp = "!07_render_ne_temperatura"
        elif regiao == "centro-oeste":
            comp = "!03_render_co_temperatura"
        elif regiao == "sudeste":
            comp = "!11_render_se_temperatura"
        elif regiao == "sul":
            comp = "!09_render_s_temperatura"


    renders = [
        {
            "comp": comp,
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
