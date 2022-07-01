#!/usr/bin/python3
import time
import settings
import keyevents

#Unicode char testing

print("▄")

print("█")

print("▓")

print("▀")

# function test

#users=['one','two','three']
#passwords=['first','second','third']

def UserInfo(length,users,passwords):
	print("A total of "+str(length)+" combos are being attempted\n")
	print("Trying Combo: "+str(users)+":"+str(passwords)+"\n")
	return

#logcat

def logcat():
	while True:
		app = 'com.nordvpn.android'
		keyevents.Tap(335,1253);time.sleep(8)
		error_log = keyevents.logcat(app)
		if 'Network error for URL: https://api.nordvpn.com/v1/users/oauth/login' in error_log:
			print("Unable to connect");break
		else:
			print('Login successful');break


logcat()



