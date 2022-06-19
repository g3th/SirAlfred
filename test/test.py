#!/usr/bin/python3

#Unicode char testing

print("▄")

print("█")

print("▓")

print("▀")

# function test

users=['one','two','three']
passwords=['first','second','third']

def UserInfo(length,users,passwords):
	print("A total of "+str(length)+" combos are being attempted\n")
	print("Trying Combo: "+str(users)+":"+str(passwords)+"\n")
	return

UserInfo(len(users),users[1],passwords[1])

