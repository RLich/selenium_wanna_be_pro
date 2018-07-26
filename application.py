from selenium.webdriver.chrome.webdriver import WebDriver
from Config.cfg_att import Config


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get(Config.main_url)

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()

        # wpisywanie użytkownika
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").send_keys(username)

        # wpisywanie hasła
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").send_keys(password)

        # zatwierdzenie logowania
        wd.find_element_by_name("login").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_class_name("username").click()


    def destroy(self):
        self.wd.quit()