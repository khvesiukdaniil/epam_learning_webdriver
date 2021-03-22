from BasePage import BasePage
from Locators import Locators, By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleCloud(BasePage):

    def search(self, text):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        search_field.send_keys(text)
        search_field.submit()

    def choose_result_by_link_text(self, text):
        result = self.find_element((By.LINK_TEXT, text))
        result.click()
    
    def choose_section_by_title(self, title):
        section = self.find_element((By.XPATH, "//*[@title='{}']".format(title)))
        section.click()

    def enter_number_instances(self, number):
        input_field = self.find_element((By.ID, 'input_65'))
        input_field.send_keys('4')

    def add_gpu(self):
        button = self.find_element((By.XPATH, '//*[@aria-label="Add GPUs"]'))
        button.click()

    def select(self, placeholder, value):
        selection = self.find_element((By.XPATH, '//md-select[@placeholder="{}"]'.format(placeholder)))
        selection.click()
        option = self.find_clickable_element((By.XPATH, "//div[@class='md-select-menu-container md-active md-clickable']//md-option[@value='{}']".format(value)))
        option.click()

    def submit_instances(self):
        input_field = self.find_element((By.ID, 'input_65'))
        input_field.submit()

    def get_estimated_fields(self):
        def select_field(text, i):
            return self.find_element(
                (
                    By.XPATH,
                    "//*[@id='compute']/md-list/md-list-item/div[contains(text(), '{}')]".format(text)
                )
            ).text.split()[i]

        return {
            'expected_vm_class' : select_field('VM class', 2),
            'expected_instance_type' : select_field( 'Instance type', 2),
            'expected_region' : select_field('Region', 1),
            'expected_local_ssd' : select_field('Total available local SSD space', 5),
            'expected_commitment_term' : select_field('Commitment term', 2)
        }

    def total_cost(self):
        return self.find_element((By.XPATH, "//*[contains(text(), 'Total Estimated Cost:')]")).text