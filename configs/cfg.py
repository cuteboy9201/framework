#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2020-01-13 16:56:52
LastEditTime: 2020-09-30 14:30:27
LastEditors: YouShumin
@Description: 
FilePath: /KwGameManager/configs/cfg.py
'''
from urllib import parse
USE_DB = True
DB_ECHO = True

ALLOW_HOST = ["*"]

LOGFILE = "/Users/youshumin/logs/kwgamemanager.log"

# 默认数据库


def db_init():
    # from oslo.db.module import mysqlHanlder
    # db = mysqlHanlder()
    # db.init(dbname=DB_DEFAULT_NAME, dburl=DB_DEFAULT_URI, dbecho=DB_ECHO)
    pass


def redis_init():
    # from oslo.db.cache_redis import REDIS
    # REDIS.init(db_key_name="123", db_host="192.168.2.34", db_port=20011)
    pass