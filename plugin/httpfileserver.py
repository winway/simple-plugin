#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date : 2018-02-09 14:05:19
# @Author : wangwei (winway1988@163.com)
# @Link : https://winway.github.io
# @Version : 0.1
# @Description : http服务器，用于下载plugin文件
# @History :
# @Other:
#
#      ┏┛ ┻━━━━━┛ ┻┓
#      ┃　　　　　　 ┃
#      ┃　　　━　　　┃
#      ┃　┳┛　  ┗┳　┃
#      ┃　　　　　　 ┃
#      ┃　　　┻　　　┃
#      ┃　　　　　　 ┃
#      ┗━┓　　　┏━━━┛
#        ┃　　　┃   GOD BLESS!
#        ┃　　　┃    NO BUG！
#        ┃　　　┗━━━━━━━━━┓
#        ┃　　　　　　　    ┣┓
#        ┃　　　　         ┏┛
#        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
#          ┃ ┫ ┫   ┃ ┫ ┫
#          ┗━┻━┛   ┗━┻━┛

r"""
http服务器，用于下载plugin文件
"""

import os
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


def startHttpFileServer(dir, port):
    """http服务器，用于下载plugin文件"""

    print('startHttpFileServer')

    ServerClass = BaseHTTPServer.HTTPServer
    HandlerClass = SimpleHTTPRequestHandler
    Protocol = "HTTP/1.0"
    server_address = ('0.0.0.0', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    if os.path.isdir(dir):
        os.chdir(dir)
    else:
        print('no such dir: %s' % dir)
        sys.exit()

    sa = httpd.socket.getsockname()
    print("Serving HTTP on %s:%s" % (sa[0], sa[1]))

    httpd.serve_forever()


if __name__ == '__main__':
    startHttpFileServer(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins'), 8080)
