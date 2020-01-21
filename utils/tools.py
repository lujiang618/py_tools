# coding = utf-8

import matplotlib.pyplot as plt
import os
import shutil
from bs4 import BeautifulSoup


def strip_html_tag(text):
    if text is None or len(text) == 0:
        return text
    soup = BeautifulSoup(text, 'html.parser')

    result = soup.get_text()
    result = result.replace('\n', '')
    result = re.sub('\?|\s', '', result)

    return result


# 删除data目录下所有文件
def del_data_file(data_path):
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    file_list = os.listdir(data_path)

    for file in file_list:
        file_path = os.path.join(data_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, True)


def paint_common(title, path, x_label='Date'):
    plt.gcf().autofmt_xdate(rotation=50)
    plt.axis('tight')
    plt.xlabel(x_label, size=20)

    plt.title(title, size=20)
    plt.tick_params(axis='x', labelsize=9)  # 设置x轴标签大小
    plt.legend(loc='best')

    if not os.path.exists(path):
        os.makedirs(path)

    plt.savefig(path + title + '.png')

    plt.show()


def print_star(text):
    print("*" * 60 + text + "*" * 60)
