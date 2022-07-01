#!/usr/bin/python3
#shell keyevents/sendevents

import modules.settings as settings

def Menu():
	cmd = settings.device.shell('input keyevent 1')
	return cmd

def Home():
	cmd = settings.device.shell('input keyevent 3')
	return cmd

def Power():
	cmd = settings.device.shell('input keyevent 26')
	return cmd

def Enter():
	cmd = settings.device.shell('input keyevent 66')
	return cmd

def Menu():
	cmd = settings.device.shell('input keyevent 82')
	return cmd

def StartApp(app):
	cmd = settings.device.shell('monkey -p '+app+' 1')
	return cmd

def Write(Text):
	cmd = settings.device.shell('input text '+Text)
	return cmd

def Tab(times):
	counter=0
	while counter < times: 
		settings.device.shell('input keyevent 61')
		counter +=1

def Tap(x,y):
	cmd = settings.device.shell('input tap '+str(x)+" "+str(y))
	return cmd

def StopApp(app):
	cmd = settings.device.shell('am force-stop '+app)
	return cmd

def Escape():
	cmd = settings.device.shell('input keyevent 111')
	return cmd

def GetActivity(internalVariable):
	cmd = settings.device.shell("dumpsys window windows | grep -E '"+internalVariable+"'")
	return cmd

def ClearData(app):
	cmd = settings.device.shell("pm clear "+app)
	return cmd

def SetUpAProxy(proxy):
	cmd = settings.device.shell('settings put global http_proxy '+proxy)
	return cmd
	
def ResetConnection():
	cmd = settings.device.shell('settings put global http_proxy :0')
	return cmd
	
def logcat(app):
	cmd = settings.device.shell('logcat -d *:E | grep '+app)
	return cmd
