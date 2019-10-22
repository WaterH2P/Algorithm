import requests
import random


urls = [
    'https://www.xicidaili.com/nn',
    'https://www.xicidaili.com/nn/2',
    'https://www.xicidaili.com/nn/3',
    'https://www.xicidaili.com/nn/4'
]
agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400'
]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'method': 'GET',
}
cookie = {
    '_free_proxy_session': 'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFiNzIxY2E3Njk0MDE0YWIzYTQ1OGMwYmUzNTJjNWIwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTRIZUlpdG03eVY0Z2RMRzdTcWtEazVOWjNCUk9lVnJpeWRnMHIrcll6VWc9BjsARg%3D%3D--d809eee3d02a7378ee648ef8365586c12a4d5274'
}

for url in urls:
    ips = []
    headers['User-Agent'] = random.choice(agents)
    req = requests.get(url, headers=headers, cookies=cookie)
    with open('./iphtml.txt', 'w', encoding='utf-8') as f:
        f.write(req.text)
    print('西刺代理 (%s) 网页爬取完毕' % url)
    with open('./iphtml.txt', 'r', encoding='utf-8') as f:
        string = f.readline().replace(' ', '')
        while string:
            if string.find('<td>') > -1 and string.find('.') > 3:
                ip = string[4:-6]
                string = f.readline().replace(' ', '')
                port = string[4:-6]
                while string and string.find('HTT') == -1:
                    string = f.readline().replace(' ', '')
                if string:
                    protocol = string[4:-6].lower()
                    ips.append(protocol+'://'+ip+':'+port)
            string = f.readline().replace(' ', '')
    with open('./ipTemp.txt', 'a', encoding='utf-8') as f:
        for ip in ips:
            f.write(ip+'\n')
    print('西刺代理 (%s) IP 提取完毕' % url)

ips, count = [], 0
print('西刺代理 IP 可用性验证开始 >------')
with open('./ipTemp.txt', 'r', encoding='utf-8') as f:
    proxyIP = f.readline().strip()
    urlCheck = 'https://www.baidu.com'
    while proxyIP:
        proxy = {}
        if proxyIP.find('https') > -1:
            proxy = {'https': proxyIP}
        else:
            proxy = {'http': proxyIP}
        strCount = ''
        if count < 10:
            strCount = '00' + str(count)
        elif count < 100:
            strCount = '0' + str(count)
        elif count < 1000:
            strCount = str(count)
        print(strCount, '  :  ', proxy, end='    : ')
        try:
            headers['User-Agent'] = random.choice(agents)
            req = requests.get(urlCheck, headers=headers, proxies=proxy, timeout=(5, 15))
            if req.text:
                ips.append('\''+proxyIP+'\',')
                print('OK')
        except requests.exceptions.ConnectionError as e:
            print("Error", e.args)
        except requests.exceptions.RequestException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            proxyIP = f.readline().strip()
    print('西刺代理 IP 可用性验证完毕 ------<')
with open('./ip.txt', 'a', encoding='utf-8') as f:
    for ip in ips:
        f.write(ip + '\n')