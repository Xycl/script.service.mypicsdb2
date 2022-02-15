#!/usr/bin/python
# -*- coding: utf8 -*-

import xbmc, xbmcaddon

from os.path import join
from pprint import pformat

# Script constants
__settings__ = xbmcaddon.Addon()
__homepath__ = __settings__.getAddonInfo('path')

def scan_exec():
    xbmc.log("scan_exec.py : Starting Kodi Image Library Update", xbmc.LOGINFO)
    common.run_script("script.module.mypicsdb2scanner,--refresh")         

if __name__=="__main__":
    try:
	    scan_exec()
    except Exception as e:
        xbmc.log(pformat(e))
