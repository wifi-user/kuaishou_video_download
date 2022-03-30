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
    #输入快手url
    response =requests.get(url_kuaishou,headers=headers)
    #print(response.text)
    # with open('html.txt','w') as file:
    #     file.write(response.text)
    data = PQ(response.text)
    title = data('title').text()
    script = data('script').text()
    # print(data)
    url1 = script.find('"json":["')
    url2 = script.find('"]},')
    url = script[url1+9:url2].replace('\\u002F', '/')
    print(url)
    response_video = requests.get(url)
    with open(title+'.mp4','wb') as file:
        file.write(response_video.content)
        print('下载完成！')


if __name__ == "__main__":
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_95b00c543c666231994c956ec01cb75e',
        'Host': 'www.kuaishou.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    URL = input("输入快手链接:")
    url = get_video_url(URL)
    main(url)