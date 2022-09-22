#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import libs.lib_abr as lib_abr
import urllib

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



def getTVBr7deSetembro2022Interatividade(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(identificador)

    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    nome = dados['nome']
    rede = dados['rede']
    cidade = dados['cidade']
    texto = dados['texto']
    foto_arquivo = dados['arquivo']
    foto_endereco = dados['endereco']

    ext = foto_arquivo.rsplit('.',1)[1]
    novo_nome_arq_imagem = 'imagem' + '-' + novo_projeto + '.' + ext
    urllib.request.urlretrieve(foto_endereco, TEMP + novo_nome_arq_imagem)

    aux_dados = {
        "nome": nome,
        "rede": rede,
        "cidade": cidade,
        "texto": texto,
        "foto_arquivo": novo_nome_arq_imagem,
    }

    renders = [
        {
            "comp": "!render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        },

    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida




def getTVBrEleicoes2022Agenda(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)

    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    nome = dados['nome']
    cargo = dados['cargo']
    partido = dados['partido']
    foto_arquivo = dados['foto_arquivo']
    foto_endereco = dados['foto_endereco']
    data = dados['data']
    local = dados['local']

    ext = foto_arquivo.rsplit('.',1)[1]
    novo_nome_arq_imagem = 'imagem' + '-' + novo_projeto + '.' + ext
    urllib.request.urlretrieve(foto_endereco, TEMP + novo_nome_arq_imagem)

    turno = {
        '': '',
        'manha': 'Manhã',
        'tarde': 'Tarde',
        'noite': 'Noite',
    }


    aux_dados = {
        "nome": nome,
        "cargo": cargo,
        "partido": partido,
        "foto_arquivo": novo_nome_arq_imagem,
        "data": data,
        "local": local,
        "linha1": dados["texto1"],
        "linha2": dados["texto2"],
        "linha3": dados["texto3"],
        "linha4": dados["texto4"],
        "linha5": dados["texto5"],
        "linha6": dados["texto6"],
        "turno1": dados["turno1"],
        "turno2": dados["turno2"],
        "turno3": dados["turno3"],
        "turno4": dados["turno4"],
        "turno5": dados["turno5"],
        "turno6": dados["turno6"],
    }

    renders = [
        {
            "comp": "!Render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MXF"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida



def getTVBrEleicoes2022Perfil(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    local = dados['local']

    nome = dados['nome']
    cargo = dados['cargo']
    partido = dados['partido']
    cod_partido = dados['cod_partido']
    uf = dados['uf']
    estado = dados['estado']
    naturalidade = dados['naturalidade']
    profissao = dados['profissao']
    perfil = dados['perfil']
    idade = dados['idade']
    foto = ROOT + 'assets/eleicoes2022/' + uf + '/' + cod_partido + '.jpg'

    aux_dados = {
        "local": local,
        "nome": nome,
        "cargo": cargo,
        "partido": partido,
        "foto": foto,
        "uf": uf,
        "estado": estado,
        "naturalidade": naturalidade,
        "profissao": profissao,
        "perfil": perfil,
        "foto": foto,
        "idade": str(idade) + ' anos',
    }

    renders = [
        {
            "comp": "!render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            # "converter": "MP4"
        }
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida





def getTVBrEleicoes2022MapaApuracao(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    url_consolidado = dados['url_consolidado']
    data_hora = dados['data_hora']
    arquivo_saida = slugify(identificador)
    arquivo_json = TEMP + "consolidado_" + data_hora + '.json'
    urllib.request.urlretrieve(url_consolidado, arquivo_json)

    with open(arquivo_json) as f:
        dados_consolidado = json.load(f)

    aux_dados = {
        "AC_dado": 0,
        "AL_dado": 0,
        "AP_dado": 0,
        "AM_dado": 0,
        "BA_dado": 0,
        "CE_dado": 0,
        "DF_dado": 0,
        "ES_dado": 0,
        "GO_dado": 0,
        "MA_dado": 0,
        "MT_dado": 0,
        "MS_dado": 0,
        "MG_dado": 0,
        "PA_dado": 0,
        "PB_dado": 0,
        "PR_dado": 0,
        "PE_dado": 0,
        "PI_dado": 0,
        "RJ_dado": 0,
        "RN_dado": 0,
        "RS_dado": 0,
        "RO_dado": 0,
        "RR_dado": 0,
        "SC_dado": 0,
        "SP_dado": 0,
        "SE_dado": 0,
        "TO_dado": 0,
        "BR_dado": "0%"
    }

    for item in dados_consolidado:
        id = item['sigla_uf'] + '_dado'
        valor_inteiro = item['secoes_totalizadas_percent'].split(',')
        aux_dados[id] = valor_inteiro[0]

        if id == "BR_dado":
            aux_dados[id] = aux_dados[id] + '%'

    renders = [
        {
            "comp": "!render",
            "inicio": "0",
            "fim": "0",
            "OM": "PNG",
            "arquivo": arquivo_saida + ".png",
            "renomear": True
        },
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida





def getTVBrEleicoes2022MapaGovernador(dados):
    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    url_consolidado = dados['url_consolidado']
    data_hora = dados['data_hora']
    arquivo_saida = slugify(identificador)
    arquivo_json = TEMP + "consolidado_" + data_hora + '.json'
    urllib.request.urlretrieve(url_consolidado, arquivo_json)

    with open(arquivo_json) as f:
        dados_consolidado = json.load(f)

    aux_dados = {
        "AC_dado": 0,
        "AL_dado": 0,
        "AP_dado": 0,
        "AM_dado": 0,
        "BA_dado": 0,
        "CE_dado": 0,
        "DF_dado": 0,
        "ES_dado": 0,
        "GO_dado": 0,
        "MA_dado": 0,
        "MT_dado": 0,
        "MS_dado": 0,
        "MG_dado": 0,
        "PA_dado": 0,
        "PB_dado": 0,
        "PR_dado": 0,
        "PE_dado": 0,
        "PI_dado": 0,
        "RJ_dado": 0,
        "RN_dado": 0,
        "RS_dado": 0,
        "RO_dado": 0,
        "RR_dado": 0,
        "SC_dado": 0,
        "SP_dado": 0,
        "SE_dado": 0,
        "TO_dado": 0,
    }

    for item in dados_consolidado:
        id = item['sigla_uf'] + '_dado'
        status_eleicao = item['status']
        if status_eleicao == "eleito":
            aux_dados[id] = 3
        elif status_eleicao == "turno2":
            aux_dados[id] = 2
        else:
            totalizadas = item['secoes_totalizadas_percent']
            if float(totalizadas.replace(',', '.')) > 0:
                aux_dados[id] = 1
            else:
                aux_dados[id] = 0

    renders = [
        {
            "comp": "!render",
            "inicio": "0",
            "fim": "0",
            "OM": "PNG",
            "arquivo": arquivo_saida + ".png",
            "renomear": True
        },
    ]

    saida = {"dados": aux_dados, "renders": renders}
    return saida
