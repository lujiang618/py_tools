# coding: utf-8

import os
import sys

import yaml

product_name = 'py_tools'
root_start = sys.path[0].index(product_name)
root_end = root_start + len(product_name)

# 根目录
root_dir = sys.path[0][0:root_end]

# 配置文件路径
config_file = root_dir + '/config/config.yaml'

# data 目录
data_dir = root_dir + '/data/'
dir_dd = data_dir + 'dd/'
dir_logs = data_dir + 'logs/'

data_path_list = [
    dir_dd,
    dir_logs,
]


def path_exists(path_list):
    for path in path_list:
        if os.path.exists(path):
            continue
        os.makedirs(path)


# 获取配置
def get_config():
    config_dict = {}

    if not os.path.exists(config_file):
        return config_dict

    with open(config_file, 'rb') as f:
        config_dict = yaml.load(f.read(), Loader=yaml.FullLoader)

    return config_dict


path_exists(data_path_list)

config = get_config()
