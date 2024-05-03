from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class LoginTest(LiveServerTestCase):

    def test_home_page(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get("http://localhost:8000/")
        assert "Home Page" in driver.page_source
    
    def test_login_page(self):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get("http://localhost:8000/login/")

        time.sleep(3)

        user_name = driver.find_element(by="id", value="id_username")
        user_pass = driver.find_element(by="id", value="id_password")
        submit_button = driver.find_element(by="id", value="submit")

        user_name.send_keys("evgen")
        user_pass.send_keys("evgen")
        submit_button.send_keys(Keys.RETURN)

        time.sleep(2)

        assert "Catalog" in driver.page_source

