import scrapy
import random


AGENTS = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
]

PROXIES = [
    'http://183.164.238.236:9999',
    'https://117.30.113.193:9999',
    'https://117.30.112.118:9999',
    'http://121.206.142.72:9999',
    'http://117.28.97.17:9999',
    'http://180.119.141.240:9999',
    'http://183.164.238.191:9999',
    'http://59.57.149.175:9999',
    'https://27.152.91.172:9999',
    'http://117.57.90.136:9999',
    'http://117.69.201.146:9999',
    'http://114.239.150.62:9999',
    'http://114.239.2.10:9999',
    'http://114.239.146.127:808',
    'http://113.120.36.75:9999',
    'http://113.194.31.16:9999',
    'http://27.152.90.171:9999',
    'http://180.122.38.21:9999',
    'http://117.57.90.167:9999',
    'http://182.35.85.192:9999',
    'http://59.57.149.134:9999',
    'http://27.152.8.246:9999',
    'http://114.239.110.51:9999',
    'http://58.253.155.76:9999',
    'http://114.239.252.232:9999',
    'http://117.95.232.200:9999',
    'http://59.57.38.215:9999',
    'http://118.78.196.142:8118',
    'http://49.89.223.35:9999',
    'http://122.4.51.161:9999',
    'http://182.35.80.36:9999',
    'http://171.35.161.201:9999',
    'http://117.94.181.84:9999',
    'http://117.94.180.253:9999',
    'http://117.94.183.121:9999',
    'http://117.94.181.221:9999',
    'http://117.69.201.57:9999',
    'http://114.239.199.110:9999',
    'http://117.26.40.248:9999',
    'http://117.26.46.183:9999',
    'https://113.121.75.139:808',
    'http://1.193.245.56:9999',
    'http://123.55.4.221:9999',
    'http://60.217.64.237:31923',
    'http://60.216.101.46:59351',
    'http://1.197.16.157:9999',
    'http://171.11.33.212:9999',
    'http://1.197.16.195:9999',
    'http://123.163.97.12:9999',
    'http://115.219.106.150:3128',
    'http://114.239.0.254:808',
    'http://117.57.90.245:48152',
    'http://122.193.61.129:8118',
    'http://175.150.102.162:1133',
    'http://117.95.162.188:9999',
    'http://122.5.176.229:9999',
    'http://113.120.60.250:9999',
    'http://117.69.200.176:9999',
    'http://171.13.103.14:9999',
    'http://117.57.91.148:9999',
    'https://59.57.148.16:9999',
    'http://117.57.91.8:9999',
    'http://171.12.113.166:9999',
    'http://120.83.110.172:9999',
    'http://1.198.72.27:9999',
    'http://121.226.214.25:9999',
    'http://117.95.232.56:9999',
    'https://117.69.201.13:9999',
    'http://125.78.16.55:9999',
    'http://59.57.148.17:9999',
    'http://1.198.73.67:9999',
    'http://27.152.8.152:9999',
    'http://118.212.107.104:9999',
    'http://117.69.201.180:9999',
    'http://117.69.201.198:9999',
    'http://123.163.96.160:9999',
    'http://27.152.91.4:9999',
    'http://106.110.195.47:23177',
    'http://114.239.198.157:9999',
    'http://117.69.201.24:9999',
    'http://183.164.239.254:9999',
    'http://182.35.87.254:9999',
    'http://182.35.80.194:9999',
    'http://113.120.37.82:9999',
    'http://49.89.143.31:9999',
    'http://60.13.42.135:9999',
    'http://113.120.62.46:9999',
    'http://117.69.200.10:9999',
    'http://1.199.30.37:9999',
    'http://183.166.139.168:9999',
    'http://183.164.239.116:9999',
    'http://117.30.113.83:9999',
    'http://117.69.201.171:9999',
    'https://27.152.91.241:9999',
    'http://117.30.112.132:9999',
    'http://114.239.198.91:9999',
    'http://117.69.200.239:9999',
    'http://27.152.90.74:9999',
    'http://114.239.248.22:9999',
    'http://120.83.102.107:9999',
    'http://182.35.81.140:9999',
    'http://27.152.91.112:9999',
    'http://117.57.90.234:34320',
    'http://117.30.112.193:9999',
    'https://106.110.212.229:9999',
    'http://113.120.35.77:9999',
    'http://117.57.91.26:9999',
    'http://114.239.145.12:808',
    'http://114.239.253.3:9999',
    'http://117.28.96.105:9999',
    'http://114.239.149.198:808',
    'http://183.166.125.253:9999',
    'http://114.239.253.65:9999',
    'http://117.57.91.69:9999',
    'http://122.4.48.170:9999',
    'http://182.34.33.49:9999',
    'http://114.239.0.124:808',
    'http://117.30.113.105:9999',
    'http://59.57.149.115:9999',
    'http://114.239.248.205:9999',
    'https://59.57.149.34:9999',
    'http://113.120.39.60:9999',
    'http://121.226.188.68:9999',
    'http://60.13.42.68:9999',
    'http://171.35.167.101:9999',
    'http://27.152.91.83:9999',
    'http://182.35.82.232:9999',
    'http://117.57.91.236:9999',
    'http://175.44.109.148:9999',
    'http://117.57.90.47:9999',
    'http://117.69.201.70:9999',
    'http://114.239.254.211:9999',
    'http://114.239.1.80:808',
    'http://183.164.238.40:9999',
    'http://114.239.249.247:808',
    'http://59.57.149.2:9999',
    'https://27.152.91.71:9999',
    'http://183.164.238.18:9999',
    'http://183.166.118.153:9999',
    'http://59.57.38.126:9999',
    'http://49.70.17.115:9999',
    'http://121.205.14.74:9999',
    'http://182.34.32.113:9999',
    'http://117.95.232.162:9999',
    'http://183.164.238.117:9999',
    'http://27.152.90.29:9999',
    'http://114.239.42.33:9999',
    'http://175.42.123.48:9999',
    'http://171.35.223.37:9999',
    'http://123.163.97.171:9999',
    'http://113.121.23.154:9999',
    'http://171.35.161.55:9999',
    'http://117.57.91.123:47488',
    'https://115.46.103.68:8123',
    'https://119.23.45.52:8080',
    'http://111.75.223.9:35918',
    'http://110.243.25.113:9999',
    'http://1.193.245.3:9999',
    'http://171.13.200.151:9999',
    'http://182.35.86.74:9999',
    'http://121.230.252.119:9999',
    'http://113.195.153.156:9999',
    'http://59.57.149.97:9999',
    'http://125.115.182.186:3128',
    'http://175.10.24.153:3128',
    'http://27.42.168.46:48919',
    'http://27.152.91.164:9999',
    'http://59.57.148.221:9999',
    'http://175.148.73.65:1133',
    'http://171.13.203.246:9999',
    'http://117.69.200.144:9999',
    'http://36.248.132.221:9999',
    'http://182.35.84.233:9999',
    'http://117.57.90.181:9999',
    'http://121.233.251.114:9999',
    'http://117.30.112.110:9999',
    'http://120.83.96.235:9999',
    'http://117.69.25.2:9999',
    'http://171.35.160.211:9999',
    'http://59.57.149.173:9999',
    'http://59.57.38.130:9999',
    'http://175.155.140.119:1133',
    'http://117.28.96.149:9999',
    'http://123.54.47.224:9999',
    'http://117.28.97.189:9999',
    'http://114.239.147.181:808',
    'http://27.152.90.250:9999',
    'http://117.95.214.149:9999',
    'http://117.57.91.116:9999',
    'http://183.164.239.9:9999',
    'http://183.164.239.69:9999',
    'http://183.166.86.253:9999',
    'http://49.70.94.183:9999',
    'http://117.95.175.222:9999',
    'http://182.35.84.103:9999',
    'http://106.110.212.236:9999',
    'http://27.152.91.27:9999',
    'http://61.145.49.220:9999',
    'http://49.71.133.42:9999',
    'http://110.243.1.70:9999',
    'http://117.30.113.217:9999',
    'http://183.164.239.222:9999',
    'http://117.57.90.64:9999',
    'http://222.190.222.19:9999',
    'http://27.152.91.75:9999',
    'http://110.243.5.29:9999',
    'http://117.95.192.171:9999',
    'http://183.166.6.90:9999',
    'http://183.164.239.92:35873',
    'http://113.194.28.202:9999',
    'http://117.69.200.96:9999',
    'http://36.25.40.80:9999',
    'http://182.34.35.12:9999',
    'http://117.57.91.141:9999',
    'http://114.239.42.10:9999',
    'https://59.57.149.239:9999',
    'http://114.230.117.38:9999',
    'http://59.57.149.47:9999',
    'http://114.239.249.21:9999',
    'http://27.152.91.65:9999',
    'http://59.57.149.59:9999',
    'http://59.57.38.13:9999',
    'http://183.166.96.39:9999',
    'http://59.57.148.15:9999',
    'http://113.120.38.185:9999',
    'http://117.57.91.119:9999',
    'http://121.205.85.174:9999',
    'http://114.239.251.177:9999',
    'http://182.35.84.193:9999',
    'http://182.34.36.7:9999',
    'http://117.30.112.185:9999',
    'http://114.239.172.115:9999',
    'http://222.89.32.139:9999',
    'http://117.69.201.120:9999',
    'http://49.70.64.33:9999',
    'http://183.164.239.97:9999',
    'http://183.164.238.64:9999',
    'http://123.163.96.120:9999',
    'http://182.35.83.46:9999',
    'http://59.57.149.76:9999',
    'http://113.120.36.61:9999',

]

