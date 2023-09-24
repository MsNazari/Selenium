from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")

click_cookies = driver.find_element('xpath', ('//*[@id="L2AGLb"]'))
click_cookies.click()
search_field = driver.find_element('name', 'q')
search_field.send_keys("keep it simple stupid")
