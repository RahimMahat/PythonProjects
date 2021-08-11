#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

webdriver_path = "full_path_to_chromedriver.exe"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_id("bigCookie")
sleep(5)
while True:
    cookie.click()
