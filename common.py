class Common:
    class SentBox:
        costam = ""

        # app.privmsg.sentbox.metoda

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()

        username_box = wd.find_element_by_name("username")
        username_box.click()
        username_box.send_keys(username)

        password_box = wd.find_element_by_name("password")
        password_box.click()
        password_box.send_keys(password)

        wd.find_element_by_name("login").click()