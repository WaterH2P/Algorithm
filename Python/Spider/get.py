import requests
url = 'https://www.zhihu.com/search'
headers = {
    'authority': 'www.zhihu.com',
    'method': 'GET',
    'path': '/api/v4/search/top_search',
    'scheme': 'https',
    'referer': 'https://www.zhihu.com/search?type=content&q=lol',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
}
cookie = {
    '_xsrf': 'D23V8aCIppizJN1D2ZhylK04OjF4foja',
    '_zap': '2e71e8ce-59a5-48e3-9f1e-2d395039599f',
    'd_c0': 'ANCjx2TC2A-PTl1e8gojNlokXclpuq4BJQ0=|1565024511',
    'ISSW': '1',
    'tst': 'r',
    '__utma': '51854390.244724095.1565620490.1565620490.1565620490.1',
    '__utmz': '51854390.1565620490.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/h2p-7/collections',
    '__utmv': '51854390.100-1|2=registration_date=20160711=1^3=entry_date=20160711=1',
    'q_c1': '308058545efe475ea567481dbfcd9f6b|1568190531000|1565183890000',
    'tgw_l7_route': '80f350dcd7c650b07bd7b485fcab5bf7',
    'capsion_ticket': '2|1:0|10:1571656096|14:capsion_ticket|44:MjQ2MTJhNGU2YTAxNDcxM2FkN2NhMzAwMjRkNzllM2E=|29b3fe6a28ac5d30f1e6341445425da7ff9ffd3cdfef48944aab0c0656520a4e',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1571656095,1571656099,1571656106,1571656128',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1571656138'
}
data = {
    'type'  : 'content',
    'q'     : 'lol,'
}
req = requests.get(url, headers=headers, params=data, cookies=cookie)
print(req.text)
