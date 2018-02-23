#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Date : 2018-02-09 14:04:30
# @Author : wangwei (winway1988@163.com)
# @Link : https://winway.github.io
# @Version : 0.1
# @Description : plugin加载器
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
plugin加载器
"""

import os
import imp
import glob
import hashlib


class Loader(object):
    """plugin加载器
    根据指定模块名，到plugins目录下查找文件并导入
    """

    def __init__(self, pluginDir):
        self.pluginDir = pluginDir
        self.plugins = {}

    def findPlugins(self):
        """遍历目录，查找可导入plugin"""

        plugins = []

        items = os.listdir(self.pluginDir)
        for item in items:
            location = os.path.join(self.pluginDir, item)

            if os.path.isdir(location) and '__init__.py' in os.listdir(location):
                info = imp.find_module('__init__', [location])
            elif os.path.isfile(location) and item.endswith('.py'):
                info = imp.find_module(os.path.splitext(item)[0], [self.pluginDir])
            else:
                continue

            print('find plugin: %s' % item)
            plugins.append({"name": os.path.splitext(item)[0], "info": info, 'md5': self.computeMd5(location)})

        return plugins

    def loadPlugins(self):
        """加载plugin
        调用findPlugins查找可用plugin，加载
        """

        for plugin in self.findPlugins():
            module = {}
            module['module'] = imp.load_module(plugin['name'], *plugin["info"])
            module['md5'] = plugin['md5']
            self.plugins[plugin['name']] = module

        return self.plugins

    def findPlugin(self, moduleName):
        """查找moduleName，并计算md5"""

        location = os.path.join(self.pluginDir, moduleName)

        if os.path.isdir(location) and '__init__.py' in os.listdir(location):
            info = imp.find_module('__init__', [location])
            md5 = self.computeMd5(location)
        elif os.path.isfile(location + '.py'):
            info = imp.find_module(moduleName, [self.pluginDir])
            md5 = self.computeMd5(location + '.py')
        else:
            return False, 'no such module: %s' % moduleName

        plugin = {"name": moduleName, "info": info, 'md5': md5}

        return True, plugin

    def loadPlugin(self, moduleName):
        """加载moduleName
        如果没有加载过或有更新，则重新加载，否则直接返回self.plugins中保存的
        """

        ok, plugin = self.findPlugin(moduleName)
        if not ok:
            return ok, plugin

        if plugin['name'] not in self.plugins:  # 新增
            print('add plugin: %s' % plugin['name'])
            self.plugins[plugin['name']] = {}
            self.plugins[plugin['name']]['module'] = imp.load_module(plugin['name'], *plugin["info"])
            self.plugins[plugin['name']]['md5'] = plugin['md5']
        elif plugin['name'] in self.plugins and plugin['md5'] != self.plugins[plugin['name']]['md5']:  # 更新
            print('update plugin: %s' % plugin['name'])
            self.plugins[plugin['name']]['module'] = imp.load_module(plugin['name'], *plugin["info"])
            self.plugins[plugin['name']]['md5'] = plugin['md5']

        # TODO：删除遗留的module

        return True, self.plugins[plugin['name']]['module']

    def computeMd5(self, entry):
        """计算文件或目录的md5值"""

        md5 = hashlib.md5()

        if os.path.isfile(entry):
            md5.update(open(entry, 'rb').read())
        elif os.path.isdir(entry):
            for path, dirList, fileList in os.walk(entry):
                for file in fileList:
                    if glob.fnmatch.fnmatch(file, '*.py'):
                        md5.update(open(os.path.join(path, file), 'rb').read())

        return md5.hexdigest()
