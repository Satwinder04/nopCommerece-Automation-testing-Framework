import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Type in browser name")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("unsupported browser")

    return driver



def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project nopCommerce'
    config.stash[metadata_key]['Module Name'] = 'Admin Login'
    config.stash[metadata_key]['Tester'] = 'Satwinder Singh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)