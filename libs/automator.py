# -*- coding: UTF-8 -*-

import os
import smtplib
import sys
import requests
import json
import platform
import subprocess
import shutil
import ast

from os.path import dirname, abspath
from datetime import datetime, timedelta

import os
import subprocess

from dotenv import load_dotenv
import os

ROOT = dirname(dirname(abspath(__file__))) + '/'

TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
BIN = ROOT + 'bin/'

AERENDER_WIN = 'C:/Program Files/Adobe/Adobe After Effects 2025/Support Files/aerender.exe'
AERENDER_MAC = '/Applications/Adobe After Effects 2025/aerender'

AEFX = 'C:/Program Files/Adobe/Adobe After Effects 2025/Support Files/AfterFX.exe'
SCPT = ROOT + 'scripts/atualizaProjeto.scpt'

DIAS_SEMANA = [
    'Seg',
    'Ter',
    'Qua',
    'Qui',
    'Sex',
    'Sáb',
    'Dom',
]

DIAS_SEMANA_FULL = [
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sábado',
    'Domingo',
]

def getBase():
    return ROOT


def alteraStatus(endereco, status):
    url = endereco + '/setWorkflowState?acao=' + status
    r = requests.get(url)
    aux = r.status_code
    return aux


def baixaLista(endereco):
    url = endereco
    req = requests.get(url)
    aux = req.text
    retorno = []
    if len(aux) > 0:
        retorno = ast.literal_eval(aux)
    return retorno


def buscaDados(endereco):
    url = endereco + '/getAutomatorText'
    req = requests.get(url)
    aux = req.json()
    return aux


def baixaArquivos(dados):
    "Baixa arquivos para o temp"
    # arquivos = eval(dados)
    for enderecofoto, nome in dados:
        r = requests.get(enderecofoto)
        open(TEMP + nome, 'wb').write(r.content)


def copiaArquivo(origem, destino):
    retorno = shutil.copy2(origem, destino)
    if destino in retorno:
        retorno = 0
    else:
        retorno = 1
    return retorno


def atualizaProjeto(projeto):
    plataforma = platform.system()
    if plataforma == "Darwin":
        scpt = ROOT + 'scripts/atualizaProjeto.scpt'
        parametros = ['osascript', scpt , projeto]
        retorno = subprocess.call(parametros)
    elif plataforma == "Windows":
        parametros = [AEFX, "-noui" ,"-r", projeto]
        retorno = subprocess.call(parametros)
    return retorno


def geraArte(projeto, comp, inicio, fim, output_module, output):
    """Gera arte"""

    plataforma = platform.system()
    AERENDER = AERENDER_WIN if plataforma == "Windows" else AERENDER_MAC

    if not os.path.exists(AERENDER):
        raise FileNotFoundError(f"aerender não encontrado: {AERENDER}")

    if not os.path.exists(projeto):
        raise FileNotFoundError(f"Projeto After não encontrado: {projeto}")

    if not inicio:
        inicio = "1"

    parametros = [
        str(AERENDER),
        "-project", str(projeto),
        "-comp", str(comp),
        "-s", str(inicio),
    ]

    if fim and str(fim) != "0":
        parametros += ["-e", str(fim)]

    parametros += [
        "-OMtemplate", str(output_module),
        "-output", str(output),
    ]

    print("PARAMETROS:")
    for p in parametros:
        print(repr(p))

    retorno = subprocess.call(parametros)
    return retorno


def enviaEmail(assunto, mensagem, destinatarios, arquivos):
    msg = MIMEMultipart()

    load_dotenv()
    senha = os.getenv("SMTP_PASSWORD")


    msg['From'] = "lflrocha@gmail.com"
    msg['To'] = ", ".join(destinatarios)
    msg['Subject'] = assunto
    if arquivos is not None:
        for arquivo in arquivos:
            file_name=arquivo.split("/")[-1]
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(arquivo, "rb").read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment' ,filename=file_name)
            msg.attach(part)

    msg.attach(MIMEText(mensagem,'html'))
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('lflrocha@gmail.com', senha)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()



def converter(tipo, arquivo):
    arq_out = arquivo.rsplit('.mov', 1)
    if tipo == "MXF":
        arq_out = arq_out[0] + '.mxf'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt', 'yuv422p', '-vcodec', 'mpeg2video', '-non_linear_quant', '1', '-flags', '+ildct+ilme', '-top', '1', '-dc', '10', '-intra_vlc', '1', '-qmax', '3', '-lmin', '1*QP2LAMBDA', '-vtag', 'xd5c', '-rc_max_vbv_use', '1', '-rc_min_vbv_use', '1', '-g', '12', '-b:v', '50000k', '-minrate', '50000k', '-maxrate', '50000k', '-bufsize', '8000k', '-acodec', 'pcm_s16le', '-ar', '48000', '-bf', '2', '-ac', '2', arq_out]
        retorno = subprocess.call(parametros)

    return(arq_out)



def getDataHora(*args):
    """
    Retorna a data em uma string.
    Se houver parâmetro, irá adicionar o número de dias passados a data atual.
    """

    data = datetime.now()

    if len(args) == 0:
        return data.strftime('%y%m%d-%H%M%S')

    if len(args) == 1:
        numero = isinstance( args[0], ( int, long ) )
        if numero:
            delta = timedelta(days=args[0])
            data = data + delta
            return data.strftime('%y%m%d-%H%M%S')
        else:
            raise NameError('Parâmetro deve ser um número.')

    if len(args) > 1:
        raise NameError('Somente um parâmetro deve ser informado.')



def guess_mime_type(f):
    '''
    Function guesses an image mime type.
    Supported filetypes are JPG, BMP, PNG.
    '''
    with open(f, 'rb') as f:
        data = f.read(11)
    if data[:4] == '\xff\xd8\xff\xe0' and data[6:] == 'JFIF\0':
        return 'jpg'
    elif data[1:4] == "PNG":
        return 'png'
    elif data[:2] == "BM":
        return 'bmp'
    else:
        return ''
