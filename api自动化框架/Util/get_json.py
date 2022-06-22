import sys
sys.path.append("D:/yiq/Demo")
import os

base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
import json


def read_json(file_name= None):
    if file_name == None:
        #file_path = path + "/Config/data.json"
        file_path = "/Demo/Config/data.json"
    else:
        file_path = path + file_name

    with open(file_path, encoding='UTF-8') as f:
    #with open("D:yiq/Demo/Config/data.json", encoding='UTF-8') as f:
        data = json.load(f)
    return data

def get_value(key, file_name=None):
    data = read_json(file_name)
    return data.get(key)
