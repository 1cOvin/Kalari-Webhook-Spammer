from dhooks import Webhook
import time
from colorama import Fore, Style, init
init()


print(f'''{Fore.BLUE}
▒██   ██▒▓█████  ███▄    █   ██████ 
▒▒ █ █ ▒░▓█   ▀  ██ ▀█   █ ▒██    ▒ 
░░  █   ░▒███   ▓██  ▀█ ██▒░ ▓██▄   
 ░ █ █ ▒ ▒▓█  ▄ ▓██▒  ▐▌██▒  ▒   ██▒
▒██▒ ▒██▒░▒████▒▒██░   ▓██░▒██████▒▒
▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
░░   ░▒ ░ ░ ░  ░░ ░░   ░ ▒░░ ░▒  ░ ░
 ░    ░     ░      ░   ░ ░ ░  ░  ░  
 ░    ░     ░  ░         ░       ░
 '''+Fore.RESET)


message = input ("[+] Input Message You Wanna Spam: ")
webhookurl = Webhook(input("[+] Enter The Webhook: "))
delay = int()

while True:
    time.sleep(0.1)
    webhookurl.send(message)
    print(f'''{Fore.BLUE}[+] Succesfully Sended The Webhook'''+Fore.RESET)
