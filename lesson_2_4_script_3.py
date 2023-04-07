from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # ждем, пока цена станет $100
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book = browser.find_element(By.XPATH, ".//*[@id='book']")
    book.click()

    # скролл до элемента???

    x_element = browser.find_element(By.XPATH, ".//*[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.XPATH, ".//*[@id='answer']")
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, ".//*[@id='solve']") 
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка в конце    

