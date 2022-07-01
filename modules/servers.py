import modules.settings
import modules.keyevents as keyevents

from random import randint
from pathlib import Path

proxylist = []

def GrabAProxy():

	with open(str(Path(__file__).parents[0])+'/proxies','r') as proxies:
		for lines in proxies:
			proxylist.append(lines.strip())	
	proxies.close()
	proxy = str(proxylist[randint(0,len(proxylist))])
	return proxy

def ProxyCheck(app):
	a=0
	while a<1:
		error_log = keyevents.logcat(app)
		if 'Network error for URL: https://api.nordvpn.com/v1/users/oauth/login' in error_log:
			print('Bad Proxy');
			return False
			break
		else:
			print('Good Proxy');break
			return True
		a +=1
