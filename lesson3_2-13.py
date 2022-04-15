import unittest
from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Test16_8(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        self.driver = webdriver.Chrome(options=options)
    
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        
        driver = self.driver
        driver.get(link)

        input1 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("Petrov")
        input3 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("av@s.com")

        # Отправляем заполненную форму
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        
        welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        
        driver = self.driver
        driver.get(link)

        input1 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
        input1.send_keys("Ivan")
        input2 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
        input2.send_keys("Petrov")
        input3 = driver.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
        input3.send_keys("av@s.com")

        # Отправляем заполненную форму
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        
        welcome_text_elt = driver.find_element(By.TAG_NAME, 'h1')
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == "__main__":
    unittest.main()