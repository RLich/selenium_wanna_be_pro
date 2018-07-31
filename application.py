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

    def get_username_from_nav_bar(self):
        wd = self.wd
        return wd.find_element_by_id("username_logged_in").text

    def get_login_from_nav_bar(self):
        wd = self.wd
        return wd.find_element_by_xpath("//*[@title='Login']").text

    def logout(self):
        wd = self.wd
        wd.find_element_by_id("username_logged_in").click()
        wd.find_element_by_xpath("//*[@title='Logout']").click()

    def get_site_title(self):
        wd = self.wd
        return wd.title

    def nav_to_first_subforum(self):
        wd = self.wd
        wd.find_element_by_class_name("forumtitle").click()

    def nav_to_subforum_by_href(self):
        wd = self.wd
        wd.find_element_by_css_selector("a[href$='viewforum.php?f=4']").click()

    def enter_subforum_by_name(self, name):
        wd = self.wd
        elements = wd.find_elements_by_class_name('forumtitle')
        for elements[0] in elements:
            if elements[0].text == name:
                elements[0].click()
                break

    def create_new_topic(self, topic_title, topic_text):
        wd = self.wd
        wd.find_element_by_xpath("//*[@title='Post a new topic']").click()
        wd.find_element_by_id("subject").click()
        wd.find_element_by_id("subject").send_keys(topic_title)
        wd.find_element_by_id("message").click()
        wd.find_element_by_id("message").send_keys(topic_text)
        wd.find_element_by_name("post").click()
        wd.find_element_by_id("logo").click()

    def eneter_last_subject(self, topic_title):
        wd = self.wd
        elements = wd.find_element_by_class_name("lastsubject")
        for elements[0] in elements:
            if elements[0].text == topic_title:
                elements[0].click()
                break

    def check_last_subject_name(self, topic_title):
        wd = self.wd
        elements = wd.find_element_by_class_name("lastsubject")
        for elements[0] in elements:
            if elements[0].text == topic_title:
                return elements[0].text


    def topic_cleanup(self):
        wd = self.wd
        wd.find_element_by_class_name("lastsubject").click()
        wd.find_element_by_xpath("//*[@title='Delete post']").click()
        wd.find_element_by_name("delete_permanent").click()
        wd.find_element_by_name("confirm").click()



    def destroy(self):
        self.wd.quit()