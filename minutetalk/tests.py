from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NewLogin2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_login2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('MinuteTalk! It', \"'\", 's time for a Mini Talk!')])[1]/following::div[1]").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("jerome")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("12345678")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign Up'])[1]/following::div[2]").click()
        time.sleep(5)
        self.assertEqual(driver.find_element_by_xpath("//h1").text, "FEATURED CHANNELS")

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

class Advertise(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_advertise(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Go Talk!'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[2]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[2]").send_keys("earl's fanclub")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").send_keys("https://www.youtube.com/channel/UCaPPe8Yauw2A14wR_EZl7TA")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("All about Earl")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::div[6]").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Jerome Requioma")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("9999 - 9999 - 9999 - 9999")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Feb'])[1]/preceding::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Feb'])[1]/preceding::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[4]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[4]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[4]").send_keys("799")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[5]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Accepted Cards'])[1]/following::input[5]").send_keys("jessa.mae45@yahoo.com")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::div[15]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").clear()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select an image'])[1]/following::input[3]").send_keys("https://www.youtube.com")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[2]/following::div[1]").click()
        self.assertEqual(driver.find_element_by_xpath("//h1").text, "Need to reach an audience? We can do that for you!")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_signup(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('MinuteTalk! It', \"'\", 's time for a Mini Talk!')])[1]/following::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::div[7]").click()
        driver.find_element_by_name("first_name").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Tim")
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("Paler")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("timpaler@gmail.com")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("12345678")
        driver.find_element_by_id("cpassword").click()
        driver.find_element_by_id("cpassword").clear()
        driver.find_element_by_id("cpassword").send_keys("12345678")
        driver.find_element_by_id("age").click()
        driver.find_element_by_id("age").clear()
        driver.find_element_by_id("age").send_keys("20")
        driver.find_element_by_name("gender").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Female'])[1]/preceding::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Age'])[1]/following::div[18]").click()
        time.sleep(5)
        self.assertEqual(driver.find_element_by_xpath("//h1").text, "MinuteTalk! It's time for a Mini Talk!")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
class UserNav2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_user_nav2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('MinuteTalk! It', \"'\", 's time for a Mini Talk!')])[1]/following::div[1]").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("12345678")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign Up'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Featured Channels'])[1]/following::div[7]").click()
        time.sleep(1)
        self.assertEqual(driver.find_element_by_xpath("//p").text, "Filter")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

class EditProf2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_edit_prof2(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)=concat('MinuteTalk! It', \"'\", 's time for a Mini Talk!')])[1]/following::div[1]").click()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("root")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("12345678")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign Up'])[1]/following::div[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='MY CHANNELS'])[1]/following::img[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Male, 20'])[1]/following::div[5]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='EDIT PROFILE'])[1]/following::i[1]").click()
        driver.find_element_by_name("first_name").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("Tim")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Age'])[1]/following::div[18]").click()
        driver.find_element_by_name("editform_pass").click()
        driver.find_element_by_name("editform_pass").clear()
        driver.find_element_by_name("editform_pass").send_keys("12345678")
        driver.find_element_by_name("editform_pass").send_keys(Keys.ENTER)
        self.assertEqual(driver.find_element_by_xpath("//h1").text, "FEATURED CHANNELS")
        time.sleep(3)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
