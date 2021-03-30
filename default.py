#!/usr/bin/python
# -*- coding: utf8 -*-


import xbmc, xbmcaddon

import time
from os.path import join
from pprint import pformat

# Script constants
__settings__ = xbmcaddon.Addon()
__addon_id__ = "script.service.mypicsdb2"

__language__ = __settings__.getLocalizedString
__homepath__ = __settings__.getAddonInfo('path')


class UpdateService():

    slept = 0
    
    def start(self):
        
        xbmc.log("scan_exec.py : Starting Kodi MyPicsDB2 Update Service", xbmc.LOGINFO)
        # sleep at the beginning "startup_sleep" seconds.
        startup_sleep = abs(int(__settings__.getSetting( "STARTUP_SLEEP" )))

        if startup_sleep > 0:
            while not xbmc.Monitor().abortRequested() and self.slept < startup_sleep:
                #xbmc.sleep(1000)
                KODIMONITOR = xbmc.Monitor()
                KODIMONITOR.waitForAbort( 5 )
                self.slept = self.slept + 5

        self.slept = 0

        while not xbmc.Monitor().abortRequested():

            try:
                # then wait sleep_period (value of var is in seconds)
                sleep_period = abs(int(__settings__.getSetting( "SLEEP_PERIOD" )) * 60)

                if sleep_period > 0 and self.slept >= sleep_period:
                    self.slept = 0
                    script = "%s,--refresh"% join( __homepath__, "..", "plugin.image.mypicsdb2", "scanpath.py")
                    xbmc.executebuiltin('RunScript(%s)'%script)                    

                # sleep at least 5 minutes
                if sleep_period < 5:
                    sleep_period = 5

                # sleep 1 second
                xbmc.sleep(1000)    
                self.slept = self.slept + 1

            except Exception as e:
                xbmc.log(pformat(e))


UpdateService().start()