HEADERS = {
    'method': 'GET',
    'scheme': 'https',
    'Referer': 'https://www.zhihu.com/',
    'Origin': 'https://www.zhihu.com/',
    'cache-control': 'no-cache',
    'Connection': 'close',
}

COOKIE = {
    '_xsrf': 'D23V8aCIppizJN1D2ZhylK04OjF4foja',
    '_zap': '2e71e8ce-59a5-48e3-9f1e-2d395039599f',
    'd_c0': 'ANCjx2TC2A-PTl1e8gojNlokXclpuq4BJQ0=|1565024511',
    'ISSW': '1',
    'tst': 'r',
    '__utma': '51854390.244724095.1565620490.1565620490.1565620490.1',
    '__utmz': '51854390.1565620490.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral',
    '__utmv': '51854390.100-1|2=registration_date=20160711=1^3=entry_date=20160711=1',
    'q_c1': '308058545efe475ea567481dbfcd9f6b|1568190531000|1565183890000',
    'tgw_l7_route': '80f350dcd7c650b07bd7b485fcab5bf7',
    'capsion_ticket': '2|1:0|10:1571656096|14:capsion_ticket|44:MjQ2MTJhNGU2YTAxNDcxM2FkN2NhMzAwMjRkNzllM2E=|29b3fe6a28ac5d30f1e6341445425da7ff9ffd3cdfef48944aab0c0656520a4e',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1571656095,1571656099,1571656106,1571656128',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1571656138'
}


