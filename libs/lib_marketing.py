# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr

import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'

def getMktMidiaIndoorAgencia2023(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    link = variaveis['link']

    aux_dados = lib_abr.getDestaqueAgencia(link, "1")

    renders = [
        {
            "comp": "render01",
            "inicio": "180",
            "fim": "180",
            "OM": "JPEG",
            "arquivo": arquivo_saida + "-192x288_relogio_SP.jpg",
            "renomear": True
        },
        {
            "comp": "render06",
            "inicio": "180",
            "fim": "180",
            "OM": "JPEG",
            "arquivo": arquivo_saida + "-2160x3840_relogio_SP.jpg",
            # "renomear": True
        },
        {
            "comp": "render01",
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-192x288_relogio_SP.mov",
            "converter": "JCDECAUX-LOW"
        },
        {
            "comp": "render02",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-880x400_aeroporto_BSB.mov",
            "converter": "JCDECAUX"
        },
        {
            "comp": "render03",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1080x1920_aeroporto_BSB.mov",
            "converter": "JCDECAUX-ROTATE"
        },
        {
            "comp": "render04",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1152x768_aeroporto_BSB.mov",
            "converter": "JCDECAUX"
        },
        {
            "comp": "render05",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1920x1080_aeroporto_BSB.mov",
            "converter": "JCDECAUX"
        },
        {
            "comp": "render06",
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-2160x3840_relogio_SP.mov",
            "converter": "JCDECAUX"
        },
        {
            "comp": "render07",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1920x1152_aeroporto_BSB.mov",
            "converter": "JCDECAUX"
        },
        {
            "comp": "render08",
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-225x337_relogio_SP.mov",
            "converter": "JCDECAUX-ODD"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida


def getMktMidiaIndoorTVBrasil2022(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    link = variaveis['link']

    arq_qrcode = novo_projeto + '_qrcode.png'
    arq_video = variaveis['arquivo']
    automator.geraQRCode(link, arq_qrcode)
    aux_dados = {}
    aux_dados['texto1'] = variaveis['texto1']
    aux_dados['texto2'] = variaveis['texto2']
    aux_dados['arq_qrcode'] = arq_qrcode
    aux_dados['arq_video'] = arq_video

    caminho_video = "/Volumes/Automator_Envios/Marketing/"
    if not os.path.isdir(caminho_video):
        retorno = os.system('osascript '+ROOT+'scripts/mountEnvio.scpt')
    retorno = os.system('cp "' + caminho_video + arq_video + '" "' + TEMP + '"')

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_tvbrasil.mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida


def getMktMidiaIndoorTVBrasilPlay2022(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    link = variaveis['link']

    arq_qrcode = novo_projeto + '_qrcode.png'
    arq_video = variaveis['arquivo']
    automator.geraQRCode(link, arq_qrcode)
    aux_dados = {}
    aux_dados['texto1'] = variaveis['texto1']
    aux_dados['texto2'] = variaveis['texto2']
    aux_dados['arq_qrcode'] = arq_qrcode
    aux_dados['arq_video'] = arq_video

    caminho_video = "/Volumes/Automator_Envios/Marketing/"
    if not os.path.isdir(caminho_video):
        retorno = os.system('osascript '+ROOT+'scripts/mountEnvio.scpt')
    retorno = os.system('cp "' + caminho_video + arq_video + '" "' + TEMP + '"')

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_tvbrasilplay.mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida


def getMktMidiaIndoorRadioNacional2022(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    link = variaveis['link']

    arq_qrcode = novo_projeto + '_qrcode.png'
    arq_video = variaveis['arquivo']
    automator.geraQRCode(link, arq_qrcode)
    aux_dados = {}
    aux_dados['texto1'] = variaveis['texto1']
    aux_dados['texto2'] = variaveis['texto2']
    aux_dados['arq_qrcode'] = arq_qrcode
    aux_dados['arq_video'] = arq_video

    caminho_video = "/Volumes/Automator_Envios/Marketing/"
    if not os.path.isdir(caminho_video):
        retorno = os.system('osascript '+ROOT+'scripts/mountEnvio.scpt')
    retorno = os.system('cp "' + caminho_video + arq_video + '" "' + TEMP + '"')

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "_radionacional.mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida
