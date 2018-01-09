import sys
import os
import subprocess
import time
import re

print "VPN builder script for Junos devices \n"


set_commands = {}

print "Configure the IKE proposal \n"
while True:
	ike_proposal_name = raw_input("Please enter a name for the IKE proposal: ")
	if re.match("^[A-Za-z0-9_-]*$", ike_proposal_name):
		print ("The IKE proposal name is: " + ike_proposal_name)
		break
	else:
		print "Enter a valid name"
		continue

menu_ike_proposal_auth_algo = {}
menu_ike_proposal_auth_algo['1'] = "md5"
menu_ike_proposal_auth_algo['2'] = "sha-256"
menu_ike_proposal_auth_algo['3'] = "sha-384"
menu_ike_proposal_auth_algo['4'] = "sha1"

while True:
	options_ike_proposal_auth_algo = menu_ike_proposal_auth_algo.keys()
	options_ike_proposal_auth_algo.sort()
	for entry in options_ike_proposal_auth_algo:
		print entry, menu_ike_proposal_auth_algo[entry]

	selection_ike_proposal_auth_algo = raw_input("Please Select:")
	if selection_ike_proposal_auth_algo == '1':
		conf_auth_algo = menu_ike_proposal_auth_algo['1']
		ike_proposal_auth_algo = "set security ike proposal " + ike_proposal_name + " authentication-algorithm " + menu_ike_proposal_auth_algo['1']
		set_commands['0'] = ike_proposal_auth_algo
		break
	elif selection_ike_proposal_auth_algo == '2':
		conf_auth_algo = menu_ike_proposal_auth_algo['2']
		ike_proposal_auth_algo = "set security ike proposal " + ike_proposal_name + " authentication-algorithm " + menu_ike_proposal_auth_algo['2']
		set_commands['0'] = ike_proposal_auth_algo
		break
	elif selection_ike_proposal_auth_algo == '3':
		conf_auth_algo = menu_ike_proposal_auth_algo['3']
		ike_proposal_auth_algo = "set security ike proposal " + ike_proposal_name + " authentication-algorithm " + menu_ike_proposal_auth_algo['3']
		set_commands['0'] = ike_proposal_auth_algo
		break
	elif selection_ike_proposal_auth_algo == '4':
		conf_auth_algo = menu_ike_proposal_auth_algo['4']
		ike_proposal_auth_algo = "set security ike proposal " + ike_proposal_name + " authentication-algorithm " + menu_ike_proposal_auth_algo['4']
		set_commands['0'] = ike_proposal_auth_algo
		break
	else:
		print "Unknown option selected"


menu_ike_proposal_auth_method = {}
menu_ike_proposal_auth_method['1'] = "dsa-signatures"
menu_ike_proposal_auth_method['2'] = "ecdsa-signatures-256"
menu_ike_proposal_auth_method['3'] = "ecdsa-signatures-384"
menu_ike_proposal_auth_method['4'] = "pre-shared-keys"
menu_ike_proposal_auth_method['5'] = "rsa-signatures"

while True:
	options_ike_proposal_auth_method = menu_ike_proposal_auth_method.keys()
	options_ike_proposal_auth_method.sort()
	for entry in options_ike_proposal_auth_method:
		print entry, menu_ike_proposal_auth_method[entry]

	selection_ike_proposal_auth_method = raw_input("Please Select:")
	if selection_ike_proposal_auth_method == '1':
		conf_auth_method = menu_ike_proposal_auth_method['1']
		ike_proposal_auth_method = "set security ike proposal " + ike_proposal_name + " authentication-method " + menu_ike_proposal_auth_method['1']
		set_commands['1'] = ike_proposal_auth_method
		break
	elif selection_ike_proposal_auth_method == '2':
		conf_auth_method = menu_ike_proposal_auth_method['2']
		ike_proposal_auth_method = "set security ike proposal " + ike_proposal_name + " authentication-method " + menu_ike_proposal_auth_method['2']
		set_commands['1'] = ike_proposal_auth_method
		break
	elif selection_ike_proposal_auth_method == '3':
		conf_auth_method = menu_ike_proposal_auth_method['3']
		ike_proposal_auth_method = "set security ike proposal " + ike_proposal_name + " authentication-method " + menu_ike_proposal_auth_method['3']
		set_commands['1'] = ike_proposal_auth_method
		break
	elif selection_ike_proposal_auth_method == '4':
		conf_auth_method = menu_ike_proposal_auth_method['4']
		ike_proposal_auth_method = "set security ike proposal " + ike_proposal_name + " authentication-method " + menu_ike_proposal_auth_method['4']
		set_commands['1'] = ike_proposal_auth_method
		break
	elif selection_ike_proposal_auth_method == '5':
		conf_auth_method = menu_ike_proposal_auth_method['5']
		ike_proposal_auth_method = "set security ike proposal " + ike_proposal_name + " authentication-method " + menu_ike_proposal_auth_method['5']
		set_commands['1'] = ike_proposal_auth_method
		break
	else:
		print "Unknown option selected"


