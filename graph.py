# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

#画图select:1标识直方图，2表示饼图
def graph(dict, select, my_title, outfile):
    fig = plt.figure()
    dict_values = list(dict.values())
    dict_keys = list(dict.keys())
    x = range(len(dict_values))
    y = dict_values
    #此处关注python2与python3差异，Python3中字典到列表需list显示转换
    #print("###%s#####%s######%s###%s#" % (type(x), type(y), type(dict_keys), type(dict)))
    if select == 1:
        rect = plt.bar(x, y, tick_label = dict_keys)
        plt.xticks(rotation=-15)
        for a, b in zip(x, y):
            plt.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    elif select == 2:
        plt.axes(aspect = 1)
        plt.pie(x = dict_values,autopct = '%3.1f%%', labels = dict_keys)

    else:
        print("图标类型不在可选范围")
        return
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title(my_title)
    fig.savefig(outfile)
