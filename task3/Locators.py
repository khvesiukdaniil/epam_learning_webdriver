from selenium.webdriver.common.by import By

class Locators:
    SEARCH_FIELD = (By.NAME, "q")
    DEFAULT_FRAME = (By.TAG_NAME, "iframe")