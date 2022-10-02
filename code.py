#1st Automation script

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe" #path location on desktop
driver = webdriver.Chrome(PATH)

driver.get("http://www.google.com/") #Enter your url destination

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element("name", "q")

search_box.send_keys('Happy Working') #Enter words you gonna search in google search bar

search_box.submit()

driver.get("https://www.sederet.com/tutorial/selamat-bekerja-dalam-bahasa-inggris/")
time.sleep(5) # Let the user actually see something!

#menu = driver.find_element("ID", "menu_container")
#hidden_submenu = driver.find_element("LINK_TEXT", "https://www.sederet.com/tutorial/listening/")

#ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

driver.quit()
