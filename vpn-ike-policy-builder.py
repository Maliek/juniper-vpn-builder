import sys
import os
import subprocess
import time
import re

print "VPN builder script for Junos devices \n"

set_commands = {}

print "Configure the IKE policy \n"

while True:
	ike_policy_name = raw_input("Please enter a name for the IKE policy: ")
	if re.match("^[A-Za-z0-9_-]*$", ike_policy_name):
		print ("The IKE proposal name is: " + ike_policy_name)
		break
	else:
		print "Enter a valid name"
		continue


menu_ike_policy_mode = {}
menu_ike_policy_mode['1'] = "aggressive"
menu_ike_policy_mode['2'] = "main"


while True:
	options_ike_policy_mode = menu_ike_policy_mode.keys()
	options_ike_policy_mode.sort()
	for entry in options_ike_policy_mode:
		print entry, menu_ike_policy_mode[entry]

	selection_ike_policy_mode = raw_input("Please Select:")
	if selection_ike_policy_mode == '1':
		ike_policy_mode = "set security ike policy " + ike_policy_name + " mode " + menu_ike_policy_mode['1']
		set_commands['0'] = ike_policy_mode
		break
	elif selection_ike_policy_mode == '2':
		ike_policy_mode = "set security ike policy " + ike_policy_name + " mode " + menu_ike_policy_mode['2']
		set_commands['0'] = ike_policy_mode
		break
	else:
		print "Unknown option selected"
		continue


menu_ike_policy_cert_or_psc = {}
menu_ike_policy_cert_or_psc['1'] = "certificate"
menu_ike_policy_cert_or_psc['2'] = "pre-shared-key"

while True:
	options_ike_policy_cert_or_psc = menu_ike_policy_cert_or_psc.keys()
	options_ike_policy_cert_or_psc.sort()
	for entry in options_ike_policy_cert_or_psc:
		print entry, menu_ike_policy_cert_or_psc[entry]

	selection_ike_policy_cert_or_psc = raw_input("Please Select:")

	if selection_ike_policy_cert_or_psc == '1':
		menu_ike_policy_cert = {}
		menu_ike_policy_cert['1'] = "local-certificate"
		menu_ike_policy_cert['2'] = "peer-certificate-type"
		menu_ike_policy_cert['3'] = "Custom completion"
		while True:
			options_ike_policy_cert = menu_ike_policy_cert.keys()
			options_ike_policy_cert.sort()
			for entry in options_ike_policy_cert:
				print entry, menu_ike_policy_cert[entry]

			selection_ike_policy_cert = raw_input("Please Select:")
			if selection_ike_policy_cert == '1':				
				ike_policy_cert = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['1'] + " " + menu_ike_policy_cert['1'] + " aamw-srx-cert"
				set_commands['1'] = ike_policy_cert
				break
			elif selection_ike_policy_cert == '2':
				menu_ike_policy_peer_cert = {}
				menu_ike_policy_peer_cert['1'] = "pkcs7"
				menu_ike_policy_peer_cert['2'] = "x509-signature"

				while True:
					options_ike_policy_peer_cert = menu_ike_policy_peer_cert.keys()
					options_ike_policy_peer_cert.sort()
					for entry in options_ike_policy_peer_cert:
						print entry, menu_ike_policy_peer_cert[entry]

					selection_ike_policy_peer_cert = raw_input("Please Select:")
					if selection_ike_policy_peer_cert == '1':				
						ike_policy_peer_cert = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['1'] + " " + menu_ike_policy_cert['2'] + " " + menu_ike_policy_peer_cert['1']
						set_commands['1'] = ike_policy_peer_cert
						break
					elif selection_ike_policy_cert == '2':
						ike_policy_peer_cert = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['1'] + " " + menu_ike_policy_cert['2'] + " " + menu_ike_policy_peer_cert['2']
						set_commands['1'] = ike_policy_peer_cert
						break
					else:
						print "Unknown option selected"
						continue
			elif selection_ike_policy_cert == '3':
				ike_policy_cert_custom = raw_input("set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['1'] + " ")
				ike_proposal_policy_cert_command = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['1'] + " " + ike_policy_cert_custom
				set_commands['1'] = ike_proposal_policy_cert_command
			else:
				print "Unknown option selected"
				continue
			break


	if selection_ike_policy_cert_or_psc == '2':
		menu_ike_policy_psc = {}
		menu_ike_policy_psc['1'] = "ascii-text"
		menu_ike_policy_psc['2'] = "hexadecimal"

		while True:
			options_ike_policy_psc = menu_ike_policy_psc.keys()
			options_ike_policy_psc.sort()
			for entry in options_ike_policy_psc:
				print entry, menu_ike_policy_psc[entry]

			selection_ike_policy_psc = raw_input("Please Select:")
			if selection_ike_policy_psc == '1':	
				ike_policy_psc_ascii = raw_input("set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['2'] + " " + menu_ike_policy_psc['1'] + " ")
				ike_proposal_policy_psc_ascii_command = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['2'] + " " + menu_ike_policy_psc['1'] + " " + ike_policy_psc_ascii
				set_commands['1'] = ike_proposal_policy_psc_ascii_command
				break
			elif selection_ike_policy_psc == '2':
				ike_policy_psc_hex = raw_input("set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['2'] + " " + menu_ike_policy_psc['2'] + " ")
				ike_proposal_policy_psc_hex_command = "set security ike policy " + ike_policy_name + " " + menu_ike_policy_cert_or_psc['2'] + " " + menu_ike_policy_psc['2'] + " " + ike_policy_psc_hex
				set_commands['1'] = ike_proposal_policy_psc_hex_command
				break
	break

menu_ike_policy_prop = {}
menu_ike_policy_prop['1'] = "proposal-set"
menu_ike_policy_prop['2'] = "proposals"


while True:
	options_ike_policy_prop = menu_ike_policy_prop.keys()
	options_ike_policy_prop.sort()
	for entry in options_ike_policy_prop:
		print entry, menu_ike_policy_prop[entry]

	selection_ike_policy_prop = raw_input("Please Select:")
	if selection_ike_policy_prop == '1':
		ike_policy_mode = "set security ike policy " + ike_policy_name + " mode " + menu_ike_policy_prop['1']
		set_commands['0'] = ike_policy_mode
		break
	elif selection_ike_policy_prop == '2':
		ike_policy_mode = "set security ike policy " + ike_policy_name + " mode " + menu_ike_policy_prop['2']
		set_commands['0'] = ike_policy_mode
		break
	else:
		print "Unknown option selected"
		continue


for entry in set_commands:
	print set_commands[entry]