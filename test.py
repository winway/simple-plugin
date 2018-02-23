#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date : 2018-02-23 16:45:21
# @Author : wangwei (winway1988@163.com)
# @Link : https://winway.github.io
# @Version : 0.1
# @Description : 这个家伙很懒，没有留下任何信息
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
docstring for module
"""

import os
import time

from plugin import loader

p = loader.Loader('/tmp')

while True:
    os.system("wget -q -r -np -nH --reject='index.html*,*.pyc' -P %s 'http://127.0.0.1:8080'" % p.pluginDir)

    ok, m = p.loadPlugin('pluginA')
    if ok:
        getattr(m, 'f')()
    else:
        print 'no such plugin pluginA'

    ok, m = p.loadPlugin('pluginB')
    if ok:
        getattr(m, 'f')()
    else:
        print 'no such plugin pluginB'

    ok, m = p.loadPlugin('pluginC')
    if ok:
        getattr(m, 'f')()
    else:
        print 'no such plugin pluginC'

    ok, m = p.loadPlugin('pluginD')
    if ok:
        getattr(m, 'f')()
    else:
        print 'no such plugin pluginD'

    time.sleep(5)
