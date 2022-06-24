#!/usr/bin/python3

import modules.header as header
from modules.clientlist import clientlist as Clients
import clients.expressvpn as expressvpn
import clients.ipvanish as ipvanish
import clients.nord as nord
import os

print("\x1bc")

header.title(); header.options()

opt=int(input("\nChoose service: "))-1

Clients[opt]()

print("\x1bc")

header.AllDone()
