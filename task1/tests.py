from PageObject import InputHelper

def test_task1(browser):
    page = InputHelper(browser)
    page.go_to_site()
    page.enter_text("Hello from WebDriver")
    page.choose_expiration_option_with_text("10 Minutes")
    page.enter_title("helloweb")
    page.submit()