import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pytest_html import extras
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
driver = None
@pytest.fixture(scope = "class")


def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path="/Users/maximnudler/Desktop/selenium/chromedriver")
    actions = ActionChains(driver)
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/angularpractice')
    request.cls.driver = driver
    yield
    driver.close()

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome")
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
    # driver.get_screenshot_as_file(name)