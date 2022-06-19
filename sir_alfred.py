#!/usr/bin/python3

import modules.header as header
from modules.clientlist import clientlist as Clients
import clients.expressvpn as expressvpn
import clients.ipvanish as ipvanish
import os

os.system("clear")

header.title(); header.options()

opt=int(input("\nChoose service: "))-1

Clients[opt]()

os.system("clear")

header.AllDone()
