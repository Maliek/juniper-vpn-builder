import sys
import os
import subprocess
import time
import re

print "VPN builder script for Junos devices \n"


set_commands = {}

print "Configure the IPSEC proposal \n"
while True:
	ipsec_proposal_name = raw_input("Please enter a name for the IPSEC proposal: ")
	if re.match("^[A-Za-z0-9_-]*$", ipsec_proposal_name):
		print ("The IPSEC proposal name is: " + ipsec_proposal_name)
		break
	else:
		print "Enter a valid name"
		continue

print "Configure the IPSEC proposal protocol \n"

menu_ipsec_proposal_protocol = {}
menu_ipsec_proposal_protocol['1'] = "ah"
menu_ipsec_proposal_protocol['2'] = "esp"

while True:
	options_ipsec_proposal_protocol = menu_ipsec_proposal_protocol.keys()
	options_ipsec_proposal_protocol.sort()
	for entry in options_ipsec_proposal_protocol:
		print entry, menu_ipsec_proposal_protocol[entry]

	selection_ipsec_proposal_protocol = raw_input("Please Select:")
	if selection_ipsec_proposal_protocol == '1':
		ipsec_proposal_protocol = "set security ipsec proposal " + ipsec_proposal_name + " protocol " + menu_ipsec_proposal_protocol['1']
		set_commands['0'] = ipsec_proposal_protocol
		break
	elif selection_ipsec_proposal_protocol == '2':
		ipsec_proposal_protocol = "set security ipsec proposal " + ipsec_proposal_name + " protocol " + menu_ipsec_proposal_protocol['2']
		set_commands['0'] = ipsec_proposal_protocol
		break
	else:
		print "Unknown option selected"


menu_ipsec_proposal_auth_algo = {}
menu_ipsec_proposal_auth_algo['1'] = "hmac-md5-96"
menu_ipsec_proposal_auth_algo['2'] = "hmac-sha-256-128"
menu_ipsec_proposal_auth_algo['3'] = "hmac-sha1-96"

while True:
	options_ipsec_proposal_auth_algo = menu_ipsec_proposal_auth_algo.keys()
	options_ipsec_proposal_auth_algo.sort()
	for entry in options_ipsec_proposal_auth_algo:
		print entry, menu_ipsec_proposal_auth_algo[entry]

	selection_ipsec_proposal_auth_algo = raw_input("Please Select:")
	if selection_ipsec_proposal_auth_algo == '1':
		ipsec_proposal_auth_algo = "set security ipsec proposal " + ipsec_proposal_name + " authentication-method " + menu_ipsec_proposal_auth_algo['1']
		set_commands['1'] = ipsec_proposal_auth_algo
		break
	elif selection_ipsec_proposal_auth_algo == '2':
		ipsec_proposal_auth_algo = "set security ipsec proposal " + ipsec_proposal_name + " authentication-method " + menu_ipsec_proposal_auth_algo['2']
		set_commands['1'] = ipsec_proposal_auth_algo
		break
	elif selection_ipsec_proposal_auth_algo == '3':
		ipsec_proposal_auth_algo = "set security ipsec proposal " + ipsec_proposal_name + " authentication-method " + menu_ipsec_proposal_auth_algo['3']
		set_commands['1'] = ipsec_proposal_auth_algo
		break
	else:
		print "Unknown option selected"


menu_ipsec_proposal_enc_algo = {}
menu_ipsec_proposal_enc_algo['1'] = "3des-cbc"
menu_ipsec_proposal_enc_algo['2'] = "aes-128-cbc"
menu_ipsec_proposal_enc_algo['3'] = "aes-128-gcm"
menu_ipsec_proposal_enc_algo['4'] = "aes-192-cbc"
menu_ipsec_proposal_enc_algo['5'] = "aes-256-cbc"
menu_ipsec_proposal_enc_algo['6'] = "aes-256-gcm"
menu_ipsec_proposal_enc_algo['7'] = "des-cbc"


while True:
	options_ipsec_proposal_enc_algo = menu_ipsec_proposal_enc_algo.keys()
	options_ipsec_proposal_enc_algo.sort()
	for entry in options_ipsec_proposal_enc_algo:
		print entry, menu_ipsec_proposal_enc_algo[entry]

	selection_ipsec_proposal_enc_algo = raw_input("Please Select:")
	if selection_ipsec_proposal_enc_algo == '1':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['1']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '2':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['2']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '3':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['3']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '4':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['4']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '5':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['5']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '6':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['6']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	elif selection_ipsec_proposal_enc_algo == '7':
		ipsec_proposal_enc_algo = "set security ipsec proposal " + ipsec_proposal_name + " encryption-algorithm " + menu_ipsec_proposal_enc_algo['7']
		set_commands['2'] = ipsec_proposal_enc_algo
		break
	else:
		print "Unknown option selected"


while True:
	ipsec_proposal_lifetime_seconds = raw_input("Please enter lifetime, in seconds: ")
	if re.match("^[0-9]*$", ipsec_proposal_lifetime_seconds):
		ipsec_proposal_lifetime_seconds_command = "set security ipsec proposal " + ipsec_proposal_name + " lifetime-seconds " + ipsec_proposal_lifetime_seconds
		print ipsec_proposal_lifetime_seconds_command
		set_commands['3'] = ipsec_proposal_lifetime_seconds_command
		break
	else:
		print "Enter a valid name"
		continue


for entry in set_commands:
	print set_commands[entry]