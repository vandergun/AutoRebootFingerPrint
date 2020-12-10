from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"D:\PySe\chromedriver.exe") #location of chrome webdriver
browser.get("http://1A.B.C.D/") # URL of finger print devices
browser.set_page_load_timeout(5)
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td[3]/input').send_keys("282") #Enter username
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[3]/td[3]/input').send_keys("1207") #Enter password
browser.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[5]/td/input[1]').click() #click login
browser.get("http://A.B.C.D/form/Device") #Goto URL of reboot.
