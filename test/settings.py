from ppadb.client import Client as AdbClient
from pathlib import Path

a=0

def directories():
	directory = str(Path(__file__).parents[1])
	return directory

while True:
	try:
		client=AdbClient(host='127.0.0.1',port=5037)
		devices=client.devices()
		device=devices[a]; break
	except IndexError:
		print('\nAndroid Debug Bridge not started.\nPlease connect your device and run "adb devices" first.\n')
		exit()
	
