from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common import keys
import time

browers = webdriver.Chrome()
browers.get("http://www.oschina.net")

login_bar = browers.find_element_by_id("OSC_Userbar")
alinks = login_bar.find_elements_by_tag_name("a")
login_link = alinks[0]
login_link.click()

login_page = browers.window_handles[-1]
browers.switch_to_window(login_page)
username = login_page.find_element_by_id("f_email")
username.clear()
username.send_keys("duguying2008@gmail.com")
# text.clear()
# text.send_keys("duguying")
# button = browers.find_element_by_id("sb_form_")
# # print button
# button.click()
