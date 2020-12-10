from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"D:\PySe\chromedriver.exe")
browser.get("http://192.168.81.11/")
browser.set_page_load_timeout(5)
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td[3]/input').send_keys("282")
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[3]/td[3]/input').send_keys("1207")
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[5]/td/input[1]').click()
browser.get("http://192.168.81.11/form/Device")
