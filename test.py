import requests

cookies = {
    'sb': 'H5N3Zg-7nFT6nKwxa16NzYCO',
    'datr': 'H5N3Zmq5mbrw_0-R-4ZNSd1M',
    'ps_n': '1',
    'ps_l': '1',
    'dpr': '2.061462879180908',
    'fr': '0UPIee7pJ9n3kHb4C..Bmd5Mf..AAA.0.0.Bmrt4d.AWXcK7ApA_k',
    'wd': '891x947',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
    # 'cookie': 'sb=H5N3Zg-7nFT6nKwxa16NzYCO; datr=H5N3Zmq5mbrw_0-R-4ZNSd1M; ps_n=1; ps_l=1; dpr=2.061462879180908; fr=0UPIee7pJ9n3kHb4C..Bmd5Mf..AAA.0.0.Bmrt4d.AWXcK7ApA_k; wd=891x947',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',
}

response = requests.get('https://www.facebook.com/342230082276535', cookies=cookies, headers=headers).url
print(response)