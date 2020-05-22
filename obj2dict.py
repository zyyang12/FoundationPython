#本模块实现python对象object递归转dict
def list2dict(datalist, keyname, key):
    keyname = keyname + "." + key
    for i in range(len(datalist)):
        keynamelist = keyname + "." + str(i)
        if isinstance(datalist[i], dict):
            obj2dict(datalist[i], keynamelist)
        elif isinstance(datalist[i], list):
            list2dict(datalist[i], keynamelist2, "")
        else:
            result_dict[keynamelist] = datalist[i]
#此功能模块的入口函数
#result_dict全局变量，存放转换后的词典结果
def obj2dict(data_obj, keyname):
    isinstance(data_obj, dict)
    for key in data_obj.keys():
        if isinstance(data_obj[key], dict):
            keynamedict = keyname + "." + key
            obj2dict(data_obj[key],keynamedict)
        elif isinstance(data_obj[key], list):
            list2dict(data_obj[key], keyname, key)
        else:
            keynamestr = keyname + "." + key
            result_dict[keynamestr] = data_obj[key]
