
# coding = utf-8

import datetime
import logging
import os

import MySQLdb

from pkg.config import config, dir_logs


class Db(object):
    cursor = None

    def __init__(self):
        mysql = config['mysql']

        db = MySQLdb.connect(
            host=mysql['host'],
            user=mysql['username'],
            password=str(mysql['password']),
            database=mysql['datebase'],
            charset=mysql['charset'],
            use_unicode=True,
            connect_timeout=30
        )
        self.cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def query(self, sql):
        today = datetime.date.today()

        dir_path = dir_logs + today.strftime('%Y-%m-%d')

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        logging.basicConfig(
            level=logging.INFO,  # 控制台打印的日志级别
            filename=dir_path + '/sql.log',
            filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志 # a是追加模式，默认如果不写的话，就是追加模式
            format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
        )

        logging.info(sql)

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        return data
