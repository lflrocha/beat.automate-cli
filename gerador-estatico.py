#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_conasems as lib_conasems

import datetime
import json
import os
import requests
import shutil
from slugify import slugify
import logging
import subprocess

ROOT = automator.getBase()

data = datetime.datetime.now()
diaSemana = data.weekday()
ano = data.strftime('%Y')
mes = data.strftime('%m')
dia = data.strftime('%d')
data_hora_str = data.strftime("%Y%m%d%H%M%S")

ARQUIVOS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
CUT = './Automate/'

with open("programacao.json", encoding="utf-8") as f:
    dados = json.load(f)


for num, dado in enumerate(dados):

    arq = "programacao_" + str(num)
    novo_projeto = arq

    print(dado)

    aux = dado['descricao'].split("|")

    if len(aux) > 1:
        texto_tipo = aux[0]
        evento = aux[1]
    else:
        texto_tipo = aux[0]
        evento = aux[0]

    SAIDA = dado
    SAIDA['texto_tipo'] = texto_tipo
    SAIDA['evento'] = evento

    if SAIDA['data'] == '12/07':
        SAIDA['dia'] = "Domingo"
    elif SAIDA['data'] == '13/07':
        SAIDA['dia'] = "Segunda"
    elif SAIDA['data'] == '14/07':
        SAIDA['dia'] = "Terça"
    elif SAIDA['data'] == '15/07':
        SAIDA['dia'] = "Quarta"
    elif SAIDA['data'] == '16/07':
        SAIDA['dia'] = "Quinta"


    ID = 'congresso_programacao'
    JSX = ROOT + 'scripts/congresso_programacao.jsx'
    EXPORT = ROOT + 'export/congresso_programacao/'
    # DESTINO = local + '/Conasems/Congresso/'

    arq_projeto = TEMP + arq + '.json'
    with open(arq_projeto, 'w') as f:
        json.dump(SAIDA, f, indent=4, sort_keys=True)

    # CRIA ARQUIVO AEP
    projetoAfter = TEMP + novo_projeto + '.aep'
    jsx = TEMP + novo_projeto + '.jsx'
    retorno = automator.copiaArquivo(JSX, jsx)
    retorno = automator.atualizaProjeto(jsx)

    # CRIA PASTA NO EXPORT
    export = EXPORT + ano + '/' + mes + '/' + dia + '/'
    if not os.path.isdir(export):
        os.makedirs(export)

    renders = [
        {
            "comp": "!01_programacao",
            "inicio": "1",
            "fim": "1199",
            "OM": "MP4",
            "arquivo": arq + ".mp4",
            # "converter": "MP4"
        }
    ]

    for render in renders:
        comp = render['comp']
        inicio  = render['inicio']
        fim = render['fim']
        om = render['OM']
        nome_arquivo = render['arquivo']
        arquivo = export + render['arquivo']
        retorno = automator.geraArte(projetoAfter, comp, inicio, fim, om, arquivo)
