[]###################  Регистрация аккаунта #############################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# wait=WebDriverWait(driver, 60)
# driver.get("http://practice.automationtesting.in/")
# Account = driver.find_element_by_id("menu-item-50").click()
# reg_email= driver.find_element_by_id("reg_email")
# reg_email.send_keys("123g@mail.ru")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("Alek$123A!")
# Register = driver.find_element_by_css_selector("[value=Register]").click()
# Register1= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[value=Register]"))).click()
# driver.quit()
[] #################   Логин в систему  ##################################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# wait = WebDriverWait(driver, 5)
# driver.get("http://practice.automationtesting.in/")
# Account = driver.find_element_by_id("menu-item-50").click()
# log_email= driver.find_element_by_id("username")
# log_email.send_keys("123g@mail.ru")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("Alek$123A!")
# Login = driver.find_element_by_css_selector("[value=Login]").click()
# Logout= wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "html.js.csstransitions"), "Logout"))
# print(Logout)
