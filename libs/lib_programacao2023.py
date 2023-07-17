# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'


def divide_string(string):
    # Verifica se a string já é menor ou igual a 30 caracteres
    if len(string) <= 15:
        return [string]

    half_index = len(string) // 2
    space_index = string.rfind(' ', 0, half_index + 1)

    if space_index == -1:
        space_index = string.find(' ', half_index)

    if space_index == -1:
        space_index = half_index

    first_part = string[:space_index].strip()
    second_part = string[space_index:].strip()

    return [first_part, second_part]

def getBussolas(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    programa = variaveis['programa'].upper()

    aux = divide_string(programa)

    if len(aux) > 1:
        programa = aux[0] + '\n' + aux[1]
    else:
        programa = aux[0]

    variaveis['programa'] = programa
    codigo_ja = variaveis['codigo_ja']
    codigo_com = variaveis['codigo_com']

    renders = [
        {
            "comp": "!01_render_com",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + '_' + codigo_com + ".mov",
            "converter": "MP4"
        },
        {
            "comp": "!02_render_ja",
            "inicio": "1",
            "fim": "300",
            "OM": "MAM",
            "arquivo": arquivo_saida + '_' + codigo_ja + ".mov",
            "converter": "MP4"
        }

    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
