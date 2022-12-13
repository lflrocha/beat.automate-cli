#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import libs.lib_copa2022 as lib_copa2022

import datetime
import json
import os
import requests
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

novo_projeto = data_hora_str + "_CONFRONTOS_"


ARQUIVOS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
CUT = '/Volumes/Automator/'
# CUT = './Automator/'

if not os.path.isdir(CUT):
    script = ROOT + 'scripts/mountCut.scpt'
    parametros = ['osascript', script ]
    retorno = subprocess.call(parametros)


ID = 'copa2022_confrontos'
JSX = ROOT + 'scripts/copa2022_confrontos.jsx'
EXPORT = ROOT + 'export/copa2022_confrontos/'
DESTINO = CUT + '/DF/Copa2022/'
DESTINO2 = CUT + '/RJ/Copa2022/'


SAIDA = lib_copa2022.getConfrontosMataMataCopa2022()

hashes = TEMP + 'hash_confrontos_mata_mata.json'
with open(hashes) as f:
    try:
        hashes_dados = json.load(f)
    except:
        hashes_dados = {}


for item in SAIDA:
    fase = item['fase']
    jogos = item['jogos']
    hash = item['hash']
    # print(fase, hash)

    if fase not in hashes_dados or hashes_dados[fase] != hash:
        hashes_dados[fase] = hash
        if fase in ["Semi", "3º Lugar", "Final"]:
        # if fase in ["Quartas"]:
            jogos = jogos[0]['jogos']
            tamanho = int(len(jogos) / 2)
            for j in range(tamanho):
                index = j * 2
                dados = jogos[index] + jogos[index + 1]

                for i, dado in enumerate(dados):
                    aux_data = datetime.datetime.strptime(dado['data'], "%d/%m/%Y")
                    dia_semana = automator.DIAS_SEMANA_FULL[aux_data.weekday()]
                    datastr = dia_semana + " " + aux_data.strftime("%d")
                    dados[i]['data_str'] = datastr
                    dados[i]['cod_time1'] = lib_copa2022.paises.index(dado['nome_time1']) + 1
                    dados[i]['cod_time2'] = lib_copa2022.paises.index(dado['nome_time2']) + 1
                #
                aux = {
                    "grupo": fase.replace("  ", " "),
                    "rodada": " ",
                    "jogos": dados
                }
                arquivo = novo_projeto + fase + '_' +str(j)
                arquivo = arquivo.replace(' ', '-')
                arq_projeto = TEMP + arquivo + '.json'
                with open(arq_projeto, 'w') as f:
                    json.dump(aux, f)
                    # json.dump(aux, f, indent=4, sort_keys=True)

                # CRIA ARQUIVO AEP
                projetoAfter = TEMP + arquivo + '.aep'
                jsx = TEMP + arquivo + '.jsx'
                retorno = automator.copiaArquivo(JSX, jsx)
                retorno = automator.atualizaProjeto(jsx)

                # CRIA PASTA NO EXPORT
                export = EXPORT + ano + '/' + mes + '/' + dia + '/'
                if not os.path.isdir(export):
                    os.makedirs(export)

                # CRIA PASTA NO DESTINO
                dest = DESTINO + ano + '/' + mes + '/' + dia + '/'
                if not os.path.isdir(dest):
                    os.makedirs(dest)

                # CRIA PASTA NO DESTINO
                dest2 = DESTINO2 + ano + '/' + mes + '/' + dia + '/'
                if not os.path.isdir(dest2):
                    os.makedirs(dest2)

                renders = [
                {
                    "comp": "!Render1_FullHD",
                    "inicio": "1",
                    "fim": "0",
                    "OM": "MOV",
                    "arquivo": arquivo + "-FULLHD.mov"
                },
                # {
                #     "comp": "!Render2_1080",
                #     "inicio": "1",
                #     "fim": "1",
                #     "OM": "PNG",
                #     "arquivo": arquivo + "-1080.png",
                #     "renomear": True
                # },
                # {
                #     "comp": "!Render3_Vertical",
                #     "inicio": "1",
                #     "fim": "1",
                #     "OM": "PNG",
                #     "arquivo": arquivo + "-vertical.png",
                #     "renomear": True
                # }
                ]

                for render in renders:
                    comp = render['comp']
                    inicio  = render['inicio']
                    fim = render['fim']
                    om = render['OM']
                    nome_arquivo = render['arquivo']
                    arquivo = export + render['arquivo']

                    retorno = automator.geraArte(projetoAfter, comp, inicio, fim, om, arquivo)

                    if 'renomear' in render.keys():
                        print(arquivo)
                        os.rename(arquivo + '00001', arquivo)

                    retorno = os.system("cp  %s  %s" % (arquivo,  dest))
                    # retorno = os.system("cp  %s  %s" % (arquivo,  dest2))


# hashes = TEMP + 'hash_confrontos_mata_mata.json'
# with open(hashes, 'w') as f:
#     json.dump(hashes_dados, f)
