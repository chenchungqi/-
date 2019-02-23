# coding:utf8
from pyecharts import Map
import xlrd

readbook = xlrd.open_workbook(r'weibo.xlsx')    #excel  文件名
#print(readbook.sheet_names())
sheet = readbook.sheet_by_name('weiboifno')     #  sheet1 替换
nrows = sheet.nrows
ncols = sheet.ncols
citylist = []
for i in range(0,180):      #具体的数据条数
    lng = sheet.cell(i,1).value
    if(lng!='其他' and lng!='海外'):
        citylist.append(lng)
    # namelist.append(lng)
#print(citylist)
n = len(citylist)
#print(n)

citydic= {
    "河北": 0,"山东": 0,"辽宁": 0,"黑龙": 0,"吉林": 0,"甘肃": 0,
    "青海": 0,"河南": 0,"江苏": 0,"湖北": 0,"湖南": 0,"江西": 0,
    "浙江": 0,"广东": 0,"云南": 0,"福建": 0,"台湾": 0,"海南": 0,
    "山西": 0, "四川": 0, "陕西": 0, "贵州": 0, "安徽": 0, "重庆": 0,
    "北京": 0, "上海": 0, "天津": 0, "广西": 0, "内蒙": 0, "西藏": 0,
    "新疆": 0, "宁夏": 0, "澳门": 0, "香港": 0}
for each in citylist:
    citydic[each]=citydic[each]+1
#print(citydic)
#print(citydic['河北'])

value = [citydic['河北'],citydic['山东'],citydic['辽宁'],citydic['黑龙'],citydic['吉林'],
         citydic['甘肃'],citydic['青海'],citydic['河南'],citydic['江苏'],
         citydic['湖北'],citydic['湖南'],citydic['江西'],citydic['浙江'],citydic['广东'],
         citydic['云南'], citydic['福建'], citydic['台湾'], citydic['海南'], citydic['山西'],
         citydic['四川'], citydic['陕西'], citydic['贵州'], citydic['安徽'], citydic['重庆'],
         citydic['北京'], citydic['上海'], citydic['天津'], citydic['广西'], citydic['内蒙'],
         citydic['西藏'], citydic['新疆'], citydic['宁夏'], citydic['澳门'], citydic['香港'],
         ]
attr = [
    "河北", "山东", "辽宁", "黑龙江", "吉林","甘肃",
    "青海", "河南", "江苏", "湖北", "湖南", "江西",
    "浙江", "广东", "云南", "福建", "台湾", "海南",
    "山西", "四川", "陕西", "贵州", "安徽", "重庆",
    "北京", "上海", "天津", "广西", "内蒙古", "西藏",
    "新疆", "宁夏", "澳门", "香港"
    ]
map = Map("微博中奖用户省份分布图", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="china",
    is_visualmap=True,
    visual_text_color="#000",
    visual_range = [0,15]
)
map.render('博中奖用户省份分布图.html')
print('文件生成成功，请在当前目录下查看文件。')