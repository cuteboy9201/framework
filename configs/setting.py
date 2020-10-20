#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-10-11 11:24:53
LastEditors: YouShumin
LastEditTime: 2020-09-26 15:13:20
@Description: 
'''

import os
from tornado.options import options
debug = options.debug
PATH_APP_ROOT = os.path.abspath(
    os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))))
COOKIE_SECRET = "0wEE^@!TKGwbC0p@nyY4*Cm*8ojzulHC48HT620YJl^zE61qE"
PROJECT_NAME = "PageGameManager"
HOST = "0.0.0.0"
PORT = 30001

if not debug:
    from configs.cfg import *
else:
    from configs.dev_cfg import *
    LOGFILE = PATH_APP_ROOT + "/" + PROJECT_NAME + ".log"
