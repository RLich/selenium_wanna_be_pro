from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

driver = WebDriver()
driver.get("http://forum.attnauka.webd.pro/index")
assert driver.title == "ATT Nauka - Index page"

driver.quit()