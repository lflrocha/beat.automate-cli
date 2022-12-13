#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import libs.automator as automator
import urllib

import json
import os
import requests
from datetime import datetime
from slugify import slugify
import hashlib

ROOT = automator.getBase()
TEMP = ROOT + 'temp/'



background = {
    "#0000ff": "q1",
    "#00ffff": "q2",
    "#008000": "q3",
    "#cccccc": "q4",
    "#ff0000": "q5",
    "#003366": "q1",
    "#d37700": "q4"
}



paises = [
    "Alemanha",
    "Arábia Saudita",
    "Argentina",
    "Austrália",
    "Bélgica",
    "Brasil",
    "Camarões",
    "Canadá",
    "Coreia do Sul",
    "Costa Rica",
    "Croácia",
    "Dinamarca",
    "Equador",
    "Espanha",
    "Estados Unidos",
    "França",
    "Gana",
    "Holanda",
    "Inglaterra",
    "Irã",
    "Japão",
    "Marrocos",
    "México",
    "País de Gales",
    "Polônia",
    "Portugal",
    "Catar",
    "Senegal",
    "Sérvia",
    "Suíça",
    "Tunísia",
    "Uruguai",
    "A definir"
]


copa2022 = {
        "nome": "Copa do Mundo 2022",
        "id": "copa-do-mundo-2022",
        "categoria": "Seleções",
        "atual": 0,
        "fases": {
            "Primeira fase": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/classificacao/",
            "Oitavas": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/oitavas-copa-do-mundo-2022/classificacao/",
            "Quartas": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/quartas-copa-do-mundo-2022/classificacao/",
            "Semi": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/semifinal-copa-do-mundo-2022/classificacao/",
            "3º Lugar": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/terceiro-copa-do-mundo-2022/classificacao/",
            "Final": "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/final-copa-do-mundo-2022/classificacao/",
        },
        "confrontos": {
            "Grupo A": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3929/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3929/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3929/jogos/",
            ],
            "Grupo B": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3930/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3930/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3930/jogos/",
            ],
            "Grupo C": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3931/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3931/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3931/jogos/",
            ],
            "Grupo D": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3932/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3932/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3932/jogos/",
            ],
            "Grupo E": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3933/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3933/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3933/jogos/",
            ],
            "Grupo F": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3934/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3934/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3934/jogos/",
            ],
            "Grupo G": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3935/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3935/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3935/jogos/",
            ],
            "Grupo H": [
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/1/grupo/3936/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/2/grupo/3936/jogos/",
                "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/rodada/3/grupo/3936/jogos/",
            ]
        }
    }


nomes_copa = {
  'copa-do-mundo-2022': {
    'Alemanha': ['Alemanha', 'paises/alemanha'],
    'Arábia Saudita': ['Arábia Saudita', 'paises/arabia_saudita'],
    'Argentina': ['Argentina', 'paises/argentina'],
    'Austrália': ['Austrália', 'paises/australia'],
    'Bélgica': ['Bélgica', 'paises/belgica'],
    'Brasil': ['Brasil', 'paises/brasil'],
    'Camarões': ['Camarões', 'paises/camaroes'],
    'Canadá': ['Canadá', 'paises/canada'],
    'Catar': ['Catar', 'paises/catar'],
    'Coreia do Sul': ['Coreia do Sul', 'paises/coreia_do_sul'],
    'Costa Rica': ['Costa Rica', 'paises/costa_rica'],
    'Croácia': ['Croácia', 'paises/croacia'],
    'Dinamarca': ['Dinamarca', 'paises/dinamarca'],
    'Equador': ['Equador', 'paises/equador'],
    'Espanha': ['Espanha', 'paises/espanha'],
    'Estados Unidos': ['Estados Unidos', 'paises/estados_unidos'],
    'França': ['França', 'paises/franca'],
    'Gana': ['Gana', 'paises/gana'],
    'Holanda': ['Holanda', 'paises/holanda'],
    'Inglaterra': ['Inglaterra', 'paises/inglaterra'],
    'Irã': ['Irã', 'paises/ira'],
    'Japão': ['Japão', 'paises/japao'],
    'Marrocos': ['Marrocos', 'paises/marrocos'],
    'México': ['México', 'paises/mexico'],
    'País de Gales': ['País de Gales', 'paises/pais_de_gales'],
    'Polônia': ['Polônia', 'paises/polonia'],
    'Portugal': ['Portugal', 'paises/portugal'],
    'Senegal': ['Senegal', 'paises/senegal'],
    'Sérvia': ['Sérvia', 'paises/servia'],
    'Suíça': ['Suíça', 'paises/suica'],
    'Tunísia': ['Tunísia', 'paises/tunisia'],
    'Uruguai': ['Uruguai', 'paises/uruguai'],
    'A definir': ['A definir', 'paises/uruguai'],
    }
}




