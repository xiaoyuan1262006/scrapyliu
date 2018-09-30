from scrapy import cmdline
import os
cmdline.execute("scrapy crawl quotes".split())


import configparser

'''
conf = configparser.ConfigParser()
conf.read(pathutils.getConfigPath() + 'test.ini')       # 文件路径
name = conf.get("baseconf", "host") # 获取指定section 的option值
print(name)
sex = conf.get("baseconf", "port")  # 获取section1 的sex值
print(sex)
'''

'''
import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)


data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


    #当前文件的路径
    pwd = os.getcwd()
    #当前文件的父路径
    father_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    #当前文件的前两级目录
    grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")

'''