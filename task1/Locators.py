from selenium.webdriver.common.by import By

class Locators:
    POSTFORM_TEXT = (By.ID, "postform-text")
    EXPIRATION_FIELD = (By.ID, "select2-postform-expiration-container")
    EXPIRATION_OPTIONS = (By.XPATH, "//*[@id='select2-postform-expiration-results']/li")
    POSTFORM_NAME = (By.ID, "postform-name")