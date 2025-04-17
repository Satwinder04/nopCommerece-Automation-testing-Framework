import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_page import Login_Admin_page


class Test_01_Admin_Login:
    # admin_page_url="https://admin-demo.nopcommerce.com/login"
    admin_page_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username="admin@yourstore.com"
    password="admin"
    invalid_username="adminrendom@yourstore.com"

    def test_title_verification(self,setup):
        self.driver=setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False
    def test_valid_admin_login(self,setup):
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text=self.driver.find_element(By.XPATH,"//h1[normalize-space()='Dashboard']").text
        if act_dashboard_text == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid-admin-login.png")
            self.driver.close()
            assert False 
    
    def test_invalid_admin_login(self,setup):
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message=self.driver.find_element(By.XPATH,'//li').text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid-admin-login.png")
            self.driver.close()
            assert False