# -*- coding: utf-8 -*-
import csv
from pymongo import MongoClient
import codecs

#建立连接
client = MongoClient('172.28.161.186',27017)
#client = MongoClient(‘10.20.66.106‘, 27017)
db_name ='CHEAA' #数据库名
db = client[db_name]
# set=db.Cheaa_Info_Items

# #测试数据库是否连接（查全部数据）
# for i in set.find():
#     print(i)

#从mongoDB数据库中读取Cheaa_Info_Data数据写到CSV文件里面
def WriteCheaaCsv():
    File=codecs.open('Cheaa_Info_Data.csv','w')  ##建立并打开文件
    headList=['Time','Title','ArtcleContent','startUrl','InfoFrom','LinkUrl']  ##表头
    # headList=['ArtcleContent']  ##表头
    writer=csv.writer(File)   ##写入文件
    writer.writerow(headList)  ##写入 标题
    for info in db.Cheaa_Info_Items.find():##查到数据库里全部的数据
        vList = []
        for k in headList:
            vList.append(info[k])
        writer.writerow(vList)

WriteCheaaCsv()

# #从mongoDB数据库中读取Cheaa_Info_Data数据写到doc文件里面,一条记录一个文件
# def WriteCheaaCsv():
#     for info in db.Cheaa_Info_Items.find():  ##查到数据库里全部的数据
#         vList = []
#         headList = ['ArtcleContent'][0]  ##表头
#         infoName=info['Title']
#         print(infoName)
#         File = codecs.open('%s.doc'%infoName,'w')  ##建立并打开文件
#         writer = csv.writer(File)
#         writer.writerow(headList)
#         for k in headList:
#             vList.append(info[k])
#             writer.writerow(vList)
#
# WriteCheaaCsv()