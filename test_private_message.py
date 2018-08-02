import pytest
from application import Application
from Config.cfg_att import Config
import time


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_private_message(app):
    app.login(Config.username1, Config.password1)
    app.wd.find_element_by_xpath("//*[@role='menuitem']").click()
    app.wd.find_element_by_class_name("rightside"[1])
    time.sleep(1)
