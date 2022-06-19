from ppadb.client import Client as AdbClient

a=0

client=AdbClient(host='127.0.0.1',port=5037)
devices=client.devices()
device=devices[a]
