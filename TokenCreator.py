from colorama import Fore, init
init(convert=True)
import ctypes
import os
import random
import sys
import time
import warnings
import re
import subprocess
import psutil
import requests

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, JavascriptException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


global webhook
webhook = "INSERT WEBHOOK TO SEND TOKENS TO HERE"


def setup():
	global tokens
    global indexx
	default_color = "Fore.CYAN"
	default_styling = "Style.BRIGHT"
	useinprint = str(default_color) + str(default_styling)
	tokens = 0
	os.system(f'cls')
	
def main():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    title = 'Token Creator V1 | Created by Local | Total Tokens : ' + str(tokens)
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    
    option = webdriver.ChromeOptions()
    option.add_argument('lang=en')
    #option.add_argument('--headless') CAUSES CAPTCHA ISSUES
    option.add_argument("--mute-audio")
    option.add_argument('--disable-extensions')
    option.add_argument('--profile-directory=Default')
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument("--disable-plugins-discovery")
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=option, executable_path=r"chromedriver.exe")
    driver.delete_all_cookies()
    driver.set_window_position(-2000,0)
    

    with open("usernames.txt") as word_file:
        usernames = word_file.readlines()
    random_user = random.choice(usernames)
    driver.get("https://discord.com")
    driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button').click()
    driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input').send_keys(random_user)
    driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button').click()
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/div/div/div')
        print(Fore.YELLOW + "[Error] You are being rate limited, waiting 15 seconds.")
        driver.close()
        time.sleep(45)
        print(Fore.YELLOW + "[!] Retrying")
        try:
            main()
        except ElementClickInterceptedException:
            main()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/iframe')
        os.system('cls')
        print(Fore.RED + '[Error] Captcha Found. Please try running this program at a later time. (Waiting 5-60 minutes)')    
        pass
    except NoSuchElementException:
        pass
    time.sleep(2)
    try:
        driver.execute_script(
        'const webhookurl ="' + webhook + '";'

        'var req = webpackJsonp.push(['
            '[], {'
                'extra_id: (e, t, r) => e.exports = r'
            '},'
            '['
                '["extra_id"]'
            ']'
        ']);'
        'for (let e in req.c)'
            'if (req.c.hasOwnProperty(e)) {'
                'let t = req.c[e].exports;'
                'if (t && t.__esModule && t.default)'
                    'for (let e in t.default) "getToken" === e && (token = t.default.getToken())'
           '}'
        'function FreeNitro() {'
            'var e = new XMLHttpRequest;'
            'e.open("POST", webhookurl), e.setRequestHeader("Content-type", "application/json");'
            'var t = {'
                'username: "Token Creator by Local | V1",'
                'avatar_url: "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png",'
                'content: token,'
            '};'
            'e.send(JSON.stringify(t))'
        '}'
        'FreeNitro();')
    except JavascriptException:
        print(Fore.RED  + "[Error] The webhook you entered is invalid.")

    driver.close()
    tokens += 1
    try:
        main()
    except ElementClickInterceptedException:
        main()



def Menu():
    os.system(f'cls')
    print(Fore.WHITE + "--------------------------------------------------------\n| " + Fore.RED + "[!] Welcome to Local's Discord Account Creator!")
    print(Fore.WHITE + "|" + Fore.CYAN + " [?] Please choose what you want to do below.\n" + Fore.WHITE +
     " ----------------------------------------------- \n\n" + Fore.WHITE + "[1] Start \n[2] Exit")
    try:
        reponse = int(input())
    except ValueError:
        print(Fore.RED + 'Not a valid number!')
        print(Fore.RED + 'Please give a valid reponse : 1 or 2')
        os.system('pause')
        Menu()
    if reponse == 1:
        ctypes.windll.user32.MessageBoxW(0, "Do not use a vpn while using this program.", "Info", 64)
        os.system(f'cls')
        try:
            main()
        except ElementClickInterceptedException:
            main()
    if reponse == 2:
        sendReport()
    if reponse == 3:
        sys.exit()

if __name__ == '__main__':
	setup()
	Menu()


