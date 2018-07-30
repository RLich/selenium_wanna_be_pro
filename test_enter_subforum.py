from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()
driver.get('http://forum.attnauka.webd.pro/index.php')
element = driver.find_element_by_class_name('forumtitle')

element_text = element.text

print (element_text)
driver.quit()