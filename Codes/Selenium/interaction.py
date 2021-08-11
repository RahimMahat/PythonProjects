#!/usr/bin/env python3
from selenium import webdriver
# to send any keys other than letter
from selenium.webdriver.common.keys import Keys


webdriver_path = "full_path_to_chromedriver.exe"
driver = webdriver.Chrome(executable_path=webdriver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# clicking on elements:
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()


# sending keys on the webpage
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# pressing enter after putting query in search bar
# search.send_keys(Keys.TAB)
# search.send_keys("Language")
# search.send_keys(Keys.ENTER)


# filling an example form automatically all by this program
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element_by_name("fName")
fname.send_keys("example")
lname = driver.find_element_by_name("lName")
lname.send_keys("example")
email = driver.find_element_by_name("email")
email.send_keys("example@example.com")
submit_button = driver.find_element_by_xpath("/html/body/form/button")
submit_button.click()


driver.quit()
