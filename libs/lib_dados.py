#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr

import json

from slugify import slugify


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
            "arquivo": arquivo_saida + "-01.jpg",
            "renomear": True
        },
        {
            "comp": "render02",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-02.jpg",
        },
        {
            "comp": "render03",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-03.jpg",
        },
        {
            "comp": "render04",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-04.jpg",
        },
        {
            "comp": "render05",
            "inicio": "1",
            "fim": "0",
            "OM": "MOV",
            "arquivo": arquivo_saida + "-05.jpg",
        },
        {
            "comp": "render06",
            "inicio": "180",
            "fim": "180",
            "OM": "JPEG",
            "arquivo": arquivo_saida + "-06.jpg",
            "renomear": True
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

    if aux_dia == "Seg a Sex":
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
