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

        username_box = wd.find_element_by_name("username")
        username_box.click()
        username_box.send_keys(username)

        password_box = wd.find_element_by_name("password")
        password_box.click()
        password_box.send_keys(password)

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
        subject_box = wd.find_element_by_id("subject")
        subject_box.clear()
        subject_box.send_keys(topic_title)

        message_box = wd.find_element_by_id("message")
        message_box.clear()
        message_box.send_keys(topic_text)

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
        search_box = wd.find_element_by_id("keywords")
        search_box.clear()
        search_box.send_keys(topic_title)
        wd.find_element_by_xpath("//*[@title='Search']").click()

    def post_a_reply(self, reply):
        wd = self.wd
        wd.find_element_by_xpath("//*[@title='Post a reply']").click()

        message_box = wd.find_element_by_id("message")
        message_box.clear()
        message_box.send_keys(reply)

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
        wd.find_element_by_id("nav-main").find_element_by_partial_link_text("Private messages").click()

    def send_private_message(self, temat_wiadomosci, tresc_wiadomosci):
        wd = self.wd
        wait = self.waiter(wd)
        wd.find_element_by_css_selector("[accesskey='n']").click()

        username_box = wd.find_element_by_id("username_list")
        username_box.clear()
        username_box.send_keys(Config.username2)
        wd.find_element_by_name("add_to").click()

        subject_box = wd.find_element_by_id("subject")
        subject_box.clear()
        subject_box.send_keys(temat_wiadomosci)

        message_box = wd.find_element_by_id("message")
        message_box.clear()
        message_box.send_keys(tresc_wiadomosci)

        time.sleep(2)
        wd.find_element_by_css_selector(".default-submit-action").click()
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "message-title")))
    def waiter(self, wd):
        wait = WebDriverWait(wd, 10)
        return wait

    def check_message_title(self, temat_wiadomosci):
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
            if "Outbox" in priv_messages_tab.text:
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

    def assert_if_user_in_private_messeges(self):
        wd = self.wd
        return wd.find_element_by_css_selector("li.activetab").text == "Private messages"

    def check_if_user_has_opened_newly_sent_message_in_outbox(self):
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

    def title_counter_before(self, temat_wiadomosci):
        wd = self.wd
        titles = wd.find_elements_by_class_name("topictitle")
        wanted_titles_before = []
        for title in titles:
            if title.text == temat_wiadomosci:
                wanted_titles_before.append(title)
        return wanted_titles_before

    def title_counter_after(self,temat_wiadomosci):
        wd = self.wd
        titles = wd.find_elements_by_class_name("topictitle")
        wanted_titles_after = []
        for title in titles:
            if title.text == temat_wiadomosci:
                wanted_titles_after.append(title)
        return wanted_titles_after

    def destroy(self):
        self.wd.quit()
