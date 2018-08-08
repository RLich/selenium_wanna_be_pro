from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import string
import random

from Config.cfg_att import Config
import time


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)

    def open_home_page(self):
        wd = self.wd
        wd.get(Config.main_url)

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()

        usernameBox = wd.find_element_by_name("username")
        usernameBox.click()
        usernameBox.send_keys(username)

        passwordBox = wd.find_element_by_name("password")
        passwordBox.click()
        passwordBox.send_keys(password)

        wd.find_element_by_name("login").click()

    def get_username_from_nav_bar(self):
        wd = self.wd
        return wd.find_element_by_id("username_logged_in").text

    def check_is_login_available(self):
        wd = self.wd
        return wd.find_element_by_xpath("//*[@title='Login']").text == "Login"

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
        subforums = wd.find_elements_by_class_name('forumtitle')
        for subforum in subforums:
            if subforum.text == name:
                subforum.click()
                break

    def create_new_topic(self, topic_title, topic_text):
        wd = self.wd
        wd.find_element_by_xpath("//a[@class='button']").click()
        subjectBox = wd.find_element_by_id("subject")  # trzymaj się nazewnictwa xxx_yyy
        subjectBox.clear()
        subjectBox.send_keys(topic_title)

        messageBox = wd.find_element_by_id("message")  # jak wyzej
        messageBox.clear()
        messageBox.send_keys(topic_text)

        time.sleep(1)
        wd.find_element_by_name("post").click()

    def enter_last_subject(self, topic_title):
        wd = self.wd
        last_subjects = wd.find_element_by_class_name("lastsubject")
        for last_subject in last_subjects:
            if last_subject.text == topic_title:
                last_subject.click()
                break

    def check_title_in_topic_titles(self, topic_title):
        wd = self.wd
        topic_titles = wd.find_elements_by_class_name("topictitle")
        for title in topic_titles:
            if title.text == topic_title:
                return True
        return False

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

    def search_by_title(self, topic_title):
        wd = self.wd
        searchBox = wd.find_element_by_id("keywords")
        searchBox.clear()
        searchBox.send_keys(topic_title)
        wd.find_element_by_xpath("//*[@title='Search']").click()

    def post_a_reply(self, reply):
        wd = self.wd
        wd.find_element_by_xpath("//*[@title='Post a reply']").click()

        messageBox = wd.find_element_by_id("message")
        messageBox.clear()
        messageBox.send_keys(reply)

        time.sleep(2)
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
            if "Private messages" in element.text:
                element.click()
                break

    def send_private_message(self, temat_wiadomosci, tresc_wiadomosci):
        wd = self.wd
        wait = self.waiter(wd)
        wd.find_element_by_css_selector("[accesskey='n']").click()

        usernameBox = wd.find_element_by_id("username_list")
        usernameBox.clear()
        usernameBox.send_keys(Config.username2)
        wd.find_element_by_name("add_to").click()

        subjectBox = wd.find_element_by_id("subject")
        subjectBox.clear()
        subjectBox.send_keys(temat_wiadomosci)

        messageBox = wd.find_element_by_id("message")
        messageBox.clear()
        messageBox.send_keys(tresc_wiadomosci)

        time.sleep(2)
        wd.find_element_by_css_selector(".default-submit-action").click()
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'message-title')))

    def waiter(self, wd):
        wait = WebDriverWait(wd, 10)
        return wait

    def check_received_message(self, temat_wiadomosci):
        wd = self.wd
        topics = wd.find_elements_by_class_name("topictitle")
        for topic in topics:
            if topic.text == temat_wiadomosci:
                return True
        return False

    def enter_outbox(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "span")))
        priv_messages_tabs = wd.find_elements_by_tag_name("span")
        for priv_messages_tab in priv_messages_tabs:
            if priv_messages_tab.text == "Outbox":
                priv_messages_tab.click()
                break

    def enter_outbox_from_newly_sent_message(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "arrow-left")))
        wd.find_element_by_class_name("arrow-left").click()

    def enter_sent_messages(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "span")))
        mail_tabs = wd.find_elements_by_tag_name("span")
        for mail_tab in mail_tabs:
            if mail_tab.text == "Sent messages":
                mail_tab.click()
                break

    def check_subforum_name(self, name_of_subforum):
        wd = self.wd
        return wd.find_element_by_class_name('forum-title').text == name_of_subforum

    def get_sent_message_title(self, temat_wiadomosci):
        wd = self.wd
        topics = wd.find_elements_by_class_name("topictitle")
        for topic in topics:
            if topic.text == temat_wiadomosci:
                return True
        return False

    def assert_if_user_in_private_messeges(self):
        wd = self.wd
        return wd.find_element_by_css_selector("li.activetab").text == "Private messages"

    def assert_if_user_redirected_to_message_in_outbox(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "arrow-left")))
        return wd.find_element_by_class_name("arrow-left").text == 'Return to “Outbox”'

    def get_message_confirmation_window_title(self):
        wd = self.wd
        return wd.find_element_by_class_name("message-title").text == "Information"

    def random_string(self, max_len):
        symbols = string.ascii_letters + string.digits + " " + string.punctuation
        return "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

    def check_highlighted_topic_title(self):
        wd = self.wd
        return wd.find_element_by_css_selector(".posthilit").text == "Unikalny"

    def destroy(self):
        self.wd.quit()
