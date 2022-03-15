import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVERS = r"C:\drivers"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="http://localhost")


def driver_factory(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = False
        service = Service(executable_path=DRIVERS + '/chromedriver')
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=DRIVERS + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=DRIVERS + "/operadriver")
    else:
        raise Exception("Driver not supported")
    return driver


@pytest.fixture
def browser(request):
    url = request.config.getoption("--url")
    driver = driver_factory(request)
    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.url = url
    return driver