def getTabelaCopa2022():

    url = "https://api.globoesporte.globo.com/tabela/d91a3f90-c034-407a-a94f-84771a7b3783/fase/fase-grupos-copa-do-mundo-2022/classificacao/"

    r = requests.get(url)
    json = r.json()
    tipo = json['fase']['tipo']['tipo_id']
    aux = []

    if tipo == "3":
        grupos = json["grupos"]
        for item in grupos:
            grupo = item['nome_grupo']
            classificacao = item['classificacao']
            tabela = []
            for linha in classificacao:
                vet = {}
                vet['time'] = linha['nome_popular']
                vet['sigla'] = linha['sigla']
                vet['variacao'] = linha['variacao']
                vet['pos'] = linha['ordem']
                vet['pon'] = linha['pontos']
                vet['jog'] = linha['jogos']
                vet['vit'] = linha['vitorias']
                vet['emp'] = linha['empates']
                vet['der'] = linha['derrotas']
                vet['gp'] = linha['gols_pro']
                vet['gc'] = linha['gols_contra']
                vet['sg'] = linha['saldo_gols']
                vet['sg'] = linha['saldo_gols']
                vet['cod'] = paises.index(linha['nome_popular']) + 1
                bg = linha['faixa_classificacao_cor']
                q = "q4"
                if bg in background.keys():
                    q = background[bg]
                vet['bg'] = q
                tabela.append(vet)
            hash = hashlib.md5(bytes(str(tabela), "utf-8")).hexdigest()
            aux.append({'nome': grupo, 'dados': tabela, 'hash': hash})

    return aux



def getConfrontosCopa2022():

    # r = requests.get('https://api.fifa.com/api/v3/calendar/matches?language=pt&count=500&idSeason=255711')
    # dados = r.json()
    # aux = dados['Results']

    nome = copa2022['nome']
    id = copa2022['id']
    categoria = copa2022['categoria']
    fase_atual = copa2022['atual']
    fases = copa2022['fases']
    confrontos = copa2022['confrontos']
    origem = id


    arq_json = ROOT + '/temp/' + origem + '/' + id + '_confrontos.json'
    if not os.path.isdir(ROOT + '/temp/' + origem):
        os.mkdir(ROOT + '/temp/' + origem)

    confrontos = get_dados_confrontos(id, categoria, confrontos)
    with open(arq_json, 'w') as f:
        json.dump(confrontos, f)


    # arq_json = ROOT + '/temp/' + origem + '/' + id + '_mata_mata.json'
    # if not os.path.isdir(ROOT + '/temp/' + origem):
    #     os.mkdir(ROOT + '/temp/' + origem)
    #
    # mata_mata = get_dados_mata_mata(id, categoria, fases)
    # with open(arq_json, 'w') as f:
    #     json.dump(mata_mata, f)
    #
    #
    # with open('/Users/lflrocha/Sistemas/ebc.copa2022/temp/copa-do-mundo-2022/copa-do-mundo-2022_confrontos.json') as f:
    #     dados = json.load(f)
    return confrontos



def get_dados_confrontos(campeonato, categoria, confrontos):
    retorno = []
    for grupo in confrontos.keys():
        dados = get_dados_confrontos_json(campeonato, categoria, grupo, confrontos[grupo])
        hash = hashlib.md5(bytes(str(dados), "utf-8")).hexdigest()
        retorno.append({"grupo": grupo, "dados":  dados, "hash": hash})
    return retorno


