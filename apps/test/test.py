#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Author: YouShumin
Date: 2020-10-20 11:43:35
LastEditTime: 2020-10-20 11:52:55
LastEditors: YouShumin
Description: Another flat day
FilePath: /framework_py3/apps/test/test.py
'''

import logging

from tornado.gen import coroutine

from oslo.web.requesthandler import MixinRequestHandler
from oslo.web.route import route

LOG = logging.getLogger("__name__")


@route("/hello/")
class HelloWorld(MixinRequestHandler):
    @coroutine
    def get(self, *args, **kwargs):
        data = "HelloWorld!!!"
        self.send_ok_json(data=data, code=0)
        return
