import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_earch_by_title(app):
    app.login(Config.username, Config.password)
    app.search_by_title()
    assert app.wd.find_element_by_css_selector(".posthilit").text == "test"