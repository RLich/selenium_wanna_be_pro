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
        wd.find_element_by_id("logo")
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
        wd.find_element_by_xpath("//*[@title='Marcin']").click()
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


    def enter_private_messages(self):
        wd = self.wd
        elements = wd.find_elements_by_css_selector("[role='menuitem']")
        for element in elements:
            if element.text.__contains__("Private messages"):
                element.click()
                break

    def send_private_message(self, temat_wiadomosci, tresc_wiadomosci):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[title='Compose message']")))
        wd.find_element_by_css_selector("[title='Compose message']").click()
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "username_list")))
        wd.find_element_by_id("username_list").clear()
        wd.find_element_by_id("username_list").send_keys(Config.username2)
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "add_to")))
        wd.find_element_by_name("add_to").click()
        time.sleep(1)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "subject")))
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys(temat_wiadomosci)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(tresc_wiadomosci)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[value='Submit']")))
        wd.find_element_by_css_selector("[value='Submit']").click()

    def assert_received_message(self, temat_wiadomosci):
        wd = self.wd
        wd.find_element_by_id("active-subsection").click()
        elements = wd.find_elements_by_class_name("topictitle")
        for element in elements:
            if element.text == temat_wiadomosci:
                return element.text

    def enter_outbox(self):
        wd = self.wd
        elements = wd.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == "Outbox":
                element.click()
                break

    def enter_sent_messages(self):
        wd = self.wd
        elements = wd.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == "Sent messages":
                element.click()
                break

    def assert_sent_message(self, temat_wiadomosci):
        wd = self.wd
        wait = WebDriverWait(wd, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "active-subsection")))
        elements = wd.find_elements_by_class_name("topictitle")
        for element in elements:
            if element.text == temat_wiadomosci:
                return element.text

    def assert_if_user_in_private_messeges(self):
        wd = self.wd
        return wd.find_element_by_css_selector("[title='Compose message']").text


    def destroy(self):
        self.wd.quit()
