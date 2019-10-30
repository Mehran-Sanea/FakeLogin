#!/usr/bin/env python3

from sys import stdout, argv, exit
from os import system
from time import sleep

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

# Set values.
blue = "\033[94m"
red = "\033[91m"
green = "\033[92m"
blink = "\033[5m"
end_blink = "\033[25m"
loading_bar = "\033[46m"
black = "\033[40m"

one = "hfyr839w nvhfji99 09iijhre dhu7%%4g jg__g739"
two = "00000000 hfyr839w nvhfji99 09iijhre 00006664"
three = "09iijhre dhu7%%4s nvhfji99 09iijhre 98765322"

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

if user_name in real_user_name:
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

for i in range(10):
    print(one)
    print(two)
    print(three)
    sleep(0.5)
    cls()
    if i % 2 == 0:
        one = one.replace("h", "8@")
        two = two.replace("0", "T")
        three = three.replace("i", "n0#")
    else:
        one = one.replace("8", "hf")
        two = two.replace("T", "50")
        three = three.replace("#", "i!")

print(f"{blue}Password:")
slowPrint(8*"*", 0.1)
sleep(2)
cls()
system("rm temp.mts")

print("""
\ \      / /__| | ___ ___  _ __ ___   ___   _    \ \ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ (_)____| |
  \ V  V /  __/ | (_| (_) | | | | | |  __/  |_____| |
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| (_)    | |
                                                 /_/ 

""")

