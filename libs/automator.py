# -*- coding: UTF-8 -*-

import ast
import os
import smtplib
import sys
import logging
import requests
import json
import platform
import subprocess
import shutil
from bs4 import BeautifulSoup
from os.path import dirname, abspath
from datetime import datetime, timedelta

import qrcode
from PIL import Image


#ROOT = '/Volumes/Automator/Automator2019/'
ROOT = dirname(dirname(abspath(__file__))) + '/'
CUT = '/Volumes/cut/Automator/'

TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
BIN = ROOT + 'bin/'

AERENDER = '/Applications/Adobe\ After\ Effects\ CS6/aerender'
AERENDER = 'C:/Program Files/Adobe/Adobe After Effects CS6/Support Files/aerender.exe'
AERENDER = '/Applications/Adobe After Effects 2023/aerender'

AEFX = 'C:/Program Files/Adobe/Adobe After Effects CS6/Support Files/AfterFX.exe'
SCPT = ROOT + 'scripts/atualizaProjeto.scpt'

DIAS_SEMANA = [
    'Seg',
    'Ter',
    'Qua',
    'Qui',
    'Sex',
    'Sab',
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


def enviaCut(origem, destino):
    "Faz a cópia do arquivo gerado para o cut."
    plataforma = platform.system()
    retorno = ""
    if plataforma == "Darwin":
        # destino = '/Volumes/Automator/' + destino
        if not os.path.isdir(CUT):
            script = ROOT + 'scripts/mountCut.scpt'
            parametros = ['osascript', script ]
            retorno = subprocess.call(parametros)
        if not os.path.isdir(destino):
            retorno = os.makedirs(destino)
        if os.path.isdir(destino):
            if os.path.isfile(origem):
                retorno = copiaArquivo(origem, destino)
    elif plataforma == "Windows":
        origem = origem.replace('/','\\')
        destino = 'q:\\Automator\\' + destino
        if not os.path.isdir("q:\\"):
            subprocess.call(r'net use Q: /del', shell=True)
            subprocess.call(r'net use Q: \\10.61.172.22\cut\ /user:automator automator!2018', shell=True)
        if not os.path.isdir(destino):
            retorno = os.makedirs(destino)
        if os.path.isdir(destino):
            if os.path.isfile(origem):
                retorno = copiaArquivo(origem, destino)
    return retorno


def geraArte(projeto, comp, inicio, fim, output_module, output):
    "Gera arte"

    if not inicio:
        inicio = "1"

    # inicio = "1"
    parametros = [AERENDER, '-project', projeto, '-comp', comp, '-s', inicio, '-e', fim,  '-OMtemplate', output_module, '-output', output]

    if not fim or fim == "0":
        parametros = [AERENDER, '-project', projeto, '-comp', comp, '-s', inicio,  '-OMtemplate', output_module, '-output', output]

    retorno = subprocess.call(parametros)
    return retorno


def enviaEmail(assunto, mensagem, destinatarios, arquivos):
    msg = MIMEMultipart()

    msg['From'] = "automator@ebc.com.br"
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
    server = smtplib.SMTP('smtp.ebc.com.br', 587)
    server.ehlo()
    server.starttls()
    server.login('automator@ebc.com.br', 'automator!2018')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()


def converterMP4(origem, destino):
    parametros = [FFMPEG, '-i', origem, destino ]
    retorno = subprocess.call(parametros)
    return retorno

def converter(tipo, arquivo):
    arq_out = arquivo.rsplit('.mov', 1)
    if tipo == "MXF":
        arq_out = arq_out[0] + '.mxf'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt', 'yuv422p', '-vcodec', 'mpeg2video', '-non_linear_quant', '1', '-flags', '+ildct+ilme', '-top', '1', '-dc', '10', '-intra_vlc', '1', '-qmax', '3', '-lmin', '1*QP2LAMBDA', '-vtag', 'xd5c', '-rc_max_vbv_use', '1', '-rc_min_vbv_use', '1', '-g', '12', '-b:v', '50000k', '-minrate', '50000k', '-maxrate', '50000k', '-bufsize', '8000k', '-acodec', 'pcm_s16le', '-ar', '48000', '-bf', '2', '-ac', '2', arq_out]
        retorno = subprocess.call(parametros)
    elif tipo == "MP4":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-b:v', '5M', '-vcodec', 'h264', '-an', arq_out]
        retorno = subprocess.call(parametros)
    elif tipo == "MP4-AUDIO":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-b:v', '5M', '-vcodec', 'h264', arq_out]
        retorno = subprocess.call(parametros)


    elif tipo == "JCDECAUX":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-b:v', '4M', '-vcodec', 'h264', '-an', arq_out]
        retorno = subprocess.call(parametros)
    elif tipo == "JCDECAUX-LOW":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-b:v', '1M', '-vcodec', 'h264', '-fs', '1000000',  '-an', arq_out]
        retorno = subprocess.call(parametros)
    elif tipo == "JCDECAUX-ROTATE":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-vf', "transpose=2", '-b:v', '1M', '-vcodec', 'h264', '-fs', '5000000',  '-an', arq_out]
        retorno = subprocess.call(parametros)
    elif tipo == "JCDECAUX-ODD":
        arq_out = arq_out[0] + '.mp4'
        parametros = [BIN + 'ffmpeg', '-i', arquivo, '-y', '-pix_fmt',  'yuv420p', '-vf', "crop=trunc(iw/2)*2:trunc(ih/2)*2", '-b:v', '900k', '-vcodec', 'h264', '-fs', '1000000', '-an', arq_out]
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


def geraQRCode(link, arquivo):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img_qr_big = qr.make_image(fill_color="black", back_color="white")
    img_qr_big.save(TEMP + arquivo)


def resizeImage(arquivo):
    from PIL import Image

    foto = Image.open(arquivo).convert('RGB')
    f_w = foto.size[0]
    f_h = foto.size[1]

    if  (f_w / f_h) > (1920/1080):
        novo_w = 1920 * (f_h / 1080.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1080 * (f_w / 1920.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1920,1080), Image.ANTIALIAS)
    foto.save(arquivo)


def resizeImage1080X1920(arquivo):
    from PIL import Image

    foto = Image.open(arquivo).convert('RGB')
    f_w = foto.size[0]
    f_h = foto.size[1]

    if  (f_w / f_h) > (1080/1920):
        novo_w = 1080 * (f_h / 1920.0)
        x1 = (f_w - novo_w) / 2
        y1 = 0
        x2 = x1 + novo_w
        y2 = f_h
        foto = foto.crop((x1, y1, x2, y2))
    else:
        novo_h = 1920 * (f_w / 1080.0)
        y1 = (f_h - novo_h) / 2
        x1 = 0
        y2 = y1 + novo_h
        x2 = f_w
        foto = foto.crop((x1, y1, x2, y2))
    foto = foto.resize((1080,1920), Image.ANTIALIAS)
    foto.save(arquivo)
