# -*- coding: utf-8 -*-
import csv
from pymongo import MongoClient
import codecs

#建立连接
client = MongoClient('172.28.161.186',27017)
#client = MongoClient(‘10.20.66.106‘, 27017)
db_name ='Cheaa_Info_Data' #数据库名
db = client[db_name]
# set=db.Cheaa_Info_Items

##测试数据库是否连接（查全部数据）
# for i in set.find():
#     print(i)

#从mongoDB数据库中读取Cheaa_Info_Data数据写到CSV文件里面
def WriteCheaaCsv():
    File=codecs.open('Cheaa_Info_Data.csv','w')  ##建立并打开文件
    headList=['Time','Title','ArtcleContent','startUrl','InfoFrom','LinkUrl']  ##表头
    writer=csv.writer(File)   ##写入文件
    writer.writerow(headList)  ##写入 标题
    # headList[0] ='_id'
    for info in db.Cheaa_Info_Items.find(): ##查到数据库里全部的数据
        vList = []
        for k in headList:
            vList.append(info[k])
            writer.writerow(vList)

WriteCheaaCsv()

