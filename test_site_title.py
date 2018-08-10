import pytest

from pages.application import Application


# jest okejka!
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_site_title(app):
    app.open_home_page()
    assert app.wd.title == "ATT Nauka - Index page"