# -*- coding: UTF-8 -*-

import libs.automator as automator
import requests
import os
import json
from PIL import Image

import xml.etree.ElementTree as ET
from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'




def getCotacaoDolar(data):
    # 2024-05-22
    url = "https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/220/" + data
    req = requests.get(url)
    aux = req.text
    root = ET.fromstring(aux)
    data_bc = root.find('data').text
    data_bc = data_bc.split("T")[0]
    cotacoes = root.find('cotacoes')
    tipo_cotacao = cotacoes.find('tipoCotacao').text
    compra = cotacoes.find('taxaCompra').text
    venda = cotacoes.find('taxaVenda').text
    compra = compra.replace(".", ",")[:6]
    venda = venda.replace(".", ",")[:6]

    if tipo_cotacao == "F" and data_bc == data:
        return [compra, venda]
    else:
        return ""


def getCotacaoEuro(data):
    # 2024-05-22
    url = "https://www3.bcb.gov.br/bc_moeda/rest/cotacao/fechamento/ultima/1/978/" + data
    req = requests.get(url)
    aux = req.text
    root = ET.fromstring(aux)
    data_bc = root.find('data').text
    data_bc = data_bc.split("T")[0]
    cotacoes = root.find('cotacoes')
    tipo_cotacao = cotacoes.find('tipoCotacao').text
    compra = cotacoes.find('taxaCompra').text
    venda = cotacoes.find('taxaVenda').text
    compra = compra.replace(".", ",")[:6]
    venda = venda.replace(".", ",")[:6]

    if tipo_cotacao == "F" and data_bc == data:
        return [compra, venda]
    else:
        return ""



def getGovOnAirCambio(data, novo_projeto):

    identificador = novo_projeto
    arquivo_saida = slugify(novo_projeto)

    var_data = data.strftime("%Y-%m-%d")
    str_data = data.strftime("%d/%m")
    euro = getCotacaoEuro(var_data)
    dolar = getCotacaoDolar(var_data)


    variaveis = {
        "data": "PTAX - " + str_data,
        "euro_compra": euro[0],
        "euro_venda": euro[1],
        "dolar_compra": dolar[0],
        "dolar_venda": dolar[1]
    }


    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "450",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4-AUDIO"
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
