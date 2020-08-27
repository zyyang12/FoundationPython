# -*- coding: utf-8 -*-
import os
import chardet
import configparser
#配置文件解析
class ParseConf:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            print("配置文件不存在")
            return -1
        data = open(filename, "rb").read()
        codeformat = chardet.detect(data).get("encoding")
        if (codeformat != "utf-8"):
            print("配置文件编码格式非utf-8格式，请修改编码格式")
            return -1
        self.config = configparser.ConfigParser()
        self.config.read(self.filename, encoding='utf-8')

    #以字符串的方式读取配置文件字符串内容
    def parseStr(self, item, member):
        member_str = ""
        sections = self.config.sections()
        if item in sections:
            options = self.config.options(item)
            print(options)
            if member in options:
                member_str = self.config.get(item, member)
            else:
                print("%s中不存在%s变量" % (item, member))
        else:
            print("配置文件中不存在%s" % item)
        return member_str

    #以列表的方式读取配置文件变量内容
    def parseList(self, item, member):
        member_list = []
        sections = self.config.sections()
        if item in sections:
            options = self.config.options(item)
            if member in options:
                member_str = self.config.get(item, member)
                member_str = member_str.strip(",")
                member_list.extend(member_str.split(','))
            else:
                print("%s中不存在%s变量" % (item, member))
        else:
            print("配置文件中不存在%s" % item)
        return member_list

    #以字典的形式读取配置文件变量item内容
    def parseDict(self, item):
        project_list = []
        sections = self.config.sections()
        if item in sections:
            options = self.config.options(item)
            option_projects = self.config.items(item)
            for option in options:
                project_list.append({option: self.config.get(item, option)})
        else:
            print("配置文件中不存在%s" % item)
        return project_list
