import requests
from bs4 import BeautifulSoup
import sys
import importlib
importlib.reload(sys)

global headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
server = 'https://www.biqugeu.net/135_135098/'
server_pre = 'https://www.biqugeu.net'
#存储地址
global save_path
save_path = 'D:/code/pythondata/'

#获取章节内容
def get_content(charpter):
    req = requests.get(url=charpter, headers=headers)
    html = req.content
    html_doc = str(html, 'utf-8')
    bf = BeautifulSoup(html_doc, 'html.parser')
    texts = bf.find_all('div', id='content')
    #替换\xa0不间断空白符
    content = texts[0].text.replace('\xa0'*4, '\n')
    return content

#存储
def save_text(path, content):
    with open(path, 'a', encoding='utf8') as f:
        f.write(content)

def main():
    try:
        req = requests.get(url=server, headers=headers)
        html = req.content
        html_doc = str(html, 'utf-8')
        bs = BeautifulSoup(html_doc, 'html.parser')
        links = bs.find('div', id='list').find_all('a')
        print(len(links))
        for link in links:
            href = server_pre+link.get('href')
            path = save_path+link.string+'.text'
            save_text(path, get_content(href))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()