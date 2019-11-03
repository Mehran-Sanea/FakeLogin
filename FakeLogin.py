#!/usr/bin/env python3

from sys import stdout, argv, exit
from os import system
from time import sleep
from hashlib import sha256

"""
This funny script make your terminal cool when you start it up.
A fake login with fake procces shows.
All that you need it's to run install file.(chmod +x install && ./install)

***Created by Mehran The SANea***
***mehran.python@gmail.com***
***I,m wainting for your feedbacks.***
"""

# Print a text slowly and char to char.
def slowPrint(text, t=0.2):
    """
    Slow Print...
    You can change print speed throgh change TIME.SLEEP(n) value. (n = numric values.)
    """
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(t)

# Clear the screen.
def cls():
    system("clear")

# make Hashes for crack ShowOff.
def hash(value):
    hashed = sha256(str(value).encode("utf-8")).hexdigest()
    return hashed

# Set values.
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
blink = "\033[5m"
end_blink = "\033[25m"
loading_bar = "\033[46m"
black = "\033[40m"

# Start
if len(argv) >= 2:
    if argv[1] == "-h" or argv[1] == "--help":
        cls()
        print("[*] Usage:\n@:~/ sudo chmod +x install && ./install\n\nManually:\n*** Enter chmod +x FakeLoggin.py then copy FakeLoggin.py in /usr/bin")
        exit(1)
    else:
        cls()
        print(f"{red}Syntax Error:\n\tEnter '-h' or '--help' as argument.")

system("whoami > temp.mts")
cls()
with open("temp.mts", "r") as file:
    real_user_name = file.read()

user_name = input(f"{red}Please enter your name for login:{green} ")
if user_name in real_user_name and len(user_name) == (len(real_user_name))-1:
    print(f"{green}[*]\tCorrect!")
    sleep(1)
    cls()
else:
    cls()
    print(f"{red}[!]\t{blue}You enter {red}{user_name}{blue} as a user name!\nNo problem I can find your correct user name. {blue}:)".expandtabs(2))
    sleep(1)
    print(f"{blue}Start searching:")
    slowPrint(f"{loading_bar}            {black}")
    print(f"{blink}{green}Find succesful!")
    sleep(1)
    print(end_blink)
    slowPrint(green+real_user_name)
    sleep(2)
    cls()

print(f"{red}{blink}Cracking your password:{end_blink}")

for i in range(7):
    print(hash(i))
    print(hash(i+233))
    print(hash(i**4))
    sleep(0.2)

print(f"{blue}Password:")
slowPrint(8*"*", 0.1)
sleep(2)
cls()
system("rm temp.mts")

print(f"""
\ \      / /__| | ___ ___  _ __ ___   ___   _    \ \ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ (_)____| |
  \ V  V /  __/ | (_| (_) | | | | | |  __/  |_____| |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)    | |
                                                 /_/ 
{red}[*] For uninstall type: {green}FakeLoginUninstall
""")


