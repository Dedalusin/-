import requests
from bs4 import BeautifulSoup
import sys
import importlib
import matplotlib.pyplot as plt
importlib.reload(sys)

global headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
server = 'https://search.bilibili.com/all?keyword=%E8%82%A1%E7%A5%A8&from_source=nav_search&spm_id_from=333.155.b_696e7465726e6174696f6e616c486561646572.10'
server_suffix = '&page='

#画图
def paint(time, count):
    plt.plot(time,count)
    plt.tick_params(labelsize=5)
    plt.show()

def main():
    time_count = {}
    sorted_time_count = []
    try:
        for i in range(1,10):
            req = requests.get(url=server+server_suffix+str(i),headers=headers)
            html = req.content
            html_doc = str(html,'utf-8')
            bf = BeautifulSoup(html_doc,"html.parser")
            times_span = bf.findAll('span', title='上传时间')
            for span in times_span:
                time = span.text.replace('-','')
                if time in time_count:
                    time_count[time]+=1
                else:
                    time_count[time]=1
        sorted_time = sorted(time_count.keys())
        for key in sorted_time:
            sorted_time_count.append(time_count[key])
        paint(sorted_time, sorted_time_count)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()