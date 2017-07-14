import requests
import json
from pprint import pprint
import numpy as np


def get_response():
    headers = {
    'Host':	'api.yunniao.cn',
    'version':	'300050000',
    'x-cli-ver':	'3.5.0',
    'timestamp':	'1490194274622',
    'channel':	'AppStore',
    'Accept':	'*/*',
    'x-cli-ch':	'AppStore',
    'Proxy-Connection':	'keep-alive',
    'Accept-Language':	'en-CN;q=1, zh-Hans-CN;q=0.9',
    'Accept-Encoding' : 'gzip, deflate',
    'x-cli-model':	'iPhone 6s',
    'x-cli-os':	'iOS10.1.1',
    'sessionid': '13122617335_Ag2xIegprD',
    'User-Agent' : 'YNDriver/3.5.0 (iPhone; iOS 10.1.1; Scale/2.00)',
    'Connection' : 'keep-alive',
    'x-cli-imei' : '1A09A2B6-4D5B-4AF2-BC93-B76DAD8B8B3E'}

    url = 'http://api.yunniao.cn/api/v2/trans_task/list?page=1&perpage=5&recomm_key=3692B31DBBE3932CF988CAB666FDF5AB&sign=588d8cac765c0515d975262da3ee4b83'
    response = requests.get(url=url, headers=headers)   #返回json格式的字符串
    result = json.loads(response.text)

    return result['info']['list']


def get_details(task_id):
    headers = {
            'Host': 'api3.yunniao.cn',
            'version':	'300050000',
            'x-cli-ver': '3.5.0',
            'timestamp': '1490255088114',
            'channel':	'AppStore',
            'Accept':	'*/*',
            'x-cli-ch': 'AppStore',
            'Proxy-Connection': 'keep-alive',
            'Accept-Language':	'en-CN;q=1, zh-Hans-CN;q=0.9',
            'Accept-Encoding':	'gzip, deflate',
            'x-cli-model':	'iPhone 6s',
            'x-cli-os': 'iOS10.1.1',
            'sessionid' : '13122617335_Ag2xIegprD',
            'User-Agent': 'YNDriver/3.5.0 (iPhone; iOS 10.1.1; Scale/2.00)',
            'Connection': 'keep-alive',
            'x-cli-imei': '1A09A2B6-4D5B-4AF2-BC93-B76DAD8B8B3E'}
    url = 'http://api3.yunniao.cn/api/v2/trans_task/detail_v2'

    params = {
            'coord_sys': '2',
            'recomm_key': '3692B31DBBE3932CF988CAB666FDF5AB',
            #'sign': 'c2ce1baceeb32d25d86e5de32d486b4f',
            'task_id': task_id}

    response = requests.get(url=url, params=params, headers=headers)

    result = json.loads(response.text)
    return result['info']['detail_infomation']
    #pprint(result['info']['detail_infomation'])


def get_quote(details):
    try: quote = details[0]['content'][4]['content']
    except: quote = None
    return quote


def get_vehicle(details):
    return details[2]


#if __name__ == '__main__':
     #print(get_quote(get_details(1492464)))