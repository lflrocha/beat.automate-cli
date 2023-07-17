# -*- coding: UTF-8 -*-

import libs.automator as automator

import datetime
import json
import os
import requests
import time
import urllib
from slugify import slugify

from twython import Twython
import mimetypes


ROOT = automator.getBase()
ARQS = ROOT + 'arquivos/'
TEMP = ROOT + 'temp/'
LOGS = ROOT + 'logs/'
DATA_HORA = automator.getDataHora()


twitter = Twython('jIVWKyXjdVbXOiTlI9X2w5P2C',
                  'Gbe1Il8bzQQ2D5JIPzp0fcBCGeRcQUdxTXLT36WH5nt8JoyxFD',
                  '788470921237504000-ekXu7nbZl7fg1gBMkD1O8rFuuYEcK30',
                  '2V26zANKmy2NemX7No1laSoSN2e3MpZwyMwqooHSfeiaS')

def getMensagem(novo_projeto, mensagem):
    mensagens = twitter.lookup_status(id=mensagem, tweet_mode='extended')
    if len(mensagens) == 1:
        mensagem = mensagens[0]
        user = mensagem['user']
        nome_perfil = user['name']
        usuario_perfil = user['screen_name']
        biografia_perfil = user['description']
        foto_perfil = user['profile_image_url_https']
        foto_topo = ''
        if 'profile_banner_url' in user.keys():
            foto_topo = user['profile_banner_url']
        dados_tweets = '{:,d}'.format(int(user['statuses_count'])).replace(',','.')
        dados_seguindo = "{:,d}".format(int(user['friends_count'])).replace(',','.')
        dados_seguidores = "{:,d}".format(int(user['followers_count'])).replace(',','.')
        dados_curtidas = "{:,d}".format(int(user['favourites_count'])).replace(',','.')

        # Foto do perfil
        perfil = foto_perfil.replace('_normal.','_400x400.')
        ext_perfil = perfil.rsplit('.', 1)
        if len(ext_perfil) > 1:
          ext_perfil = ext_perfil[1]
        else:
          ext_perfil = ''

        arq_img_perfil = novo_projeto + '_foto.' + ext_perfil
        urllib.request.urlretrieve(str(perfil), ROOT + 'temp/' + arq_img_perfil)

        if foto_topo:
            banner = str(foto_topo) + '/1500x500'
            arq_banner = novo_projeto + '_banner.jpg'
            urllib.request.urlretrieve(str(banner), ROOT + 'temp/' + novo_projeto + '_banner.jpg')
            os.rename(ROOT + 'temp/' + novo_projeto + '_banner.jpg', ROOT + 'temp/' + arq_banner)
        else:
            arq_banner = ''

        # msg = mensagem['full_text'].replace('"','\\"').replace('\n','\\n').replace("'","\\'")
        msg = mensagem['full_text']
        data = mensagem['created_at']
        media_type = ''
        media_url = ''
        aspect =  "false"
        legenda = ''
        midia = ''
        if 'extended_entities' in mensagem.keys():
            extended_entities = mensagem['extended_entities']
            media = extended_entities['media'][0]
            url = media['url']
            msg = msg.replace(url,'')
            media_type = media['type']

            if media_type == 'photo':
                media_url = media['media_url']
            if media_type == 'video':
                video_info = media['video_info']
                aspect = video_info['aspect_ratio']
                variants = video_info['variants']
                videos = {}
                for variant in variants:
                    if variant['content_type'] == 'video/mp4':
                        url = variant['url']
                        bitrate = variant['bitrate']
                        videos[bitrate] = url
                maior = sorted(videos.keys())
                maior = maior[-1]
                media_url = videos[maior]

            aux = media_url.rsplit('?',1)
            aux = aux[0]

            ext_midia = aux.rsplit('.', 1)
            if len(ext_midia) > 1:
              ext_midia = ext_midia[-1]
            else:
              ext_midia = ''

            midia = novo_projeto + '_midia_' +  '.' + ext_midia
            urllib.request.urlretrieve(str(media_url), ROOT + 'temp/' + midia)

        dataAux = data
        dataAux = dataAux.split(' ')
        dt_dia = dataAux[2]
        dt_mes = dataAux[1]
        if dt_mes == 'Jan':
            dt_mes = u'janeiro'
        elif dt_mes == 'Feb':
            dt_mes = u'fevereiro'
        elif dt_mes == 'Mar':
            dt_mes = u'março'
        elif dt_mes == 'Apr':
            dt_mes = u'abril'
        elif dt_mes == 'May':
            dt_mes = u'maio'
        elif dt_mes == 'Jun':
            dt_mes = u'junho'
        elif dt_mes == 'Jul':
            dt_mes = u'julho'
        elif dt_mes == 'Aug':
            dt_mes = u'agosto'
        elif dt_mes == 'Sep':
            dt_mes = u'setembro'
        elif dt_mes == 'Oct':
            dt_mes = u'outubro'
        elif dt_mes == 'Nov':
            dt_mes = u'novembro'
        elif dt_mes == 'Dec':
            dt_mes = u'dezembro'

        data = dt_dia + ' de ' +  dt_mes

        tweet = {
            'nome_perfil': nome_perfil,
            'usuario_perfil': usuario_perfil,
            'biografia_perfil': biografia_perfil,
            'foto_perfil': arq_img_perfil,
            'foto_topo': arq_banner,
            'dados_tweets': dados_tweets,
            'dados_seguindo': dados_seguindo,
            'dados_seguidores': dados_seguidores,
            'dados_curtidas': dados_curtidas,
            'texto': msg,
            'midia': midia,
            'tipo_midia': media_type,
            'aspecto':  aspect,
            'legenda': legenda,
            'data': data
        }
        return tweet
    else:
        return ''



def getTwitter2023(dados):

    novo_projeto = dados['novo_projeto']
    identificador = dados['identificador']
    arquivo_saida = slugify(novo_projeto + '-' + identificador)
    variaveis = dados['variaveis']

    url = variaveis['endereco']
    aux = url.split('/status/')
    dados_perfil = getMensagem(novo_projeto, aux[1])

    variaveis = dados_perfil



    renders = [
        {
            "comp": "!01_render",
            "inicio": "1",
            "fim": "0",
            "OM": "MAM",
            "arquivo": arquivo_saida + ".mov",
            "converter": "MP4"
        }
    ]

    saida = {"dados": variaveis, "renders": renders}
    return saida
