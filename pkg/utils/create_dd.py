# coding = utf-8

import os

import pandas as pd

from pkg.config import config, dir_dd
from .db import Db
from .tools import save2txt

# 创建数据库字典文件，保存格式.md
class CreateDD(Db):
    columns = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra', 'Comment']

    def __init__(self):
        super(CreateDD, self).__init__()

    def execute(self):
        print('开始生成数据字典......')
        tables = self.get_tables()
        self.create_markdown(tables)
        print('执行结束......')

    # 获取数据库的全部表，show tables只能获取到表名，所以用 show table status
    def get_tables(self):
        sql = """
            show table status;
        """

        return self.query(sql)

    # 获取表的详细信息
    def get_table_info(self, table):
        sql = """
            show full columns from `%s`;
        """ % table

        return self.query(sql)

    # 将数据保存到markdown文件中
    def create_markdown(self, tables):
        file = self.init_file_dd()

        df = pd.DataFrame(tables)
        df = df[['Name', 'Comment']]

        table_list = df.to_dict(orient='index').values()

        title = '|%s|%s|%s|%s|%s|%s|%s|' % tuple(self.columns)
        save2txt(file, '> 共有表：%d张\r[TOC]' % len(table_list))

        index = 1
        for table in table_list:
            # 表名
            save2txt(file, '##### %d.%s-%s' % (index, table['Name'], table['Comment']))
            save2txt(file, title)
            save2txt(file, '| -- | -- | -- | -- | -- | -- | -- |')

            table_info = self.get_table_info(table['Name'])
            df = pd.DataFrame(table_info)
            df = df[self.columns]

            for item in df.to_dict(orient='index').values():
                content = '|%s|%s|%s|%s|%s|%s|%s|' % tuple([item[key] for key in item.keys()])
                save2txt(file, content)

            index += 1

    # 字典文件路径
    def init_file_dd(self):
        file = dir_dd + config['mysql']['datebase'] + '.md'
        if os.path.exists(file):
            os.remove(file)
        return file
