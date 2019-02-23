import requests
import time
import json
from bs4 import BeautifulSoup
import requests
import re
import random

def lottery(page,pageid,lid):
    cookies = {
        'SINAGLOBAL': '2122001130231.9897.1498131937106',
        'UM_distinctid': '16744ae69f98d1-066795ed791476-4313362-100200-16744ae69fba43',
        '_td': '9feed471-5046-4602-93aa-381f26fdf018',
        'UOR': ',weibo.com,bbs.51testing.com',
        'un': '13695858176',
        'wvr': '6',
        'wb_timefeed_2430743534': '1',
        'Ugrow-G0': '7e0e6b57abe2c2f76f677abd9a9ed65d',
        'ALF': '1578278141',
        'SSOLoginState': '1546742147',
        'SCF': 'Ag8X5sd77UoArZkHQjYth8x16qGclOwbO_IW3V2jxSwMxqaW0cNa02vVaPtLdzYMOxQCGTmqGdt5PpK9vy7zDu8.',
        'SUB': '_2A25xNRnUDeRhGeRK6FIW9C3JyDiIHXVSQwwcrDV8PUNbmtBeLWOtkW9NU2inKxoWDvIny-93MMetJydv6yMSxKX_',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5mp82Cz6lndiH-TDwjVAwo5JpX5KzhUgL.FozXe05NShefe0B2dJLoIE.LxK-L1K-L128GC-iaqbH81C-41C-R1FH8SC-R1F-4BbH8SCHWSC-RS7tt',
        'SUHB': '09PM8Dt6ah8Ib4',
        'YF-V5-G0': '69afb7c26160eb8b724e8855d7b705c6',
        'YF-Page-G0': '70942dbd611eb265972add7bc1c85888',
        '_s_tentry': 'login.sina.com.cn',
        'Apache': '5190441265001.855.1546742157185',
        'ULV': '1546742157246:73:2:1:5190441265001.855.1546742157185:1546669919321',
        'wb_view_log_2430743534': '1366*7681',
    }
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Referer': 'http://event.weibo.com/yae/event/lottery/result?pageid=100140E1204222&id=3538105&f=weibo',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
    params = (
        ('pageid', pageid), #100140E1204222
        ('id', lid), #3538105
        ('page', page), #2
        ('prizeLevel', '1'),
        ('_t', '0'),
        ('__rnd',int(time.time()* 1000) ),  #1543237214927
    )
    response = requests.get('http://event.weibo.com/yae/aj/event/lottery/result', headers=headers, params=params, cookies=cookies)
    return response.text
def result(pageid,lid):
    userid = []
    jsonObj = json.loads(lottery('1',pageid,lid))
    html = jsonObj['data']['html']
    # print(html)
    bsObj = BeautifulSoup(html,'html.parser')
    #<span class='lottery_published_gray'>67</span>
    spans = bsObj.find_all('span',{'class':'lottery_published_gray'})
    count = spans[-1].text
    n = int(count)//3 + 1
    if n == 1:
        dt = bsObj.find_all('dt')
        for each in dt:
            userid.append(each.find('a')['href'].split('/')[3])
        #print(userid)
    else:
        for i in range(1, n+1 ):
            jsonObj = json.loads(lottery(i, pageid, lid))
            html = jsonObj['data']['html']
            bsObj = BeautifulSoup(html, 'html.parser')
            dt = bsObj.find_all('dt')
            for each in dt:
                userid.append(each.find('a')['href'].split('/')[3])
            #print(userid)
    return userid
def userInfo(uid):
    cookies = {
        'ALF': '1549334147',
        'SCF': 'Ag8X5sd77UoArZkHQjYth8x16qGclOwbO_IW3V2jxSwMwXqkVHnZQi0gS0Z9xIrgIVUyC-EOGuRlrIXjWajv-_U.',
        'SUB': '_2A25xNRxlDeRhGeRK6FIW9C3JyDiIHXVS2aQtrDV6PUJbktAKLXmmkW1NU2inKzZR6Qu7N1kDmm35M2DeYxbPLPvr;',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5mp82Cz6lndiH-TDwjVAwo5JpX5K-hUgL.FozXe05NShefe0B2dJLoIE.LxK-L1K-L128GC-iaqbH81C-41C-R1FH8SC-R1F-4BbH8SCHWSC-RS7tt;',
        'SUHB': '0vJ5m_fg7KIgVg',
        'SSOLoginState': '1543471384',
        '_T_WM': 'c7d295cbb0f5d9feb948ee18584b6e4f',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    response = requests.get('https://weibo.cn/'+ uid + '/info', headers=headers, cookies=cookies)
    h = response.text
    pattern = re.compile(r'性别:(.)')
    sex = pattern.search(h).group(1)
    #print(sex)
    pattern = re.compile(r'地区:(..)')
    area = pattern.search(h).group(1)
    #print(area)
    pattern = re.compile(r'生日:(\d\d\d\d.\d\d.\d\d)')
    try:
        birth = pattern.search(h).group(1)
    except AttributeError:
       # print('error')
        birth = 'null'
    s = '00-00'
    if (s in birth or '000' in birth):
        birth = 'null'
    #print(birth)

    with open('weiboifno.csv', 'a+', encoding='utf-8-sig') as f:
        f.write(sex + ',' + area + ',' + birth + '\n')
        f.close()
    return 1

usersex = []
count=0
for each in result('100140E1198435','3436763'):
    if(userInfo(each)):
        count=count+1
    time.sleep(0.5 + float(random.randint(1, 100)) / 20)
    print('已插入%d条信息'%count)
    if(count == 70):
        time.sleep(120)

#usersex = ['男', '女', '女', '男', '女', '男', '女', '女', '女', '男', '女', '女', '女', '女', '女', '女', '女', '男', '女', '男', '女', '男', '男', '女', '男', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '男', '女', '男', '男', '男', '女', '女', '男', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '女', '男', '女', '女', '男', '女', '女', '女', '女', '女', '女']

# male =usersex.count('男')
# female = usersex.count('女')
# print('男生/女生中奖比：')
# print(male/female)
# for each in usersex:
#     if(usersex[each] == '男')
#         male=male+1
#     else:
#         female=female+1


# response = requests.get('https://weibo.cn/2533560981/info', headers=headers, cookies=cookies)
# h = response.text
# pattern = re.compile(r'性别:(.)')
# sex = pattern.search(h).group(1)
# print(sex)
# pattern = re.compile(r'地区:(..)')
# area = pattern.search(h).group(1)
# print(area)
# pattern = re.compile(r'生日:(..........)')
# birth = pattern.search(h).group(1)
# s = '<br/>'
# if(s in birth):
#     birth = birth[0:5]
# print(birth)
# with open('weiboifno.csv', 'a+', encoding='utf-8-sig') as f:
#     f.write(sex + ',' + area + ',' + birth + '\n')
#     f.close()