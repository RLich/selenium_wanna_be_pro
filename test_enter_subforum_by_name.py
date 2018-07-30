from selenium.webdriver.chrome.webdriver import WebDriver
from Config.cfg_att import Config
import time

driver = WebDriver()
driver.get('http://forum.attnauka.webd.pro/index.php')

driver.find_element_by_name("username").click()
driver.find_element_by_name("username").send_keys(Config.username)
driver.find_element_by_name("password").click()
driver.find_element_by_name("password").send_keys(Config.password)
driver.find_element_by_name("login").click()

element = driver.find_elements_by_class_name('forumtitle')
subforum = driver.find_element_by_class_name('forumtitle')
for subforum in element:
    subforum.text == 'Konrad'
    subforum.click()
time.sleep(3)

driver.quit()