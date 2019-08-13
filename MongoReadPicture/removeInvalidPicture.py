# !_*_ coding:utf8 _*_
# @function 剔除无效图片
# @Author alexchung
# @Date 2019/7/31 16:13 PM

import os
from PIL import Image

class JudgeImageType(object):
    """
    判断图片类型
    JPG|JPEG 数据表头格式 ：\xff\xd8
    png 数据表头格式：
    """
    def __init__(self, image):
        """
        构造函数
        :param image: 图片数据
        """
        self.img_type = 'png'
        self.img_bytes = ''
        # with open(image, 'rb') as f:
        #     self.img_bytes = f.read(4)
        #     f.close()
        self.img_bytes = image[:4]
        self.image_type_flag = {
            'jpg': b'\xff\xd8\xff\xe0',
            # 'jpeg': b'\xff\xd8',
            # 'png': b'\xaeB`\x82'
            'png': b'\x89PNG'
        }

    def run(self):
        self.judgeType()

    def judgeType(self):
        """
        判断图片类型
        :return:
        """
        if self.img_bytes == self.image_type_flag['jpg']:
            self.img_type = 'jpg'
        elif self.img_bytes == self.image_type_flag['png']:
            self.img_type = 'png'
        else:
            self.img_type = None


class CheckImageValidity(object):
    """
    检测图片是否完整
    # 三种常见图片的最后两个字节标识图片类型
    JPG文件结尾标识：\xff\xd9
    JPEG文件结尾标识：\xff\xd9
    PNG文件结尾标识：\xaeB`\x82
    """

    def __init__(self, image, type):
        """
        默认构造函数
        :param image: 图片文件
        """

        # 保存图片最后两个字节内容
        self.img_bytes = image[-2:]
        # with open(image, 'rb') as f:
        #     # 移动游标读取最后个字节内容
        #     # offset:偏移量
        #     # whence；偏移位置 0：开头 1：当前位置 2：末尾
        #     f.seek(-2, 2)
        #     self.img_bytes = f.read()
        #     f.close()
        # 保存图片有效性标志位
        self.is_valid = True
        # jpg | png
        self.img_type = type
        # 保存图片格式
        self.img_end_format = {
        'jpg': b'\xff\xd9',
        # 'jpeg': b'\xff\xd9',
        # 'png': b'\xaeB`\x82'
        'png': b'`\x82'
        }

    def run(self):
        """
        更新属性
        :return:
        """
        self.checkIntegrity()

    def checkIntegrity(self):
        """
        检查 图片是否完整
        :return:
        """
        if self.img_type == 'jpg':
            self.is_valid = self.img_bytes.endswith(self.img_end_format['jpg'])

        if self.img_type == 'png':
            self.is_valid = self.img_bytes.endswith(self.img_end_format['png'])

class SaveValidImage(object):
    def __init__(self, source_path, destination_path):
        """
        构造函数
        :param source_path: 图片源路径
        :param destination_path: 图片目的路径
        """
        self.src_path = source_path
        self.des_path = destination_path
        self.img_type = 'jpg'
        self.is_valid = True
        self.image = ''

    def run(self):
        self.checkSaveValidImage()

    def judgeCheckIntegrity(self, image):
        """
        判断图片是否完整
        :param image: 图片数据
        :return:
        """
        judge_type = JudgeImageType(image)
        judge_type.run()
        self.img_type = judge_type.img_type

        if self.img_type == None:
            self.is_valid = False
        else:
            check_integrity = CheckImageValidity(image, self.img_type)
            check_integrity.run()
            self.is_valid = check_integrity.is_valid

    def checkSaveValidImage(self):
        """
        检查和保存完整图片
        :return:
        """
        image_index = 0
        for img_name in os.listdir(self.src_path):
            image_data = ''
            img_src_file = os.path.join(self.src_path, img_name)
            with open(img_src_file, 'rb') as f:
                image_data = f.read()
            self.judgeCheckIntegrity(image_data)
            if self.is_valid == False:
                continue
            elif self.is_valid == True:
                file_des_name = ''
                if self.img_type == 'jpg':
                    file_des_name = 'license image_' + str(image_index) + '.jpg'
                elif self.img_type == 'png':
                    file_des_name = 'license image_' + str(image_index) + '.png'

                file_des_file = os.path.join(self.des_path, file_des_name)
                if os.path.exists(self.des_path) == False:
                    os.mkdir(self.des_path)
                    with open(file_des_file, 'wb') as f:
                        f.write(image_data)
                else:
                    with open(file_des_file, 'wb') as f:

                        f.write(image_data)
                image_index += 1


if __name__ == "__main__":

    # PATH = os.path.join(os.getcwd(), 'license picture1')
    # # for file_name in os.listdir(PATH):
    # #     print(file_name)
    #
    # PATH0 = os.getcwd()
    # file_path = os.path.join(PATH, 'license picture_3.jpg')
    # out_path = os.path.join(PATH0, 'test.jpg')
    # data = ''
    # with open(file_path, 'rb') as f:
    #     # f.seek(-2, 2)
    #     # print(f.read().endswith(b'\xff\xd9'))
    #     data = f.read()
    #     print(data)
    #
    # with open(out_path, 'wb') as f:
    #     # f.seek(-2, 2)
    #     # print(f.read().endswith(b'\xff\xd9'))
    #     f.write(data)

        # print(f.read().endswith(b'`\x82'))
        # print(f.read(4))
        # b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
        # b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x00\x96'
    sPATH = os.path.join(os.getcwd(), 'license picture1')
    dPATH = os.path.join(os.getcwd(), 'license picture3')

    save_valid_image = SaveValidImage(sPATH, dPATH)
    save_valid_image.run()
    # judge = JudgeImageType(file_path)
    # judge.run()
    # print(judge.img_type)
    # check = CheckImageValidity(file_path, 'png')
    # check.run()
    # print(check.is_valid)

