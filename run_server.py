#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Author: Youshumin
@Date: 2019-08-21 11:13:46
LastEditors: YouShumin
LastEditTime: 2020-10-20 11:59:07
@Description:  程序启动文件 提供启动停止功能...
'''
import os
import sys
import logging
import tornado.options
from tornado.options import define, options
import sentry_sdk
from sentry_sdk.integrations.tornado import TornadoIntegration
from oslo.utils.log import LogHandler
from tornado.log import enable_pretty_logging
import tornado.httpserver
import tornado.ioloop
import logging

LOG = logging.getLogger(__name__)
sentry_sdk.init(
    dsn="https://b1696404710445e79550eb272ab9b5c1@sentry.io/1818061",
    integrations=[TornadoIntegration()])

define("debug", default=True, help="enable debug mode")
define("host", default="127.0.0.1", help="run on this host", type=str)
define("port", default="8888", help="run on this port", type=int)


class Application(tornado.web.Application):
    """
        初始化application
    """
    def __init__(self):
        from configs.setting import COOKIE_SECRET
        configs = {
            'debug': options.debug,
            'cookie_secret': COOKIE_SECRET,
            'autoescape': None
        }
        self.format_db()
        self.format_route()
        tornado.web.Application.__init__(self, self.route.get_urls(),
                                         **configs)

    def format_route(self):
        from oslo.web.route import route
        from configs.setting import PATH_APP_ROOT
        from views import route_init
        route_init()
        route_file = open("{}/urls.py".format(PATH_APP_ROOT), "w+")
        write_data = str(route.get_urls())
        route_file.write(write_data)
        route_file.close()
        self.route = route

    def format_db(self):
        from configs.setting import db_init, redis_init
        db_init()
        redis_init()


class APP:
    def __init__(self) -> object:
        tornado.options.parse_command_line(final=False)
        self.handler_project_path()
        self.handler_logger()
        self.set_options()

    def handler_project_path(self):
        from configs.setting import PATH_APP_ROOT
        if PATH_APP_ROOT not in sys.path:
            sys.path.insert(0, PATH_APP_ROOT)

    def handler_logger(self):
        from configs.setting import LOGFILE
        LogHandler(LOGFILE, num=90, stder=options.debug)
        enable_pretty_logging(options=options)

    #设置一些内置参数
    def set_options(self):
        from configs.setting import ALLOW_HOST
        if options.debug:
            logging.getLogger().setLevel(logging.DEBUG)
            define("allow_host", default=[], help="allow_host")
        else:
            define("allow_host", default=ALLOW_HOST, help="allow host")

    def start(self):
        http_server = tornado.httpserver.HTTPServer(Application(),
                                                    xheaders=True)
        http_server.listen(options.port, address=options.host)
        LOG.info("start app on {}:{}".format(options.host, options.port))
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            tornado.ioloop.IOLoop.instance().stop()

    def stop(self):
        tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    main = APP()
    try:
        main.start()
    except KeyboardInterrupt:
        main.stop()