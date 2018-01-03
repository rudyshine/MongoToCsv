# -*- coding: utf-8 -*-
import csv
from pymongo import MongoClient
import codecs
import re

#建立连接
client = MongoClient('172.28.171.13',27017)
#client = MongoClient(‘10.20.66.106‘, 27017)
# db_name ='WeatherData' #数据库
# db = client[db_name]
# set=db.HistoryData2016

db_name ='CHEAA' #家电新闻数据库
db = client[db_name]
set=db.Cheaa_Info_Items
# #测试数据库是否连接（查全部数据）
# for i in set.find():
#     print(i)


# ###天气数据导出
# ###从mongoDB数据库中读表数据写到CSV文件里面
# def WriteCheaaCsv():
#     year='2016'
#     month=9
#     for i in range(month,13):
#         month=str(i) if i > 9 else "0" + str(i)
#         File=codecs.open(year+month+'.csv','w')  ##建立并打开文件
#         headList=['日期', '最高温度', '最低温度', '湿度','节日', '星期', '发布时间','城市ID']  ##表头
#         # headList=['ArtcleContent']  ##表头
#         writer=csv.writer(File)   ##写入文件
#         writer.writerow(headList)  ##写入 标题
#         for info in set.find({'日期':re.compile(year+month)}):##查到数据库里全部的数据
#             vList = []
#             for k in headList:
#                 vList.append(info[k])
#             writer.writerow(vList)
#
# WriteCheaaCsv()






# #从mongoDB数据库中读取Cheaa_Info_Data数据写到doc文件里面,一条记录一个文件
# def WriteCheaaCsv():
#     date = '2018-01-02'
#     for info in db.Cheaa_Info_Items.find({'ProgramStarttime':re.compile(date)}):  ##查到数据库里全部的数据
#     # for info in db.Cheaa_Info_Items.find():  ##查到数据库里全部的数据
#         vList = []
#         headList =['ArtcleContent'] ##表头
#         infoName=info['Title'].replace('/','-')
#         print(infoName)
#         File = codecs.open('%s.doc'%infoName,'w') ##建立并打开文件
#         writer = csv.writer(File)
#         writer.writerow(headList)
#         for k in headList:
#             text=''.join(info[k])
#             vList.append(text.strip())
#             writer.writerow(vList)
#
# WriteCheaaCsv()

#家电新闻导出
###从mongoDB数据库中读取Cheaa_Info_Data数据写到CSV文件里面
def WriteCheaaCsv():
    date='2018-01-02'
    File=codecs.open('Cheaa_Info_Data %s.csv'%date,'w')  ##建立并打开文件
    headList=['LinkUrl','ArtcleContent','Title','Time','InfoFrom', 'startUrl','ProgramStarttime']  ##表头
    writer=csv.writer(File)   ##写入文件
    writer.writerow(headList)  ##写入 标题
    for info in set.find({'ProgramStarttime':re.compile(date)}):##查到数据库里全部的数据
        vList = []
        for k in headList:
            text = ''.join(info[k])
            vList.append(text.strip())
        writer.writerow(vList)

WriteCheaaCsv()