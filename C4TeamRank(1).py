
# coding: utf-8

# In[49]:

from prettytable import PrettyTable
import urllib.request
import sys
import json
import time
from imp import reload
from bs4 import BeautifulSoup
import  matplotlib.pyplot as plt
import re
fontSize=6
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
from matplotlib.font_manager import FontProperties
import numpy as np
reload(sys)
#sys.setdefaultencoding('utf-8')
import requests

def alignment(str1, space, align = 'left'):
    length = len(str1.encode("UTF-8"))
    space = space - length if space >=length else 0
    if align == 'left':
        str1 = str1 + ' ' * space
    elif align == 'right':
        str1 = ' '* space +str1
    elif align == 'center':
        str1 = ' ' * (space //2) +str1 + ' '* (space - space // 2)
    return str1
tb = PrettyTable(["\t\t\t名次/队伍\t\t\t", "\t\t学校\t\t","\t成绩\t"])
tb.align["名次/队伍"] = "l"
tbHN = PrettyTable(["\t\t\t名次/队伍\t\t\t", "\t\t学校\t\t","\t成绩\t"])
tbHN.align["名次/队伍"] = "l"
dictSchool = {}
lstTeam = []
lstHNShoolUrl = 'http://www.gx211.com/news/20170619/n14978548564767.html'
data = urllib.request.urlopen(lstHNShoolUrl).read()
soup = BeautifulSoup(data,"lxml")
table = soup.find("table")
lstHNSchool = []
for row in table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells) >=2:
        school = cells[1].find(text=True)
    lstHNSchool.append(school)
    #setHNSchool.add(school)
#print(lstHNSchool)

urls = 'http://gplt.patest.cn/api/cached/board?timestamp='+str(time.time())
#print(urls)
content = requests.get(urls).content
#contentSchool = request.get(urlschool).content
#print(content)
inp_dict = json.loads(content) # 根据字符串书写格式，将字符串自动转换成 字典类型
#school_dict = json.loads(contentSchool)

teamInfo = inp_dict['data']['rawData']['score']['teams']
schoolInfo = inp_dict['data']['rawData']['score']['schools']
#print(schoolInfo)
for k,v in schoolInfo.items():
   # print(schoolInfo[i][1])
    _id = v['_id']
    name = v['name']
    dictSchool[_id]=name
#print(dictSchool)
#print(lstTeam)
#print(teamInfo)
for team in list(teamInfo):
    #print(team)
    #print()
    if (teamInfo[team]['type']==0 or teamInfo[team]['type']==2):
        del teamInfo[team]
sorted_dict_asc = sorted(teamInfo.items(),key=lambda item:item[1]['tScore'],reverse=True)
#print(sorted_dict_asc)
#全国队伍总排名
sorted_dict_asc_all = sorted_dict_asc
cnt = 1

f = open(r'C:\Users\ysyma\Desktop\c4\out.txt','w',encoding='utf-8')
for teamAll in sorted_dict_asc_all:
   # print(teamAll)
    name = teamAll[1]['name']
    sid = teamAll[1]['_sid']
    schoolName = dictSchool.get(sid)
    score = teamAll[1]['tScore']
    '''
    if schoolName == '华北水利水电大学':
        #print("\033[1;31;40m全国总榜第"+str(cnt)+"名：",name,"\t所属学校：",schoolName,"\t总分：",score,"\033[0m")
        strName = "\033[1;31;43m全国总榜第"+str(cnt)+"名："+name+"\033[0m"
       # alignment(",20,'left')
        strSchool = "\033[1;31;43m所属学校："+schoolName+"\033[0m"
        strScore = "\033[1;31;43m总分："+str(score)+"\033[0m"  
        tb.add_row([strName,strSchool,strScore])
      #  print(strName+'\t'+strSchool+'\t'+strScore)
    # print(,alignment("\033[1;31;40m所属学校：",schoolName,+"\033[0m",20,'left'),alignment("\033[1;31;40m总分：",score,+"\033[0m",20,'left'))
    else:
        #print("全国总榜第"+str(cnt)+"名：",name,"\t所属学校：",schoolName,"\t总分：",score)
        strName = "全国总榜第"+str(cnt)+"名："+name
        strSchool = "所属学校："+schoolName
        strScore = "总分："+str(score)
        #print(alignment(strName,60),alignment(strSchool,30),alignment(strScore,20,'right'))
        tb.add_row([strName,strSchool,strScore])
    '''
    # print("全国总榜第"+str(cnt)+"名：",name,"\t所属学校：",schoolName,"\t总分：",score)
    strName = "全国总榜第" + str(cnt) + "名：" + name
    strSchool = "所属学校：" + schoolName
    strScore = "总分：" + str(score)

    if schoolName in lstHNSchool:
        tbHN.add_row([strName, strSchool, strScore])
    # print(alignment(strName,60),alignment(strSchool,30),alignment(strScore,20,'right'))
    tb.add_row([strName, strSchool, strScore])
    cnt = cnt +1
#    print(tb,file=f)

#print(tb)
print(tb,file=f)
print(tbHN)

#print(tb,file=f)
f.close()

print("<------------------------------------------------------------------------------------------------------------------------------>")
