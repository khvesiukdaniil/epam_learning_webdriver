from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    timeout=100000

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator,time=timeout):
        return WebDriverWait(
            self.driver,time).until(EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_clickable_element(self, locator,time=timeout):
        return WebDriverWait(
            self.driver,time).until(EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=timeout):
        return WebDriverWait(
            self.driver,time).until(EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def switch_to_frame_by_locator(self, locator, time=timeout):
        frame = WebDriverWait(
            self.driver,time).until(EC.presence_of_element_located(locator),
            message=f"Can't find elements by locator {locator}")
        
        return self.driver.switch_to.frame(frame)

    def switch_to_parent_frame(self):
        return self.driver.switch_to.parent_frame()

    def open(self):
        return self.driver.get(self.base_url)