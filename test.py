from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'D:\Selenium-GRID\chromedriver.exe')
driver.get('https://google.com')
web_element = driver.find_element_by_name('q')
web_element.send_keys('cheese!')
web_element.submit()
driver.quit() 