class LOLSpider(scrapy.Spider):
    name = 'zhLOL'

    # def start_requests(self):
    #     urls = [
    #         'https://www.baidu.com'
    #     ]
    #     for url in urls:
    #         agent = random.choice(AGENTS)
    #         HEADERS['User-Agent'] = agent
    #         proxy = random.choice(PROXIES)
    #         yield scrapy.Request(url=url, headers=HEADERS, meta={'proxy': proxy}, callback=self.parse)
    #
    # def parse(self, response):
    #     for ele in response.css('div#u_sp a').getall():
    #         content = ele.css('::text').get()
    #         yield {
    #             'content': content
    #         }

    def start_requests(self):
        urls = [
            'https://www.zhihu.com/search?type=content&q=lol'
        ]
        for url in urls:
            agent = random.choice(AGENTS)
            HEADERS['User-Agent'] = agent
            proxy = random.choice(PROXIES)
            yield scrapy.Request(url=url, headers=HEADERS, callback=self.parse)

    def parse(self, response):
        for card in response.css('div.SearchResult-Card'):
            url = card.css('h2.ContentItem-title a::attr(href)').get()
            url = response.urljoin(url)
            title = str(card.css('h2.ContentItem-title span.Highlight').get())
            title = title.replace('<span class="Highlight">', '')
            title = title.replace('<em>', '')
            title = title.replace('</em>', '')
            title = title.replace('</span>', '')
            yield {
                'url': url,
                'title': title
            }