menu_ike_proposal_dh_group = {}
menu_ike_proposal_dh_group['1'] = "group1"
menu_ike_proposal_dh_group['2'] = "group2"
menu_ike_proposal_dh_group['3'] = "group5"
menu_ike_proposal_dh_group['4'] = "group14"
menu_ike_proposal_dh_group['5'] = "group19"
menu_ike_proposal_dh_group['6'] = "group20"
menu_ike_proposal_dh_group['7'] = "group24"


while True:
	options_ike_proposal_dh_group = menu_ike_proposal_dh_group.keys()
	options_ike_proposal_dh_group.sort()
	for entry in options_ike_proposal_dh_group:
		print entry, menu_ike_proposal_dh_group[entry]

	selection_ike_proposal_dh_group = raw_input("Please Select:")
	if selection_ike_proposal_dh_group == '1':
		conf_dh_group = menu_ike_proposal_dh_group['1']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['1']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '2':
		conf_dh_group = menu_ike_proposal_dh_group['2']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['2']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '3':
		conf_dh_group = menu_ike_proposal_dh_group['3']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['3']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '4':
		conf_dh_group = menu_ike_proposal_dh_group['4']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['4']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '5':
		conf_dh_group = menu_ike_proposal_dh_group['5']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['5']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '6':
		conf_dh_group = menu_ike_proposal_dh_group['6']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['6']
		set_commands['2'] = ike_proposal_dh_group
		break
	elif selection_ike_proposal_dh_group == '7':
		conf_dh_group = menu_ike_proposal_dh_group['7']
		ike_proposal_dh_group = "set security ike proposal " + ike_proposal_name + " dh-group " + menu_ike_proposal_dh_group['7']
		set_commands['2'] = ike_proposal_dh_group
		break
	else:
		print "Unknown option selected"


menu_ike_proposal_enc_algo = {}
menu_ike_proposal_enc_algo['1'] = "3des-cbc"
menu_ike_proposal_enc_algo['2'] = "aes-128-cbc"
menu_ike_proposal_enc_algo['3'] = "aes-128-gcm"
menu_ike_proposal_enc_algo['4'] = "aes-192-cbc"
menu_ike_proposal_enc_algo['5'] = "aes-256-cbc"
menu_ike_proposal_enc_algo['6'] = "aes-256-gcm"
menu_ike_proposal_enc_algo['7'] = "des-cbc"


while True:
	options_ike_proposal_enc_algo = menu_ike_proposal_enc_algo.keys()
	options_ike_proposal_enc_algo.sort()
	for entry in options_ike_proposal_enc_algo:
		print entry, menu_ike_proposal_enc_algo[entry]

	selection_ike_proposal_enc_algo = raw_input("Please Select:")
	if selection_ike_proposal_enc_algo == '1':
		conf_enc_algo = menu_ike_proposal_enc_algo['1']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['1']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '2':
		conf_enc_algo = menu_ike_proposal_enc_algo['2']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['2']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '3':
		conf_enc_algo = menu_ike_proposal_enc_algo['3']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['3']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '4':
		conf_enc_algo = menu_ike_proposal_enc_algo['4']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['4']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '5':
		conf_enc_algo = menu_ike_proposal_enc_algo['5']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['5']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '6':
		conf_enc_algo = menu_ike_proposal_enc_algo['6']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['6']
		set_commands['3'] = ike_proposal_enc_algo
		break
	elif selection_ike_proposal_enc_algo == '7':
		conf_enc_algo = menu_ike_proposal_enc_algo['7']
		ike_proposal_enc_algo = "set security ike proposal " + ike_proposal_name + " encryption-algorithm " + menu_ike_proposal_enc_algo['7']
		set_commands['3'] = ike_proposal_enc_algo
		break
	else:
		print "Unknown option selected"


while True:
	ike_proposal_lifetime_seconds = raw_input("Please enter lifetime, in seconds: ")
	if re.match("^[0-9]*$", ike_proposal_lifetime_seconds):
		ike_proposal_lifetime_seconds_command = "set security ike proposal " + ike_proposal_name + " lifetime-seconds " + ike_proposal_lifetime_seconds
		print ike_proposal_lifetime_seconds_command
		set_commands['4'] = ike_proposal_lifetime_seconds_command
		break
	else:
		print "Enter a valid name"
		continue


menu = {}
menu['1'] = "Show set command"
menu['2'] = "Print curl command"


while True:
	options_menu = menu.keys()
	options_menu.sort()
	for entry in options_menu:
		print entry, menu[entry]

	selection_menu = raw_input("Please Select:")
	if selection_menu == '1':
		for entry in set_commands:
			print set_commands[entry]
		break
	elif selection_menu == '2':
		body = "<security><ike><proposal><name>" + ike_proposal_name + "</name><authentication-method>" + conf_auth_method + "</authentication-method><dh-group>" + conf_dh_group + "</dh-group><authentication-algorithm>" + conf_auth_algo + "</authentication-algorithm><encryption-algorithm>" + conf_enc_algo + "</encryption-algorithm><lifetime-seconds>" + ike_proposal_lifetime_seconds + "</lifetime-seconds></proposal></ike></security>"
		print "curl http://<host>:<port>/rpc/ -u '<username>:<password>' -H 'Content-Type:application/xml' -H 'Accept: application/xml' -d '" + body + "'"

		break
	else:
		print "Unknown option selected"
