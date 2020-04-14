#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time      :  16:33
# Email     : spirit_az@foxmail.com
# File      : __init__.py.py
__author__ = 'ChenLiang.Miao'
# import --+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
message = """
author  : MCL
email   : spirit_az@foxmail.com
QQGrp   : 885789807

"""
print(message)
# function +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
import maya.cmds as cmds

needScripts = ['matrixNodes.mll']

for each in needScripts:
    cmds.pluginInfo(each, q=1, l=1) or cmds.loadPlugin(each)
