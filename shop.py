[]######################## Отображение страницы товара #########################
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
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# HTML = driver.find_element_by_css_selector(".post-181 :nth-child(2)").click()
# HTML5 = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title"), "HTML5 Forms"))
# print(HTML5)
[]####################### Количество товаров в категории #######################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# Account = driver.find_element_by_id("menu-item-50").click()
# log_email= driver.find_element_by_id("username")
# log_email.send_keys("123g@mail.ru")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("Alek$123A!")
# Login = driver.find_element_by_css_selector("[value=Login]").click()
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# HTML = driver.find_element_by_css_selector(".product-categories :nth-child(2)>a").click()
# post = driver.find_elements_by_class_name("product-type-simple")
# if len(post) == 3:
#      print("Отображается 3 товара")
# else:
#      print("Ошибка. Количество товаров : " + str(len(post)))
# driver.quit()
[]####################### Сортировка товаров ###################################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# Account = driver.find_element_by_id("menu-item-50").click()
# log_email= driver.find_element_by_id("username")
# log_email.send_keys("123g@mail.ru")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("Alek$123A!")
# Login = driver.find_element_by_css_selector("[value=Login]").click()
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# ######### Проверка селектора по умолчанию
# menu_order= driver.find_element_by_css_selector("option[value=menu_order]")
# menu_order_selected =menu_order .get_attribute("selected")
# print(menu_order_selected)
# if menu_order_selected is None:
#      print("Default sorting no")
# else:
#      print("the default sorting is selecte сотировка по умолчанию выбрана ")
# driver.find_element_by_tag_name("select").click()
# driver.find_element_by_css_selector("option:nth-child(6)").click()
# ############ Проверка селектора от большей цены к меньшей
# price_desc= driver.find_element_by_css_selector("option[value=price-desc]")
# price_desc_selected = price_desc.get_attribute("selected")
# print(price_desc_selected)
# if menu_order_selected is None:
#      print("Error. No price high to low")
# else:
#      print("Price от большей к меньшей ")
# driver.quit()
[]####################### Отображение, скидка товара ###########################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# wait = WebDriverWait(driver, 20)
# driver.get("http://practice.automationtesting.in/")
# Account = driver.find_element_by_id("menu-item-50").click()
# log_email= driver.find_element_by_id("username")
# log_email.send_keys("123g@mail.ru")
# log_password = driver.find_element_by_id("password")
# log_password.send_keys("Alek$123A!")
# Login = driver.find_element_by_css_selector("[value=Login]").click()
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# Android=driver.find_element_by_css_selector(".wp-post-image:nth-child(2)").click()
# ########### проверка cтарой цены  ########################
# oldprice = driver.find_element_by_class_name("price")
# oldprice_get_text = oldprice.text
# assert "600.00" in oldprice_get_text
# print("старая цена ₹600.00")
# ########### проверка новой цены ###########################
# newprice = driver.find_element_by_class_name("price")
# newprice_get_text = newprice.text
# assert "450.00" in newprice_get_text
# print("новая цена ₹450.00")
# ############ явное ожидание на предпросмотр обложки ########
# img = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wp-post-image"))).click()
# ############ закрытие предпросмотра ########################
# close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
[]######################## Проверка цены в корзине #############################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# driver.get("http://practice.automationtesting.in/")
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# driver.execute_script("window.scrollBy(0, 400);")
# tobasket = driver.find_element_by_css_selector(".post-182>:nth-child(2)").click()
# ############### проверка количества товаров ##########
# time.sleep(3)
# item= driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
# item_get_text = item.text
# assert item_get_text == "1 Item"
# print("В корзине один товар")
# # # ############### проверка цены #######################
# time.sleep(3)
# cost= driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# cost_get_text = cost.text
# assert cost_get_text == "₹180.00"
# print("Стоимость товара ₹180.00")
# time.sleep(2)
# basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# ############# проверка на отображение стоимости subtotal ###########
# subtotal = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))
# print(subtotal)
# ############# проверка на отображение стоимости total ##############
# total = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "₹189.00"))
# print(total)
[]######################## Работа в корзине ####################################
# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# driver.execute_script("window.scrollBy(0, 400);")
# book1 = driver.find_element_by_css_selector(".post-182>:nth-child(2)").click()
# driver.execute_script("window.scrollBy(0, 400);")
# time.sleep(2)
# book2 = driver.find_element_by_css_selector(".post-180>:nth-child(2)").click()
# time.sleep(1)
# basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# time.sleep(2)
# remove1 = driver.find_element_by_css_selector(".cart_item:nth-child(1) .remove").click()
# time.sleep(2)
# Undo=driver.find_element_by_css_selector(".woocommerce-message :nth-child(1)")
# Undo.click()
# quantity=driver.find_element_by_css_selector(".cart_item:nth-child(1) .input-text.qty.text")
# quantity.clear()
# quantity.send_keys("3")
# Update_Basket = driver.find_element_by_css_selector("[name=update_cart]").click()
# quantity_field = driver.find_element_by_css_selector(".cart_item:nth-child(1) .input-text.qty.text")
# quantity_field_value = quantity_field.get_attribute("value")
# assert quantity_field_value == '3'
# print("Количество товара (JS Data Structures and Algorithm) = 3")
# time.sleep(3)
# apply_coupon = driver.find_element_by_css_selector("[name=apply_coupon]")
# apply_coupon.click()
# time.sleep(2)
# error_coupon_code = driver.find_element_by_css_selector("ul.woocommerce-error")
# error_coupon_code_text = error_coupon_code.text
# assert error_coupon_code_text == 'Please enter a coupon code.'
# print("Текст в элементе найден")
[]######################## Покупка товара ######################################
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
# Shop = driver.find_element_by_css_selector("#menu-item-40>:nth-child(1)").click()
# driver.execute_script("window.scrollBy(0, 400);")
# book1 = driver.find_element_by_css_selector(".post-182>:nth-child(2)").click()
# time.sleep(3)
# basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
# time.sleep(2)
# checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))).click()
# ########################## Заполнение полей данных #####################
# first_name = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys("Simon")
# time.sleep(3)
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Tanner")
# time.sleep(3)
# ######################### Данные о адресе ############################
# Email= driver.find_element_by_id("billing_email")
# Email.send_keys("djl@mail.ru")
# phone= driver.find_element_by_id("billing_phone")
# phone.send_keys("398747765738")
# time.sleep(3)
# Country= driver.find_element_by_class_name("select2-arrow").click()
# Country1= driver.find_element_by_id("s2id_autogen1_search")
# Country1.send_keys("Zimbabwe")
# Country2= driver.find_element_by_class_name("select2-results-dept-0").click()
# time.sleep(3)
# Address= driver.find_element_by_css_selector("[name=billing_address_1]")
# Address.send_keys("Sam Nujoma Street (2nd St. Extension)")
# City= driver.find_element_by_id("billing_city")
# City.send_keys("Harare")
# time.sleep(2)
# state= driver.find_element_by_id("billing_state")
# state.send_keys("is unknown")
# ######################## Оплата #######################################
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# radio_btn = driver.find_element_by_id("payment_method_cheque").click()
# time.sleep(2)
# place_order= driver.find_element_by_id("place_order").click()
# ####################### Явные ожидания ################################
# time.sleep(2)
# thankyou = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# print(thankyou)
# method= wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details :nth-child(3)>td"), "Check Payments"))
# print(method)






