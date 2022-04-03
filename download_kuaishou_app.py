import requests
from pyquery import PyQuery as PQ
import time
import threading
def download(title,url):
    response_video = requests.get(url)
    with open(title+'.mp4','wb') as file:
        file.write(response_video.content)
        print(title,'下载完成！')

def main(url_kuaishou):
    #输入快手url------------------->> https://v.kuaishou.com/mvFFl6
    #----------------------------->> https://v.kuaishouapp.com/s/TPDdI9GB
    """>>>>>>>>>>>>>>>>>>>>>>以下用于获取urlHost用于headers<<<<<<<<<<<<<<<<<<<<<"""
    url_head = url_kuaishou.find('://')
    url_tail = url_kuaishou.find('.com')
    url_host = url_kuaishou[url_head+3:url_tail+4]
    print(url_host)
    headers['Host'] = url_host
    """>>>>>>>>>>>>>>>>>>>>>>以上用于获取urlHost用于headers<<<<<<<<<<<<<<<<<<<<<"""
    response =requests.get(url_kuaishou,headers=headers)
    #print(response.text)
    # with open('html.txt','w') as file:
    #     file.write(response.text)
    data = PQ(response.text)
    title = data('title').text()
    script = data('script').text()
    print(title)
    url1 = script.find('"json":["')
    url2 = script.find('"]},')
    url = script[url1+9:url2].replace('\\u002F', '/')
    print(url)
    response_video = requests.get(url)
    with open(title+'.mp4','wb') as file:
        file.write(response_video.content)
        print('下载完成！')

def get_video_url(get_url):
    if 'www.kuaishou.com/short-video' in get_url :
        #内含“ kuaishou.com/short-video ”将无跳转
        return get_url
    while True:
        # print(get_url)
        """>>>>>>>>>>>>>>>>>>>>>>以下用于获取urlHost用于headers<<<<<<<<<<<<<<<<<<<<<"""
        url_head = get_url.find('://')
        url_tail = get_url.find('.com')
        url_host = get_url[url_head+3:url_tail+4]
        print(url_host)
        headers['Host'] = url_host
        """>>>>>>>>>>>>>>>>>>>>>>以上用于获取urlHost用于headers<<<<<<<<<<<<<<<<<<<<<"""
        response = requests.get(get_url,headers=headers,allow_redirects=False)
        get_url = response.headers['Location']
        print(get_url)
        #response = requests.get(get_url,allow_redirects=False)
        #print(get_url)
        if 'http' not in get_url:
            get_url = 'http:'+get_url 
        elif 'www.kuaishou.com/short-video' in get_url:
            print('\n\nget_kuaishou_url: '+get_url,'\n')
            return get_url
           

if __name__ == "__main__":
    headers={
        #https://v.kuaishou.com/mvFFl6
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'clientid=3; did=web_95b00c543c666231994c956ec01cb75e; didv=1648965523000; userId=1760196216',
        'Host': 'v.kuaishou.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
    while True:
        try:
            URL = input("输入快手链接:")
            url = get_video_url(URL)
            main(url)
        except:
            print('error')
            continue
