"""
调用百度语音api识别语音
"""
import base64
import json
import logging
import logging.config
import os
import re
import wave
from os import system

import pyaudio
import requests

server_url = 'http://vop.baidu.com/server_api'
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()


def init():
    """
    初始化程序，读取配置文件

    :return: 配置信息 {'api-key':xxx,'secret-key':xxx}
    """
    logger = logging.getLogger(__name__)
    logger.info('init begin.')
    try:
        file = open('baiduDev.json', encoding="utf-8")
        conf = json.load(file)
        logger.info('rend config file success.')
        return conf['baidu']
    except BaseException as e:
        logger.error(e)
        raise BaseException('init failed')


def get_token(api_key, secret_key):
    """
    从服务器获取一次token

    :param api_key: 百度开发者提供的api-key
    :param secret_key: 百度开发者提供的secret-key
    :return: 'xxxxxtoken'
    """
    logger = logging.getLogger(__name__)
    getTokenURL = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}"
    getTokenURL = getTokenURL.format(api_key, secret_key)
    logger.info('token url:' + getTokenURL)
    resp = requests.post(getTokenURL)
    access = resp.json()
    if access['access_token'] is not None:
        return access['access_token']
    else:
        logger.error('get_token() : no token got.')
        raise BaseException('get token failed.')


def prepare_file(filename):
    logger = logging.getLogger(__name__)
    # get file length
    file_size = os.path.getsize(filename)
    logger.info('file size:' + str(file_size))
    pcm = open(filename, mode='rb')
    all_pcm = pcm.read(file_size)
    based_data = base64.encodebytes(all_pcm)
    based_data = based_data.decode('utf-8').replace('\n', '')
    return {'size': file_size, 'data': based_data, 'format': filename[filename.rfind('.') + 1:]}


def send_request(filedata, token, cuid='yang', rate=8000, channel=1):
    logger = logging.getLogger(__name__)
    parameter = {
        "format": filedata['format'],
        "rate": rate,
        "channel": channel,
        "token": token,
        "cuid": cuid,
        "len": filedata['size'],
        "speech": filedata['data']
    }
    logger.info('parameter:')
    logger.info(parameter)
    header = {'Content-Type': 'application/json; charset=utf-8'}
    resp = requests.post(server_url, json=parameter, headers=header)
    result = resp.json()
    return result


def deal_words(voice_data):
    result = voice_data['result']
    no_restart = re.compile('.*不\w{0,3}重启.*')
    restart = re.compile('.*重启.*')
    if result is None or result == []:
        raise BaseException('no result found!')
    for s in result:
        if (not no_restart.match(s)) and restart.match(s):
            print('重启')
            system('shutdown /r /t 120')
            return
    print('不重启')


def main():
    logging.config.fileConfig("log.conf")
    logger = logging.getLogger(__name__)
    conf = init()
    input('press "Enter" key to start recording.')
    record()
    api_key = conf['api-key']
    secret_key = conf['secret-key']
    token = get_token(api_key, secret_key)
    file_data = prepare_file('output.wav')
    resp = send_request(file_data, token)
    logger.info(resp)
    deal_words(resp)


def record():
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording.")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    main()
