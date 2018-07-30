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

elements = driver.find_elements_by_class_name('forumtitle')
for elements[0] in elements:
    if elements[0].text == 'Konrad':
        elements[0].click()
        break
assert driver.find_element_by_class_name('forum-title').text == 'Konrad'
driver.find_element_by_xpath("//*[@title='Post a new topic']").click()
driver.find_element_by_id("subject").click()
driver.find_element_by_id("subject").send_keys("test1")


time.sleep(3)

driver.quit()
