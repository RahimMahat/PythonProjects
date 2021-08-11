#!/usr/bin/env python3
from selenium import webdriver

# to use selenium with chrome first download chrome driver compatible to you latest chrome version
webdriver_path = "full_path_to_chromedriver.exe"
driver = webdriver.Chrome(executable_path=webdriver_path)

# getting a price of a particular product from amazon
# driver.get("https://www.amazon.com/SENZER-SG500-Surround-Cancelling-Microphone/dp/B08FX35S7K/ref=pd_pbp13n_hpb_sims_2/142-2739385-9559118?pd_rd_w=1ospq&pf_rd_p=a0aefcc4-048a-468d-a4bb-24a7e1d03f86&pf_rd_r=MR7QMPV92QJX0N3XE1QS&pd_rd_r=ffb0f257-51ac-4a23-b0bc-4436a713f5e2&pd_rd_wg=YdoWi&pd_rd_i=B08FX35S7K&psc=1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)


driver.get("https://www.python.org/")
search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(
#     ".documentation-widget a")
# print(documentation_link.text)

# you can get xpath from inspector click on element and in the copy section you'll get copy xpath
# bug_link = driver.find_element_by_xpath(
#     '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute("href"))

# find multiple elements
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_names[n].text,
    }
print(events)


driver.quit()
