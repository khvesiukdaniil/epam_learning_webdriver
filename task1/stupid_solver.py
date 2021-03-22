from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://pastebin.com/')

# step 1
postform_text = driver.find_element_by_id('postform-text')
postform_text.send_keys('Hello from WebDriver')

# step 2
expiration_field = driver.find_element_by_id('select2-postform-expiration-container')
expiration_field.click()
expiration_ul = driver.find_element_by_id('select2-postform-expiration-results')
expiration_options = expiration_ul.find_elements_by_tag_name('li')
for option in expiration_options:
    if option.text == '10 Minutes':
        option.click()
        break

# step 3
postform_name = driver.find_element_by_id('postform-name')
postform_name.send_keys('helloweb')
postform_name.submit()


driver.close()