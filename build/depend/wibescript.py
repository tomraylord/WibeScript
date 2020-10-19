import os
import time
import threading
import random
import webbrowser
from queue import Queue
import socket

advancedmenu = False

T = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# ################################################################
# Purpose: Clear the console
# ################################################################

def clear():
    os.system("cls")

# ################################################################
# Purpose:
# ################################################################

def printasciiart():
    print('''
     _       ___ __         _____           _       __
    | |     / (_) /_  ___  / ___/__________(_)___  / /_
    | | /| / / / __ \/ _ \ \__ \/ ___/ ___/ / __ \/ __/
    | |/ |/ / / /_/ /  __/ __/ / /__/ /  / / /_/ / /_
    |__/|__/_/_.___/\___//____/\___/_/  /_/ .___/\__/
                                         /_/           ''')

# ################################################################
# Purpose: Password protection
# ################################################################

def login():
    login_key = input('Password: ')
    if login_key == "root":
        os.system("title WibeScript (currently wibing)")
        clear()
        print('Password: ****\n\nLoading [............] 0/3')
        time.sleep(0.5)
        clear()
        print('Password: ****\n\nLoading [####........] 1/3')
        time.sleep(0.5)
        clear()
        print('Password: ****\n\nLoading [############] 3/3')
        time.sleep(0.5)
        clear()
    else:
        clear()
        login()

# ################################################################
# Purpose: CMD Rave
# ################################################################

def rgbthread():
    while True:
        os.system("color c")
        time.sleep(0.5)
        os.system("color a")
        time.sleep(0.5)
        os.system("color 9")
        time.sleep(0.5)

# Multithreading here is needed so we can run other stuff
# otherwise because of sleep functions, nothing will happen.
# Also multithreading will stop CTRL + C shortcut

rgbthread = threading.Thread(target=rgbthread)
# Comment out line below to stop RGB and regain CTRL + C
rgbthread.start()

# ################################################################
# Purpose: Port scanner lib
# ################################################################

target = ""
queue = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports():
    for port in range(1, 49152):
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("\tPort {} is open!".format(port))
            open_ports.append(port)

def run_scanner(threads):

    get_ports()

    thread_list = []

    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("\tOpen ports are:", open_ports)

# ################################################################

# ################################################################
# Purpose: Main Menu
# ################################################################

def menu():
    global advancedmenu
    global target
    printasciiart()
    # print('''
    #    ╔════════════════════════════════════════════════════════════════╗
    #    ║ 1 - Ping IP                    4 - VPN                         ║
    #    ║ 2 - Generate Password          5 - GeoIP                       ║
    #    ║ 3 - Fake Email                                                 ║
    #    ║                                                                ║
    #    ║ 0 - Credits                                                    ║
    #    ╚════════════════════════════════════════════════════════════════╝
    #    ''')
    print('''

         1 - Ping IP                    2 - Generate Password
         3 - VPN                        4 - Fake Email
         5 - GeoIP                      6 - Credits''')
    if advancedmenu == True:
        print('''
         A1 - Free Stressers            A2 - XResolver
         A3 - PS4Resolver               A4 - Port Scanner''')
    menu_opt = input('\n      WibeScript/console: ')
    if menu_opt == '1':
        opt1_ip = input('\n\tIP Address: ')
        os.system("ping " + opt1_ip)
        time.sleep(2.0)
        clear()
        menu()
    if menu_opt == '2':
        try:
            opt2_len = int(input('\n\tPassword length: '))
        except ValueError:
            print('\n\tError: Expected integer value.')
            time.sleep(5)
            clear()
            menu()
        x = 0
        s = ''
        while x < opt2_len:
            z = random.randint(0, len(T) - 1)
            s = s + T[z - 1]
            x = x + 1
        print('\n\t' + s)
        time.sleep(10)
        clear()
        menu()
    if menu_opt == '4':
        webbrowser.open('https://temp-mail.org/en/', new=2)
        clear()
        menu()
    if menu_opt == '3':
        print('\n\tUse temp email (4) to sign up to ProtonVPN with it')
        webbrowser.open_new_tab('https://account.protonvpn.com/login')
        time.sleep(10)
    if menu_opt == '5':
        opt5_ip = input('\n\tIP Address: ')
        webbrowser.open_new_tab('https://www.ip-tracker.org/locator/ip-lookup.php?ip=' + opt5_ip)
        time.sleep(2.0)
    if menu_opt == '6':
        print('\n\tMade by timothy#3273')
        time.sleep(5)
        clear()
        menu()
    # Advanced Menu Hide/Show
    if menu_opt == 'show':
        advancedmenu = True
        os.system("title WibeScript (currently wibing) [advanced]")
        clear()
        menu()
    if menu_opt == 'hide':
        advancedmenu = False
        os.system("title WibeScript (currently wibing)")
        clear()
        menu()
    # Advanced Options
    if menu_opt == 'A1':
        if advancedmenu == True:
            print('\n\tStressthem.to\n\tFreeboot.to\n\tStressing.ninja')
            time.sleep(5)
            clear()
            menu()
        else:
            clear()
            menu()
    if menu_opt == 'A2':
        if advancedmenu == True:
            webbrowser.open_new_tab('https://xresolver.com/')
            clear()
            menu()
        else:
            clear()
            menu()
    if menu_opt == 'A3':
        if advancedmenu == True:
            webbrowser.open_new_tab('https://psnresolver.org/')
            clear()
            menu()
        else:
            clear()
            menu()
    if menu_opt == 'A4':
        if advancedmenu == True:
            opta4_ip = input('\n\tIP Address: ')
            target = opta4_ip
            print('\n')
            run_scanner(100)
            time.sleep(10)
            clear()
            menu()
            target = None
        else:
            clear()
            menu()
    else:
        clear()
        menu()

# ################################################################
# Main 'Script'

os.system("title WibeScript made by timothy#3273")

clear()
login()
menu()
