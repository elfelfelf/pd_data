from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

def login(portal):
	driver.get(portal)

	driver.find_element_by_name("j_username").send_keys(userName)
	driver.find_element_by_name("j_password").send_keys(passName)
	driver.find_element_by_name('submit').click()
