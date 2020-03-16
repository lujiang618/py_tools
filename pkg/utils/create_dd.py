# coding = utf-8

import os

import pandas as pd

from pkg.config import config, dir_dd
from .db import Db
from .tools import save2txt


class CreateDD(Db):
    columns = ['Field', 'Type', 'Null', 'Key', 'Default', 'Extra', 'Comment']

    def __init__(self):
        super(CreateDD, self).__init__()

    def execute(self):
        print('开始生成数据字典......')
        tables = self.get_tables()
        self.create_markdown(tables)
        print('执行结束......')

    def get_tables(self):
        sql = """
            show tables;
        """

        return self.query(sql)

    def get_table_info(self, table):
        sql = """
            show full columns from `%s`;
        """ % table

        return self.query(sql)

    def create_markdown(self, tables):
        df = pd.DataFrame(tables)
        table_list = df['Tables_in_promotion_management'].to_numpy().tolist()
        file = dir_dd + config['mysql']['datebase'] + '.md'
        if os.path.exists(file):
            os.remove(file)

        title = '|%s|%s|%s|%s|%s|%s|%s|' % tuple(self.columns)
        save2txt(file, '> 共有表：%d张\r\n[TOC]' % len(table_list))

        index = 1
        for table in table_list:
            # 表名
            save2txt(file, '##### %d.%s' % (index, table))
            save2txt(file, title)
            save2txt(file, '| -- | -- | -- | -- | -- | -- | -- |')

            table = self.get_table_info(table)
            df = pd.DataFrame(table)
            df = df[self.columns]

            for item in df.to_dict(orient='index').values():
                content = '|%s|%s|%s|%s|%s|%s|%s|' % tuple([item[key] for key in item.keys()])
                save2txt(file, content)

            index += 1
