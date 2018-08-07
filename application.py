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

        # wpisywanie użytkownika
        usernameBox = wd.find_element_by_name("username")
        usernameBox.click()
        usernameBox.send_keys(username)

        # wpisywanie hasła
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").send_keys(password)

        # zatwierdzenie logowania
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
        wait = self.waiter(wd)
        wd.find_element_by_xpath("//a[@class='button']").click()
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys(topic_title)
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(topic_text)
        time.sleep(1)
        wd.find_element_by_name("post").click()

    def enter_last_subject(self, topic_title):
        wd = self.wd
        elements = wd.find_element_by_class_name("lastsubject")
        for topics in elements:
            if topics.text == topic_title:
                topics.click()
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

    def search_by_title(self):
        wd = self.wd
        wd.find_element_by_id("keywords").clear()
        wd.find_element_by_id("keywords").send_keys("test")
        wd.find_element_by_xpath("//*[@title='Search']").click()

    def post_a_reply(self, reply):
        wd = self.wd
        wait = self.waiter(wd)
        wd.find_element_by_xpath("//*[@title='Post a reply']").click()
        time.sleep(1)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
        wd.find_element_by_id("message").clear()
        wd.find_element_by_id("message").send_keys(reply)
        time.sleep(1)
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, "post")))
        time.sleep(1)
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
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[title='Compose message']")))
        wd.find_element_by_css_selector("[title='Compose message']").click() ### sadsad
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "username_list")))
        wd.find_element_by_id("username_list").clear()
        wd.find_element_by_id("username_list").send_keys(Config.username2)
        # wait.until(expected_conditions.visibility_of_element_located((By.NAME, "add_to")))

        wd.find_element_by_name("add_to").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "subject")))
        wd.find_element_by_id("subject").clear()
        wd.find_element_by_id("subject").send_keys(temat_wiadomosci)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
        wd.find_element_by_id("message").clear()

        wd.find_element_by_id("message").send_keys(tresc_wiadomosci)
        # time.sleep(100)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".default-submit-action")))
        # wd.find_element_by_id("postform").submit()
        wd.find_element_by_css_selector(".default-submit-action").click()
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'message-title')))

    def waiter(self, wd):
        wait = WebDriverWait(wd, 10)
        return wait

    def assert_received_message(self, temat_wiadomosci):
        wd = self.wd
        # wd.find_element_by_id("active-subsection").click()
        elements = wd.find_elements_by_class_name("topictitle")
        for element in elements:
            if element.text == temat_wiadomosci:
                return element.text

    def enter_outbox(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "span")))
        elements = wd.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == "Outbox":
                element.click()
                break

    def enter_outbox_from_newly_sent_message(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "active-subsection")))
        wd.find_element_by_class_name("active-subsection").click()


    def enter_sent_messages(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "span")))
        elements = wd.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == "Sent messages":
                element.click()
                break
# kutang nazewnictwa -> medal cebulandii

    def check_subforum_name(self, name_of_subforum):
        wd = self.wd
        return wd.find_element_by_class_name('forum-title').text == name_of_subforum


    def assert_sent_message(self, temat_wiadomosci):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "active-subsection")))
        elements = wd.find_elements_by_class_name("topictitle")
        for element in elements:
            if element.text == temat_wiadomosci:
                return element.text

    def assert_if_user_in_private_messeges(self):
        wd = self.wd
        return wd.find_element_by_css_selector("[title='Compose message']").text

    def assert_if_user_redirected_to_sent_message(self):
        wd = self.wd
        wait = self.waiter(wd)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "arrow-left")))
        return wd.find_element_by_class_name("arrow-left").text

    def assert_if_information_window_present(self):
        wd = self.wd
        return wd.find_element_by_class_name("message-title").text

    def random_string(self, max_len):
        prefix = "test "
        symbols = string.ascii_letters + string.digits + " " + string.punctuation
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])




    def destroy(self):
        self.wd.quit()
