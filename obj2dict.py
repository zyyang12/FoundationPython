def list2dict(datalist, keyname):
    for i in range(len(datalist)):
        keyname = keyname + "." + str(i)
        if isinstance(datalist[i], dict):
            obj2dict(datalist[i], keyname)
        elif isinstance(datalist[i], list):
            list2dict(datalist[i], keyname)
        else:
            result_dict[keyname] = datalist[i]
#递归实现object转dict
def obj2dict(data_obj, keyname):
    isinstance(data_obj, dict)
    for key in data_obj.keys():
        if isinstance(data_obj[key], dict):
            keyname = keyname + "." + key
            obj2dict(data_obj[key],keyname)
        elif isinstance(data_obj[key], list):
            list2dict(data_obj[key], keyname)
        else:
            keyname = keyname + "." + key
            result_dict[keyname] = data_obj[key]
