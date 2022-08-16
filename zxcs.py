#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   zxcs.py
@Time    :   2022/07/18 10:37:01
@Author  :   Yao Zipeng 
@Version :   python 3.8
知轩藏书 小说下载
'''
from ast import keyword
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


def file_download(url, filename):
    try:
        fname = re.search('《(.*?)》', filename).group(1)
    except:
        fname = filename.split('作者')[0]
    print('开始下载：' + filename)
    response = requests.get(url, verify=False)
    with open(f'./{fname}.zip', 'wb') as f:
        f.write(response.content)
    print('下载完成')


def get_dwonload_url(id):
    data = {
        'id': id,
    }
    host_url = 'http://207.246.114.172'
    response = requests.post(
        'https://www.zxcs.info/download1.php', data=data, verify=False).text
    if response != '':
        download_url = host_url + response
        return download_url
    else:
        print('没有找到下载地址')


def search(name):
    response = requests.get(
        f'https://www.zxcs.info/index.php?keyword={name}', headers=headers,  verify=False)

    html = response.text.replace('\n', '').replace('\r', '').replace(' ', '')
    plist = re.findall(
        '<dlid="plist"><dt><ahref="https://www.zxcs.info/post/(.*?)"target="_blank">(.*?)</a></dt>', html)
    for i in plist:
        id = i[0]
        title = i[1]
        return id, title


if __name__ == '__main__':
    keyword = input('请输入小说名称：')
    id, name = search(keyword)
    down_url = get_dwonload_url(id)
    file_download(down_url, name)