def get_dados_confrontos_json(campeonato, categoria, fase, urls):
    saida = {}
    for i, url in enumerate(urls):
        rodada = "Rodada  %s" % str(i + 1)
        r = requests.get(url)
        aux = r.json()

        saida[rodada] = []
        for dados in aux:
            data = dados['data_realizacao']
            data = datetime.strptime(data, "%Y-%m-%dT%H:%M")
            data_str = data.strftime('%d/%m/%Y')
            jogo = {
                "nome_time1": dados['equipes']['mandante']['nome_popular'],
                "sigla_time1":  dados['equipes']['mandante']['sigla'],
                "nome_time2":  dados['equipes']['visitante']['nome_popular'],
                "sigla_time2":  dados['equipes']['visitante']['sigla'],
                "placar_time1":  dados['placar_oficial_mandante'],
                "penalti_time1":  dados['placar_penaltis_mandante'],
                "placar_time2":  dados['placar_oficial_visitante'],
                "penalti_time2":  dados['placar_penaltis_visitante'],
                "data":  data_str,
                "hora":  dados['hora_realizacao'],
                "estadio":  dados['sede']['nome_popular'],
            }
            saida[rodada].append(jogo)
    return saida

















def getConfrontosMataMataCopa2022():

    nome = copa2022['nome']
    id = copa2022['id']
    categoria = copa2022['categoria']
    fase_atual = copa2022['atual']
    fases = copa2022['fases']
    origem = id

    arq_json = ROOT + '/temp/' + origem + '/' + id + '_mata_mata.json'
    if not os.path.isdir(ROOT + '/temp/' + origem):
        os.mkdir(ROOT + '/temp/' + origem)

    mata_mata = get_dados_mata_mata(id, categoria, fases)
    with open(arq_json, 'w') as f:
        json.dump(mata_mata, f)

    return mata_mata


# JOGOS MATA MATA
def get_dados_mata_mata(campeonato, categoria, fases):
    retorno = []
    for fase in fases.keys():
        dados = get_dados_mata_mata_json(campeonato, categoria, fase, fases[fase])
        hash = hashlib.md5(bytes(str(dados), "utf-8")).hexdigest()

        retorno.append({"fase": fase, "jogos":  dados, "hash": hash})
    return retorno


def get_jogo_mata_mata(campeonato, dados):
    jogos = []
    for jogo in dados:
        vet = {}
        aux = jogo['equipes']['mandante']
        if 'nome_popular' in  aux.keys():
            nome = jogo['equipes']['mandante']['nome_popular']
            sigla = jogo['equipes']['mandante']['sigla']
            vet['nome_time1'] = nome
            vet['sigla_time1'] = sigla
        else:
            vet['nome_time1'] = "A definir"
            vet['sigla_time1'] = "ZZZ"

        aux = jogo['equipes']['visitante']
        if 'nome_popular' in  aux.keys():
            nome = jogo['equipes']['visitante']['nome_popular']
            sigla = jogo['equipes']['visitante']['sigla']
            vet['nome_time2'] = nome
            vet['sigla_time2'] = sigla
        else:
            vet['nome_time2'] = "A definir"
            vet['sigla_time2'] = "ZZZ"

        vet['placar_time1'] = jogo['placar_oficial_mandante']
        vet['penalti_time1'] = jogo['placar_penaltis_mandante']
        vet['placar_time2'] = jogo['placar_oficial_visitante']
        vet['penalti_time2'] = jogo['placar_penaltis_visitante']
        data = ""
        if jogo['data_realizacao']:
            aux = datetime.strptime(jogo['data_realizacao'], "%Y-%m-%d")
            data = aux.strftime("%d/%m/%Y")
        vet['data'] = data
        vet['hora'] = jogo['hora_realizacao'][:5]
        vet['estadio'] = "A definir"
        if 'sede' in jogo.keys():
            if jogo['sede']:
                if 'nome_popular' in jogo['sede'].keys():
                    vet['estadio'] = jogo['sede']['nome_popular']
        if vet['estadio'] == "A definir" and vet['placar_time1'] is not None and vet['placar_time2'] is not None:
            vet['estadio'] = ""

        jogos.append(vet)
    return jogos


def get_dados_mata_mata_json(campeonato, categoria, fase, url):
    r = requests.get(url)
    json = r.json()
    tipo = json['fase']['tipo']['tipo_id']
    saida = []

    if tipo == "2":
        secao = json['secao']
        aux = []
        for item in secao:
            chave = item['chave']
            for grupo in chave:
                jogos = grupo['jogos']
                aux.append(get_jogo_mata_mata(campeonato, jogos))
        saida.append({"tipo": tipo, "jogos": aux})

    return saida
