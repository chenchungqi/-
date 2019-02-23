import xlrd
from pyecharts import Pie
readbook = xlrd.open_workbook(r'weibo.xlsx')  #格式转换后的文件名
#print(readbook.sheet_names())
sheet = readbook.sheet_by_name('weiboifno')   #xlsx里的sheet1名字
nrows = sheet.nrows
ncols = sheet.ncols

sexlist = []
for i in range(0,180):         #手动更改excel中具体的条数
    lng = sheet.cell(i,0).value
    if(lng!='null'):
        sexlist.append(lng)
#print(len(sexlist))
boy=0
girl=0
for each in sexlist:
    if(each == '男'):
        boy = boy+1
    else:
        girl = girl+1
#print(boy,girl)

attr = ["男", "女"]
v1 = [boy,girl]
pie = Pie("中奖用户男女比例示意图")
pie.add("", attr, v1, is_label_show=True)
pie.render('中奖用户男女比例示意图.html')
print('文件生成成功，请在当前目录下查看文件。')