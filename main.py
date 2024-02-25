import random
import time
import colorama
from colorama import Fore, Back, Style
import fs
from time import sleep

colorama.init()

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            # Identify Brand
            self.cardNumber = number
            self.__findBrand()
            # Luhn's Algorithm
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[!] {self.cardNumber} is a valid Store Card!'
            else:
              return f'{Fore.RED}[!] Invaild Card Number'
              file = open("cards.txt", "w")
              number = repr(number)
              file.write(number)
              file.close()

text = f"""
  ___  ___  ___  ___   ___________ _   _   _____  _____ _   _ 
 / _ \ |  \/  | / _ \ |___  /  _  | \ | | |  __ \|  ___| \ | |
/ /_\ \| .  . |/ /_\ \   / /| | | |  \| | | |  \/| |__ |  \| |
|  _  || |\/| ||  _  |  / / | | | | . ` | | | __ |  __|| . ` |
| | | || |  | || | | |./ /__\ \_/ / |\  | | |_\ \| |___| |\  |
\_| |_/\_|  |_/\_| |_/\_____/\___/\_| \_/  \____/\____/\_| \_/
"""

print(Fore.YELLOW + text)
print(" ")
print(" ")
print(" ")
print(" ")
print(Fore.CYAN + "Made by t.me/zenithail")
print(Fore.BLUE + " ")
print("1. 1k Balance Card")
print("2. 2k Balance Card")
print("3. 5k Balance Card")
print("4. 10k Balance Card")
print(" ")
whatcard = input(f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.GREEN}Option: ")
print(" ")
whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    print("")
    howmany = input(f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.GREEN}How Many Cards You Want: ")
    time.sleep(0.8)
    print("[/] Starting")
    time.sleep(0.8)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811425"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))

if whatcard == 2:
    print("")
    howmany = input(f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.GREEN}How Many Cards You Want: ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578114"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

if whatcard == 3:
    print("")
    howmany = input(f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.GREEN}How Many Cards You Want: ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578118"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

if whatcard == 4:
    howmany = input(f"{Fore.WHITE}[{Fore.BLUE}?{Fore.WHITE}] {Fore.GREEN}How Many Cards You Want: ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "6045781123"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = ''.join([str(bin), str(ff1), str(ff2), str(ff3), str(ff4), str(ff5), str(ff6)])
        print(validator().validate(int(cc)))
        number = repr(number)
        file.write(number)
        file.close()

                