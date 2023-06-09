import requests
from lxml import etree

url = 'https://www.runoob.com/python/python-exercise-example%s.html'


def get_element(url):
    headers = {
        'cookie': 'Hm_lpvt_3eec0b7da6548cf07db3bc477ea905ee',
        'referer': 'https://www.runoob.com/python/python-100-examples.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return etree.HTML(response.text)


def write_py(i, text):
    with open('练习实例%s.py' % i, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    for i in range(1, 101):
        html = get_element(url % i)
        content = '题目：' + html.xpath('//div[@id="content"]/p[2]/text()')[0] + '\n'
        fenxi = html.xpath('//div[@id="content"]/p[position()>=2]/text()')[0]
        daima = ''.join(html.xpath('//div[@class="hl-main"]/span/text()')) + '\n'
        haha = '"""\n' + content + fenxi + daima + '\n"""'
        write_py(i, haha)
        print(fenxi)

if __name__ == '__main__':
    main()

