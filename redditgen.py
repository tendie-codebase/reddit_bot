# -*- coding: utf-8 -*-
"""
@dev: credits to Sebastian27

Requirements:
    selenium 
    chromedriver (https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/)
        must be in script folder
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import time
import re
import string
import secrets

driver = webdriver.Chrome()  



# GENERATE PASSWORD
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
# PASSWORD GENERATION FINISHED



# NAME GENERATION
driver.get('https://en.wikipedia.org/wiki/Special:Random')
temp = driver.find_element_by_class_name("firstHeading").text
for char in string.punctuation:
    temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, '') #REMOVES SPACES
name = ''.join(temp.split())
name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000,99999) #GENERATES RANDOM NUMBER
text_file = open("namesforreddit.txt", "a")
text_file.write("USR: " + name + str(randomNumber) + " PWD: " + password) #OUTPUTS NAME AND NUMBER
text_file.write("\n")
text_file.close()

finalName = name+str(randomNumber)
time.sleep(1)



# REDDIT ACCOUNT CREATION
driver.get('https://www.reddit.com/register/')
driver.find_element_by_id('regEmail').send_keys('mail@mail.mail')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset[3]/button').click()
time.sleep(3)
driver.find_element_by_id('regUsername').send_keys(finalName)
driver.find_element_by_id('regPassword').send_keys(password)


# reCAPTCHA solver
print("start reCAPTCHA solver, can take time")
time.sleep(3)
ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).key_down(Keys.RETURN).key_up(Keys.RETURN).perform() #AUTOMATICALLY OPENS CAPTCHA

#CAPTACHA solver should be here

driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div/div/div[3]/button').click()
