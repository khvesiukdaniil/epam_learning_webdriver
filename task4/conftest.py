import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_rect(0, 0, 1000, 1000)
    yield driver
    driver.quit()