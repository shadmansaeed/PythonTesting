#  pytest test_e2eTestFramework.py --browser_name firefox
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# register browser name request


def pytest_addoption(parser):

    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"

    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")
    # chrome driver service
    service_obj = Service()
    if browser_name == "chrome":  # --browser_name firefox
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(10)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
    # driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    yield driver  # Before test function execution
    driver.close()  # post your test function execution

