import base64
from sys import platform
import os
from colorama import Fore, Back, Style
import colorama
import time
import requests
import webbrowser
import sys as n
import random
import webbrowser
import threading
rhaby2 = int(5)
rhaby = int(1)
ruksI = '''IdMN1w9spls'''
rg = '''D'''
ruks_ = '''[1;36m'''
ruks__ = '''[1;36m'''
jruks = '''[1;37m'''
_ruks = '''[1;31m'''
BGreen = '''[1;32m'''
BRed = '''[1;31m'''
N = 0
R = ''''''

def clear():
    if platform == '''linux''' or platform == '''linux2''':
        os.system('''clear''')
    elif platform == '''win32''':
        os.system('''cls''')

clear()
en = base64.b64decode('''''')
print(en.decode('''UTF-8'''))
print(Fore.GREEN + '''
\033[1;31m
         .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$by$$$$$$
     d$$$$$$$$$$$$$$b
     $$Almunharif$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F * 4$$F * 4$"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$
         "$$$$$$"
          ^$$$$
 4$$c       ""       .$$r
 ^$$$b              e$$$"
 d$$$$$e          z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
 ""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
 $$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
 "*$$$"            ^$$P
    ""              ^"
	''')

try:
	import random,requests,os,asyncio,user_agent
	from user_agent import generate_user_agent 
except ModuleNotFoundError:
	os.system('pip install random')
	os.system('pip install requests')
	os.system('pip install asyncio')
	os.system('clear')

chars = 'azertyuuiopqsdfghjklmwxcvbn'
chars0 = '0987654321'
h = '_'
def tik():
	global num,tele,myadmin,h
	for y in range(num):		
		
		u1 = str("". join(random.choice(chars0+chars)for i in range(5)))
		user = str("". join(random.choice(h+h+h+u1)for i in range(5)))
		head_carlo = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max - age = 0',
                'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
		ree = requests.get(f'https://www.tiktok.com/@{user}?', headers=head_carlo)
		if ree.status_code==404:
			requests.post(f'''https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
𝘼𝙇𝙈𝙀𝙐𝙉𝙃𝙍𝙀𝙁✅ 
←•━━━━━━━━━━━━•→
🏆 𝚄𝚂𝙴𝚁 ➠ {user}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @VlP_12''')                                                 
			print(BGreen+f'⌯ Good User : {user} ')
		else:
			print(BRed+f'⌯ Bad User : {user} ')
def snap():
	global tele,num,myadmin,chars,chars0
	for y in range(num):
		u1 = str("". join(random.choice(chars0+chars)for i in range(5)))
		user = str("". join(random.choice(u1)for i in range(5)))
		url = 'https://accounts.snapchat.com/accounts/get_username_suggestions'
		headers_check = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '57',
			'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
			'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
			'origin': 'https://accounts.snapchat.com',
			'referer': 'https://accounts.snapchat.com/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'same-origin',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
		data_checker = {
			'requested_username': user,
			'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
		req_checker = requests.post(url, data=data_checker, headers=headers_check).text
		if '"status_code":"OK"' in req_checker:
			requests.post(f'''https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
𝘼𝙇𝙈𝙀𝙐𝙉𝙃𝙍𝙀𝙁 ✅ 
←•━━━━━━━━━━━━•→
🏆 𝚄𝚂𝙴𝚁 ➠ {user}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @VlP_12''')                                                 
			print(BGreen+f'⌯ Good User : {user} ')
		else:
			print(BRed+f'⌯ Bad User : {user} ')
			
def insta():
	global tele,num,myadmin,chars,chars0,h
	for y in range(num):
		u1 = str("". join(random.choice(chars0+chars)for i in range(5)))
		user = str("". join(random.choice(h+h+h+u1)for i in range(5)))
		head = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '319',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'mid=YK6KIwALAAFPXuqAe6p00RKBWZIx; ig_did=A6EA6F97-5E6B-4AFE-8865-B8AA6BEC12C2; ig_nrcb=1; shbid=14241; datr=S8G7YI6NN3DQAVegqiUhLmEB; shbts=1623052140.675064; csrftoken=lNBRJc6RDmjmwtNiWxI32faja9EzFpQ3',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': generate_user_agent(),
'x-asbd-id': '437806',
'x-csrftoken': 'lNBRJc6RDmjmwtNiWxI32faja9EzFpQ3',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-instagram-ajax': '8efffa255ae6-hot',
'x-requested-with': 'XMLHttpRequest'
}
		url = 'https://www.instagram.com/accounts/login/ajax/' 
		data = {
		'username': user,
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:102919292:diwddeoded',
		'queryParams': '{}',
		'optIntoOneTap': 'false',
		
		'trustedDeviceRecords': '{}'}
		req = requests.post(url,headers=head,data=data).text
		if '"user":true,"' in req:
			print(BRed+f'⌯ Bad User : {user} ')
		elif ('"user":false,') in req:
			requests.post(f'''https://api.telegram.org/bot{tele}/sendMessage?chat_id={myadmin}&text=
𝘼𝙇𝙈𝙀𝙐𝙉𝙃𝙍𝙀𝙁 ✅ 
←•━━━━━━━━━━━━•→
🏆 𝚄𝚂𝙴𝚁 ➠ {user}
←•━━━━━━━━━━━━•→
🚫 𝐁𝐘 » @VlP_12''')                                                 
			print(BGreen+f'⌯ Good User : {user} ')
		
		
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[2;32m" # White
print(' ')
print(""+BBlue+"["+BWhite+"1"+BBlue+"]"+BWhite+" Tik Tok ")
print(""+BBlue+"["+BWhite+"2"+BBlue+"]"+BYellow+" snap chat")
print(""+BBlue+"["+BWhite+"3"+BBlue+"]"+BPurple+"Instagram")
chose = input(""+BBlue+" ⌯ to choose: ")
if chose == '1':
	myadmin = input(""+BWhite+" ⌯"+BGreen+" lD :  ") 
	tele = input(""+BWhite+" ⌯"+BGreen+" Token :  ") 
	num = int(input(""+BWhite+" ⌯"+BGreen+" Number of users  :  "))
	tik()
if chose == '2':
	myadmin = input(""+BWhite+" ⌯"+BGreen+" lD :  ") 
	tele = input(""+BWhite+" ⌯"+BGreen+" Token :  ") 
	num = int(input(""+BWhite+" ⌯"+BGreen+" Number of users  :  "))
	snap()
if chose == '3':
	myadmin = input(""+BWhite+" ⌯"+BGreen+" lD :  ") 
	tele = input(""+BWhite+" ⌯"+BGreen+" Token :  ") 
	num = int(input(""+BWhite+" ⌯"+BGreen+" Number of users  :  "))
	insta()