# !_*_ coding:utf8 _*_
# @function MongoDB 读取图片数据
# @Author alexchung
# @Date 2019/7/31 16:13 PM

import os
import base64
import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId

def base2img(baseStr, fileName):
    """
    解码base64文件为图片
    :param baseStr: bytes 格式文件
    :param fileName: 图片直接路径
    :return: None
    """
    with open(fileName, "wb+") as f:
        # f.write(base64.b64decode(baseStr))
        f.write(baseStr)

def downLoadMongoDBPiture(baseStr='', fold_name='', pic_index=0):
    """
    下载MongoDB图片
    :param baseStr: base64 编码文件
    :param fold_name: 文件夹名称
    :return: None
    """
    print('第{0}张图片开始下载'.format(pic_index))
    # 图片文件夹路径
    fold_path = os.getcwd() + r'\\' + fold_name
    # 图片名称
    file_name = 'license picture_' + str(pic_index) + '.jpg'

    # 图片直接路径
    file_path = fold_path + r'\\' + file_name
    # 判断文件夹是否存在
    if os.path.exists(fold_path) == False:
        os.mkdir(fold_path)
        base2img(baseStr, file_path)
    else:
        base2img(baseStr, file_path)


if __name__ == "__main__":
    # mongoDB 用户密码远程登陆格式
    # mongodb://[username:password@]hostname[:port][/database]
    mongo_client = MongoClient("mongodb://license:linewell_license123@{0}:27017/admin".format('192.168.81.24'))
    # mongo_client = MongoClient("mongodb://192.168.81.24:27017/admin")
    # mongo_client.adb.authenticate("license", "linewell_license123", mechanism='MONGODB-CR')
    LicenseFilesDBNew = mongo_client['LicenseFilesDBNew']
    # LicenseFilesDBNew = mongo_client['LicenseFilesDBNew']
    LicenseFilesDBNew = LicenseFilesDBNew['fs.chunks']
    document = LicenseFilesDBNew.find_one({"_id": ObjectId("5cf70fe495f8222fe8bb14b")})
    documents = LicenseFilesDBNew.find()

    print(document)
    # pic_index = 0
    # # 读取数据并保存为.jpg
    # for doc in documents:
    #     print(pic_index, doc['_id'])
    #     downLoadMongoDBPiture(doc['data'], 'license picture1', pic_index)
    #     pic_index += 1

