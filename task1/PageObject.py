from BasePage import BasePage
from Locators import Locators

class InputHelper(BasePage):
    
    def enter_text(self, text):
        postform_text = self.find_element(Locators.POSTFORM_TEXT)
        postform_text.send_keys(text)
        return postform_text

    def choose_expiration_option_with_text(self, text):
        expiration_field = self.find_element(Locators.EXPIRATION_FIELD)
        expiration_field.click()
        expiration_options = self.find_elements(Locators.EXPIRATION_OPTIONS)
        for option in expiration_options:
            if option.text == text:
                return option.click()

    def enter_title(self, text):
        postform_name = self.find_element(Locators.POSTFORM_NAME)
        postform_name.send_keys(text)
        return postform_name

    def submit(self):
        postform_text = self.find_element(Locators.POSTFORM_TEXT)
        postform_text.submit()
        return self.driver.current_url