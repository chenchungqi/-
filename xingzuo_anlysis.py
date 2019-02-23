# coding:utf8
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple
from pyecharts import Bar

def get_constellation(month, date):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
    if date < dates[month-1]:
    	return constellations[month-1]
    else:
    	return constellations[month]

readbook = xlrd.open_workbook(r'weibo.xlsx')    #excel  文件名
#print(readbook.sheet_names())
sheet = readbook.sheet_by_name('weiboifno')     #  sheet1 替换
nrows = sheet.nrows
ncols = sheet.ncols
namelist = []
for i in range(0,180):      #具体的数据条数
    lng = sheet.cell(i,2).value
    if(lng!='null'):
        namelist.append(lng)
    # namelist.append(lng)
# print(namelist)
n = len(namelist)
#print(n)
dic = {"摩羯": 0, "水瓶": 0, "双鱼": 0, "白羊": 0, "金牛": 0, "双子": 0, "巨蟹": 0, "狮子": 0, "处女": 0, "天秤": 0, "天蝎": 0, "射手": 0}
for i in range(0,n):
    # print(type(namelist[i]))
    sss = datetime(*xldate_as_tuple(namelist[i], 0))
    cell = sss.strftime('%Y/%d/%m %H:%M:%S')
    day = cell[5:7]
    month = cell[8:11]
    xingzuo =get_constellation(int(month), int(day))
    dic[xingzuo]=dic[xingzuo]+1
#print(dic)

x= ["摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤","天蝎","射手"]
y= [dic['摩羯'],dic['水瓶'],dic['双鱼'],dic['白羊'],dic['金牛'],dic['双子'],dic['巨蟹'],dic['狮子'],dic['处女'],dic['天秤'],dic['天蝎'],dic['射手'],]
bar = Bar("中奖用户星座分布图")
bar.add('数目',x,y)
bar.render('中奖用户星座分布图.html')
print('文件生成成功，请在当前目录下查看文件。')