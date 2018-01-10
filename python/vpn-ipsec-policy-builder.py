import sys
import os
import subprocess
import time
import re

print "VPN builder script for Junos devices \n"


set_commands = {}

print "Configure the IPSEC policy \n"
while True:
	ipsec_policy_name = raw_input("Please enter a name for the IPSEC policy: ")
	if re.match("^[A-Za-z0-9_-]*$", ipsec_policy_name):
		print ("The IPSEC policy name is: " + ipsec_policy_name)
		break
	else:
		print "Enter a valid name"
		continue

print "Configure the IPSEC policy perfect forward secrecy \n"

menu_ipsec_policy_dh_group = {}
menu_ipsec_policy_dh_group['1'] = "group1"
menu_ipsec_policy_dh_group['2'] = "group2"
menu_ipsec_policy_dh_group['3'] = "group5"
menu_ipsec_policy_dh_group['4'] = "group14"
menu_ipsec_policy_dh_group['5'] = "group19"
menu_ipsec_policy_dh_group['6'] = "group20"
menu_ipsec_policy_dh_group['7'] = "group24"


while True:
	options_ipsec_policy_dh_group = menu_ipsec_policy_dh_group.keys()
	options_ipsec_policy_dh_group.sort()
	for entry in options_ipsec_policy_dh_group:
		print entry, menu_ipsec_policy_dh_group[entry]

	selection_ipsec_policy_dh_group = raw_input("Please Select:")
	if selection_ipsec_policy_dh_group == '1':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['1']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '2':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['2']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '3':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['3']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '4':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['4']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '5':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['5']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '6':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['6']
		set_commands['1'] = ipsec_policy_dh_group
		break
	elif selection_ipsec_policy_dh_group == '7':
		ipsec_policy_dh_group = "set security ipsec policy " + ipsec_policy_name + " perfect-forward-secrecy keys " + menu_ipsec_policy_dh_group['7']
		set_commands['1'] = ipsec_policy_dh_group
		break
	else:
		print "Unknown option selected"


menu_ipsec_policy_prop = {}
menu_ipsec_policy_prop['1'] = "policy-set"
menu_ipsec_policy_prop['2'] = "policys"

while True:
	options_ipsec_policy_prop = menu_ipsec_policy_prop.keys()
	options_ipsec_policy_prop.sort()
	for entry in options_ipsec_policy_prop:
		print entry, menu_ipsec_policy_prop[entry]

	selection_ipsec_policy_prop = raw_input("Please Select:")
	if selection_ipsec_policy_prop == '1':
		menu_ipsec_policy_prop_set = {}
		menu_ipsec_policy_prop_set['1'] = "basic"
		menu_ipsec_policy_prop_set['2'] = "compatible"
		menu_ipsec_policy_prop_set['3'] = "prime-128"
		menu_ipsec_policy_prop_set['4'] = "prime-256"
		menu_ipsec_policy_prop_set['5'] = "standard"
		menu_ipsec_policy_prop_set['6'] = "suiteb-gcm-128"
		menu_ipsec_policy_prop_set['7'] = "suiteb-gcm-256"
		while True:
			options_ipsec_policy_prop_set = menu_ipsec_policy_prop_set.keys()
			options_ipsec_policy_prop_set.sort()
			for entry in options_ipsec_policy_prop_set:
				print entry, menu_ipsec_policy_prop_set[entry]

			selection_ipsec_policy_prop_set = raw_input("Please Select:")

			if selection_ipsec_policy_prop_set == '1':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['1']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '2':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['2']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '3':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['3']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '4':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['4']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '5':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['5']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '6':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['6']
				set_commands['2'] = ipsec_policy_prop_set
				break
			elif selection_ipsec_policy_prop_set == '7':
				ipsec_policy_prop_set = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['1'] + " " +  menu_ipsec_policy_prop_set['7']
				set_commands['2'] = ipsec_policy_prop_set
				break
			else:
				print "Unknown option selected"
				continue
		break
	elif selection_ipsec_policy_prop == '2':
		ipsec_policy_props_input = raw_input("set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['2'] + " ")
		ipsec_policy_policy_props_command = "set security ipsec policy " + ipsec_policy_name + " " + menu_ipsec_policy_prop['2'] + " [ " + ipsec_policy_props_input + " ]"
		set_commands['2'] = ipsec_policy_policy_props_command
		break
	else:
		print "Unknown option selected"
		continue
	break

for entry in set_commands:
	print set_commands[entry]