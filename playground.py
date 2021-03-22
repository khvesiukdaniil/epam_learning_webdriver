from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
driver.get("http://stackoverflow.com")

# Open a new window
driver.execute_script("window.open('');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.reddit.com/")
# close the active tab
driver.close()

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])
driver.get("https://bing.com")

# Close the only tab, will also close the browser.
driver.close()