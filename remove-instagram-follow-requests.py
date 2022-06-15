from asyncio import sleep
from selenium import webdriver
from bs4 import BeautifulSoup 
import time
from selenium.webdriver.support.select import Select
browser = webdriver.Firefox()

username = 'YOUR ACCOUNT'
password = 'YOUR PASSWORD'

browser.get('https://www.instagram.com/accounts/login/')

usernameInput = browser.find_element_by_xpath('//input[@name = "username"]')
usernameInput.send_keys(username)

passwordInput = browser.find_element_by_xpath('//input[@name = "password"]')
passwordInput.send_keys(password)

browser.find_element_by_xpath('//button[@class = "sqdOP  L3NKy   y3zKF     "]').click()


time.sleep(10)
browser.find_element_by_xpath('//a[@href = "/accounts/activity/"]').click()
time.sleep(10)

browser.find_element_by_xpath('//div[@class = "PUHRj eKc9b H_sJK"]').click()
mainBox = browser.page_source
soup = BeautifulSoup(mainBox, 'html.parser')

def clickBTN():
    time.sleep(2)
    browser.find_element_by_xpath('//button[text()="Delete"]').click()
    
deleteBTN = soup.find_all("button", string="Delete")

for i in deleteBTN:
    clickBTN()

    





















