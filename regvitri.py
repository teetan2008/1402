try:import requests
except:import os;os.system('pip install requests')
from datetime import datetime
import requests,sys,time,os,random,re
from pystyle import Write,Colors
import base64, requests, json
from time import sleep
from pystyle import *
import threading

def EAAG(cookie, fa):
	head = {
	"Host":"business.facebook.com",
	"upgrade-insecure-requests":"1",
	"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-bA217F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"dnt":"1",
	"x-requested-with":"mark.via.gp",
	"sec-fetch-site":"none",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"accept-encoding":"gzip, deflate",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
	"cookie":cookie,
	}
	access = requests.get("https://business.facebook.com/content_management", headers=head).text
	try:
		token = "EAAG"+access.split('EAAG')[1].split('"')[0]
		return token
	except:
		id = cookie.split("c_user=")[1].split(";")[0]
		fa = fa.replace(" ", "")
		code = requests.get("http://2fa.live/tok/"+fa).json["token"]
		hs = access.split('"haste_session":"')[1].split('"')[0]
		rev = access.split('"server_revision":')[1].split('"')[0]
		hsi = access.split('"hsi":"')[1].split('"')[0]
		fb_dtsg = access.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
		lsd = access.split('"LSD",[],{"token":"')[1].split('"')[0]
		r = access.split('"__spin_r":')[1].split(',')[0]
		t = access.split('"__spin_t":')[1].split(',')[0]
		data ={
		"approvals_code":code,
		"save_device":"false",
		"__user":id,
		"__a":"1",
		"__dyn":"7xeUmF3EfXpUS2q3mbwyyVuC2-m2q3Kq2i5U4e1Fx-ewSxu68uxa2e1Ezobo9E98dEO0G8G6Ehw9-15wfO1YCwjHwuk9wgovyolwuEsxe687C2m3K2y1nUS0jG12KdwnU5W0IU9kbxR12ewi85W1bxq1uG3G48comy84CfxW4U28wdq1iwmEiwuU5Wu0FUkyFo158ixe9zUdEGdwzwea0Lo4K2e1Fwba9w",
		"__csr":"",
		"__req":"8",
		"__hs":hs,
		"dpr":"2",
		"__ccg":"EXCELLENT",
		"__rev":rev,
		"__s":"3z6ci8%3Ar5okmm%3As2km74",
		"__hsi":hsi,
		"__comet_req":"0",
		"fb_dtsg":fb_dtsg,
		"jazoest":"25716",
		"lsd":lsd,
		"__aaid":"5294291090639440",
		"__spin_r":r,
		"__spin_b":"trunk",
		"__spin_t":t,
		"__jssesw":"1"
		}
		head = {
		"Host":"business.facebook.com",
		"x-fb-lsd":lsd,
		"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36",
		"content-type":"application/x-www-form-urlencoded",
		"accept":"*/*",
		"origin":"https://business.facebook.com",
		"x-requested-with":"mark.via.gp",
		"sec-fetch-site":"same-origin",
		"sec-fetch-mode":"cors",
		"sec-fetch-dest":"empty",
		"referer":"https://business.facebook.com/security/twofactor/reauth/?twofac_next=https%3A%2F%2Fbusiness.facebook.com%2Fcontent_management&type=avoid_bypass&app_id=0&save_device=0",
		"accept-encoding":"gzip, deflate",
		"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
		"cookie":cookie
		}
		access = requests.post("https://business.facebook.com/security/twofactor/reauth/enter/", headers=head, data=data).text
		access = requests.get("https://business.facebook.com/content_management", headers=head).text
		try:
			token = "EAAG"+access.split('EAAG')[1].split('"')[0]
			return token
		except:
			return "'die'"

os.system("cls" if os.name == "nt" else "clear")
list_token_page=[]
list_id_page=[]
token_s=1
ckk=input('NHẬP COOKIE FB : ')
h_fa=input('NHẬP 2FA(NẾU CÓ) : ')
cookie=ckk
fa=h_fa
Access = EAAG(cookie, fa)
if "'die'" in Access:
    print("die")
else:
    token = Access
    print('token live'.upper())
os.system("clear")
print("\033[1;31mLưu Ý\033[1;33m:nếu lần 1 chạy chưa lên 50 thì là do quá nhanh nên block đợi 1-2day ae chạy lại tool auto lên hơn 100 page luôn!! ")
id_page=input('\033[1;37mNHẬP ID PAGE MẸ : ')

head = {
"cookie":ckk
}
get_token_page=requests.get('https://graph.facebook.com/v3.1/'+id_page+'?fields=access_token,name&access_token='+token,headers=head).json()

if 'access_token' in get_token_page:
    token_page=get_token_page["access_token"]
    ten=get_token_page["name"]
elif 'error' in get_token_page:print(get_token_page['error']['message'])
else:print(get_token_page)
def reg():
	latitude=random.randrange(9999)
	longitude=random.randrange(3333)
	store_number=random.randrange(999)
	name=requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/female?count=2').json()['data'][0]['name']
	data={'_reqName': 'object:page/locations','_reqSrc': 'LocationManagerUtils','always_open': 'false','differently_open_offerings': '{}','id': id_page,'ignore_warnings': 'true','is_franchise': 'false','locale': 'vi_VN','location': '{"city_id":2599270,"latitude":"21.'+str(latitude)+'","longitude":"105.2'+str(longitude)+'","street":"'+name+'","zip":"10000"}','method': 'post','permanently_closed': 'false','phone': '+84395581887','pickup_options': '[]','place_topics': '["123377808095874","530553733821238"]','pretty': '0','price_range': 'Unspecified','store_name': name,'store_number': store_number,'suppress_http_code': '1'}
	reg=requests.post(f'https://graph.facebook.com/v12.0/{id_page}/locations?access_token={token_page}',data=data,headers=head).json()
	try:
	  id = reg["id"]
	  print(f" ID : {id} | NAME : {name}")
	except:
	  print(reg)
num=50 #ae có thể chỉnh số cao hơn để test xem được bao nhiêu page vtri nha khuyên ae không nên để cao quá 100 vì số cao sẽ dễ nhanh block mình đã test và thấy số này là ổn nhất cho điện thoại nha!.Còn ae có máy tính hay vps core cao càng tốt ae test số cao xem lên bnh page nha
threads=[]
for _ in range(num):
    thread = threading.Thread(target=reg)
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
