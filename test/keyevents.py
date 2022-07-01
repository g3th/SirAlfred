#!/usr/bin/python3
#shell keyevents/sendevents

import settings

def Tap(x,y):
	cmd = settings.device.shell('input tap '+str(x)+" "+str(y))
	return cmd
	
def logcat(app):
	cmd = settings.device.shell('logcat -d *:E | grep '+app)
	clear = settings.device.shell('logcat -c')
	return cmd, clear
