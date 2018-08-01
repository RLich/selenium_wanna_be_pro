from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from Config.cfg_att import Config
import time


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
        for user in elements:
            if user.text == name:
                user.click()
                break

    def create_new_topic(self, topic_title, topic_text):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_xpath("//*[@title='Post a new topic']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "subject")))
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys(topic_title)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(topic_text)
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "post")))
        wd.find_element_by_name("post").click()

    def enter_last_subject(self, topic_title):
        wd = self.wd
        elements = wd.find_element_by_class_name("lastsubject")
        for topics in elements:
            if topics.text == topic_title:
                topics.click()
                break

    def get_name_of_topic_title(self, topic_title):
        wd = self.wd
        elements = wd.find_elements_by_class_name("topictitle")
        for topic in elements:
            if topic.text == topic_title:
                return topic.text

    def topic_cleanup(self, topic_title):
        wd = self.wd
        elements = wd.find_elements_by_class_name("topictitle")
        for topic in elements:
            if topic.text == topic_title:
                topic.click()
                break
        wd.find_element_by_xpath("//*[@title='Delete post']").click()
        wd.find_element_by_name("delete_permanent").click()
        wd.find_element_by_name("confirm").click()

    def search_by_title(self):
        wd = self.wd
        wd.find_element_by_id("keywords").clear()
                                        # clear()
        wd.find_element_by_id("keywords").send_keys("test")
        wd.find_element_by_xpath("//*[@title='Search']").click()

    def post_a_reply(self, reply):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wd.find_element_by_xpath("//*[@title='Post a reply']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(reply)
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "post")))
        wd.find_element_by_name("post").click()

    def get_post_content(self, reply):
        wd = self.wd
        elements = wd.find_elements_by_class_name("content")
        for post in elements:
            if post.text == reply:
                return post.text

    def post_and_topic_cleanup(self):
        wd = self.wd
        wd.find_element_by_xpath("//*[@title='Delete post']").click()
        wd.find_element_by_name("delete_permanent").click()
        wd.find_element_by_name("confirm").click()
        time.sleep(3)
        wd.find_element_by_xpath("//*[@title='Delete post']").click()
        wd.find_element_by_name("delete_permanent").click()
        wd.find_element_by_name("confirm").click()

    def destroy(self):
        self.wd.quit()
