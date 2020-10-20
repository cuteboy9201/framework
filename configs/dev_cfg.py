#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@Author: YouShumin
@Date: 2019-11-20 17:15:56
LastEditTime: 2020-10-13 18:14:41
LastEditors: YouShumin
@Description: 
FilePath: /KwGameManager/configs/dev_cfg.py
'''

# 测试时候的默认设置
from urllib import parse
USE_DB = True
DB_ECHO = False

ALLOW_HOST = ["*"]

LOGFILE = "dev_rbac.log"


def db_init():
    # from oslo.db.module import mysqlHanlder
    # db = mysqlHanlder()
    # db.init(dbname=DB_DEFAULT_NAME, dburl=DB_DEFAULT_URI, dbecho=DB_ECHO)
    pass


def redis_init():
    # from oslo.db.cache_redis import REDIS
    # REDIS.init(db_key_name="123", db_host="192.168.2.34", db_port=20011)
    pass
