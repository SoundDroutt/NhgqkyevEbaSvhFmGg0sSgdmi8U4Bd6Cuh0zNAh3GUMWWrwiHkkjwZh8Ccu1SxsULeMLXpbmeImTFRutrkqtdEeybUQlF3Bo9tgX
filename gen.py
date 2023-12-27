import requests
import json
import time
import random
import string
from colorama import Fore, Style;

print(f"\n{Fore.RED}𝗕𝘂 𝘁𝗼𝗼𝗹 𝗙𝗮𝘁𝗶𝗵 𝗔𝘆𝗮𝗻 𝘁𝗮𝗿𝗮𝗳ı𝗻𝗱𝗮𝗻 𝗸𝘂𝗿𝘂𝗹𝗺𝘂ş𝘁𝘂𝗿.{Style.RESET_ALL}")
print(f"{Fore.CYAN}𝘿𝙞𝙨𝙘𝙤𝙧𝙙 𝙏𝙤𝙥𝙡𝙪𝙡𝙪𝙜𝙪𝙢𝙪𝙯: 𝙝𝙩𝙩𝙥𝙨://𝙗𝙞𝙩.𝙡𝙮/𝙛𝙖𝙩𝙞𝙝𝙘𝙢{Style.RESET_ALL}\n\n")

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

if __name__ == "__main__":
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }

    data = {
        'partnerUserId': generate_random_string(64)
    }

    session = requests.Session()
    try:
        while True:
            response = session.post(url, headers=headers, json=data)

            if response.status_code == 200:
                token = response.json()['token']
                with open('kodlar.txt', 'a') as file:
                    file.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n")
                print(f"{Fore.GREEN}➤ Promosyon kodlar.txt dosyasına kaydedildi!{Style.RESET_ALL}\n")            
     
            else:
                print(f"İstek şu durum koduyla başarısız oldu: {response.status_code}.")
                print(f"Hata mesajı: {response.text}")

            time.sleep(1)

    except Exception as e:
        print(f"Bir hata oluştu: {str(e)}")

    finally:
        session.close()
