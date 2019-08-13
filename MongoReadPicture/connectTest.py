# !_*_ coding:utf8 _*_
# !_*_ env:python3 _*_
# @function MongoDB 连接测试
# @Author alexchung
# @Date 2019/7/31 16:12 PM

import os
import base64
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId



if __name__ == "__main__":
    # mongoDB 用户密码远程登陆格式
    # mongodb://[username:password@]hostname[:port][/database]
    mongo_client = MongoClient("mongodb://license:linewell_license123@{0}:27017/admin".format('192.168.81.24'))
    # mongo_client = MongoClient("mongodb://192.168.81.24:27017/admin")
    # mongo_client.adb.authenticate("license", "linewell_license123", mechanism='MONGODB-CR')
    LicenseFilesDBNew = mongo_client['LicenseFilesDB']
    # LicenseFilesDBNew = mongo_client['LicenseFilesDBNew']
    LicenseFilesDBNew = LicenseFilesDBNew['fs.chunks']
    document = LicenseFilesDBNew.find_one({"_id": ObjectId("5c6ceb78bc468a72b12387db")})
    documents = LicenseFilesDBNew.find()

    print(document)
    print(LicenseFilesDBNew.count())

