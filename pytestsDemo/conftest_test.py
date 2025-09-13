import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    print("user profile data is being created")
    return request.param