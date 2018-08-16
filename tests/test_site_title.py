import pytest

from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_site_title(app):
    site_title = "ATT Nauka - Index page"

    # przejście na stronę główną forum i potwierdzenie zgodności tytułu strony z oczekiwaną wartością
    app.open_home_page()
    assert app.check_site_title(site_title) == site_title