import sys
import os
import subprocess
import time
import re

print "VPN builder script for Junos devices \n"

set_commands = {}

print "Configure the IKE gateway \n"

while True:
	ike_gw_name = raw_input("Please enter a name for the IKE gateway: ")
	if re.match("^[A-Za-z0-9_-]*$", ike_gw_name):
		print ("The IKE gateway name is: " + ike_gw_name)
		break
	else:
		print "Enter a valid name"
		continu

while True:
	ike_gateway_ike_policy = raw_input("Please enter IKE policy you want to use: ")
	if re.match("^[A-Za-z0-9_-]*$", ike_gateway_ike_policy):
		ike_gw_ike_policy_command = "set security ike gateway " + ike_gw_name + " ike-policy " + ike_gateway_ike_policy
		set_commands['0'] = ike_gw_ike_policy_command
		break
	else:
		print "Enter a valid name"
		continue

while True:
	ike_gateway_address = raw_input("Address or hostname of peer: ")
	if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ike_gateway_address):
		ike_gw_address_command = "set security ike gateway " + ike_gw_name + " address [ " + ike_gateway_address + " ]"
		set_commands['1'] = ike_gw_address_command
		break
	else:
		print "Enter a valid address"
		continue

print "Configure the IKE gateway local-identity \n"

menu_ike_gw_local_identity = {}
menu_ike_gw_local_identity['1'] = "distinguished-name"
menu_ike_gw_local_identity['2'] = "hostname"
menu_ike_gw_local_identity['3'] = "inet"
menu_ike_gw_local_identity['4'] = "inet6"
menu_ike_gw_local_identity['5'] = "key-id"
menu_ike_gw_local_identity['6'] = "user-at-hostname"

while True:
	options_ike_gw_li = menu_ike_gw_local_identity.keys()
	options_ike_gw_li.sort()
	for entry in options_ike_gw_li:
		print entry, menu_ike_gw_local_identity[entry]

	selection_ike_gw_li = raw_input("Please Select:")

	if selection_ike_gw_li == '1':
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['1']
		set_commands['2'] = ike_policy_gw_li
		break
	elif selection_ike_gw_li == '2':
		ike_policy_gw_li_input = raw_input("The local hostname: ")
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['2'] + ike_policy_gw_li_input
		set_commands['2'] = ike_policy_gw_li
		break
	elif selection_ike_gw_li == '3':
		ike_policy_gw_li_input = raw_input("The local IPv4 identity: ")
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['3'] + ike_policy_gw_li_input
		set_commands['2'] = ike_policy_gw_li
		break
	elif selection_ike_gw_li == '4':
		ike_policy_gw_li_input = raw_input("The local IPv6 identity: ")
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['4'] + ike_policy_gw_li_input
		set_commands['2'] = ike_policy_gw_li
		break
	elif selection_ike_gw_li == '5':
		ike_policy_gw_li_input = raw_input("Key ID in ASCII string: ")
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['5'] + ike_policy_gw_li_input
		set_commands['2'] = ike_policy_gw_li
		break
	elif selection_ike_gw_li == '6':
		ike_policy_gw_li_input = raw_input("The local user-FQDN: ")
		ike_policy_gw_li = "set security ike gateway " + ike_gw_name + " local-identity " + menu_ike_gw_local_identity['6'] + ike_policy_gw_li_input
		set_commands['2'] = ike_policy_gw_li
		break
	else:
		print "Unknown option selected"
		continue


print "Configure the IKE gateway remote-identity \n"

menu_ike_gw_remote_identity = {}
menu_ike_gw_remote_identity['1'] = "distinguished-name"
menu_ike_gw_remote_identity['2'] = "hostname"
menu_ike_gw_remote_identity['3'] = "inet"
menu_ike_gw_remote_identity['4'] = "inet6"
menu_ike_gw_remote_identity['5'] = "key-id"
menu_ike_gw_remote_identity['6'] = "user-at-hostname"

while True:
	options_ike_gw_ri = menu_ike_gw_remote_identity.keys()
	options_ike_gw_ri.sort()
	for entry in options_ike_gw_ri:
		print entry, menu_ike_gw_remote_identity[entry]

	selection_ike_gw_ri = raw_input("Please Select:")

	if selection_ike_gw_ri == '1':
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['1']
		set_commands['3'] = ike_policy_gw_ri
		break
	elif selection_ike_gw_ri == '2':
		ike_policy_gw_ri_input = raw_input("The remote hostname: ")
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['2'] + ike_policy_gw_ri_input
		set_commands['3'] = ike_policy_gw_ri
		break
	elif selection_ike_gw_ri == '3':
		ike_policy_gw_ri_input = raw_input("The remote IPv4 identity: ")
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['3'] + ike_policy_gw_ri_input
		set_commands['3'] = ike_policy_gw_ri
		break
	elif selection_ike_gw_ri == '4':
		ike_policy_gw_ri_input = raw_input("The remote IPv6 identity: ")
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['4'] + ike_policy_gw_ri_input
		set_commands['3'] = ike_policy_gw_ri
		break
	elif selection_ike_gw_ri == '5':
		ike_policy_gw_ri_input = raw_input("Key ID in ASCII string: ")
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['5'] + ike_policy_gw_ri_input
		set_commands['3'] = ike_policy_gw_ri
		break
	elif selection_ike_gw_ri == '6':
		ike_policy_gw_ri_input = raw_input("The remote user-FQDN: ")
		ike_policy_gw_ri = "set security ike gateway " + ike_gw_name + " remote-identity " + menu_ike_gw_remote_identity['6'] + ike_policy_gw_ri_input
		set_commands['3'] = ike_policy_gw_ri
		break
	else:
		print "Unknown option selected"
		continue


ike_gateway_ext_int = raw_input("Please enter the external interface for IKE negotiations: ")
ike_gw_ext_int_command = "set security ike gateway " + ike_gw_name + " external-interface " + ike_gateway_ext_int
set_commands['4'] = ike_gw_ext_int_command

print "Configure negotiate using either IKE v1 or IKE v2 protocol \n"

menu_ike_gw_version = {}
menu_ike_gw_version['1'] = "v1-only"
menu_ike_gw_version['2'] = "v2-only"


while True:
	options_ike_gw_version = menu_ike_gw_version.keys()
	options_ike_gw_version.sort()
	for entry in options_ike_gw_version:
		print entry, menu_ike_gw_version[entry]

	selection_ike_gw_version = raw_input("Please Select:")
	if selection_ike_gw_version == '1':
		ike_gw_version = "set security ike gateway " + ike_gw_name + " version " + menu_ike_gw_version['1']
		set_commands['4'] = ike_gw_version
		break
	elif selection_ike_gw_version == '2':
		ike_gw_version = "set security ike gateway " + ike_gw_name + " version " + menu_ike_gw_version['2']
		set_commands['4'] = ike_gw_version
		break
	else:
		print "Unknown option selected"
		continue


print "Configure negotiate using either IKE v1 or IKE v2 protocol \n"

for entry in set_commands:
	print set_commands[entry]