# -*- coding: utf-8 -*-
import os
import shutil

class Directory():

    #获取当前文件夹及其子文件夹中的所有文件
    def getFiles(path):
        file_list = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file = os.path.join(root, file)
                file_list.append(file)
        return file_list

    #获取当前文件夹的所有子文件夹（含递归）
    def getDirs(path):
        dir_list = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                dir = os.path.join(root, dir)
                dir_list.append(dir)
        return dir_list

    #删除当前文件夹内的所有文件（含递归）
    def delFiles(path):
        for file in Directory.getFiles(path):
            os.remove(file)

    #删除当前文件夹
    def delDirs(path):
        shutil.rmtree(path)
