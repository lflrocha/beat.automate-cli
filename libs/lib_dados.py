#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import urllib
import os
import json

from slugify import slugify

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'

def getMktMidiaIndoorAgencia2022(dados):
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
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-192x288_relogio_SP.mov",
            "converter": "MP4-LOW"
        },
        {
            "comp": "render02",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-880x400_aeroporto_BSB.mov",
            "converter": "MP4"
        },
        {
            "comp": "render03",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1080x1920_aeroporto_BSB.mov",
            "converter": "MP4-ROTATE"
        },
        {
            "comp": "render04",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1152x768_aeroporto_BSB.mov",
            "converter": "MP4"
        },
        {
            "comp": "render05",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1920x1080_aeroporto_BSB.mov",
            "converter": "MP4"
        },
        {
            "comp": "render06",
            "inicio": "1",
            "fim": "300",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-2160x3840_relogio_SP.mov",
            "converter": "MP4"
        },
        {
            "comp": "render07",
            "inicio": "1",
            "fim": "450",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-1920x1152_aeroporto_BSB.mov",
            "converter": "MP4"
        },

    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida


def getTVBrProgramacaoChamadas2022(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    aux_dados = variaveis
    aux_dia = variaveis['dia']

    if aux_dia in ["Seg a Sex", "Seg a Sáb", "Ter a Sex"]:
        aux_comp_dia = "!Render_SeloSEGASEX"
    else:
        aux_comp_dia = "!Render_SeloDia"

    renders = [
        {
            "comp": "!Render_AssinaChamadaAlphaDia",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-01.mov",
        },
        {
            "comp": "!Render_AssinaChamadaAlphaHoje",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-02.mov",
        },
        {
            "comp": "!Render_AssinaChamadaDia",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-03.mov",
        },
        {
            "comp": "!Render_AssinaChamadaHoje",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-04.mov",
        },
        {
            "comp": aux_comp_dia,
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-05.mov",
        },
        {
            "comp": "!Render_SeloHoje",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV+ALPHA",
            "arquivo": arquivo_saida + "-06.mov",
        },
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida

def getTVBrProgramacaoDestaqueAgencia2022(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']
    link1 = variaveis['link1']
    link2 = variaveis['link2']
    link3 = variaveis['link3']

    saida = []
    saida.append(lib_abr.getDestaqueAgencia(link1, "1"))
    saida.append(lib_abr.getDestaqueAgencia(link2, "2"))
    saida.append(lib_abr.getDestaqueAgencia(link3, "3"))
    aux_dados = {"noticias": saida}

    renders = [
        {
            "comp": "!_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
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
            "arquivo": arquivo_saida + "_tvbrasil_SP.mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida








def getTVBrRadiosChamada(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    variaveis = dados['variaveis']

    arq_imagem1 = variaveis['arq_imagem1']
    arq_imagem2 = variaveis['arq_imagem2']
    arq_imagem3 = variaveis['arq_imagem3']
    arq_audio = variaveis['arq_audio']

    end_imagem1 = variaveis['end_imagem1']
    end_imagem2 = variaveis['end_imagem2']
    end_imagem3 = variaveis['end_imagem3']
    end_audio = variaveis['end_audio']

    download = [
        (end_imagem1, arq_imagem1),
        (end_imagem2, arq_imagem2),
        (end_imagem3, arq_imagem3),
        (end_audio, arq_audio)
    ]

    automator.baixaArquivos(download)

    automator.resizeImage(TEMP + arq_imagem1)
    automator.resizeImage(TEMP + arq_imagem2)
    automator.resizeImage(TEMP + arq_imagem3)

    renders = [
        {
            "comp": "01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + "_radios_chamada.mov",
            "converter": "MP4-AUDIO"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
