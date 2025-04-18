import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_page import Login_Admin_page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import XLUtils
import time

class Test_02_Admin_Login_Data_Driven:
    # admin_page_url="https://admin-demo.nopcommerce.com/login"
    admin_page_url=Read_Config.get_admin_page_url()

    logger=Log_Maker.log_gen()
    path=".\\test_data\\admin_login_data.xlsx"
    status_list=[]
    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("***************test_valid_admin_login_data_driven_started************************")
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp=Login_Admin_page(self.driver)
        
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows in excel:",self.rows)


        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp_login=XLUtils.readData(self.path,"Sheet1",r,3)

            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)
            act_title =self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp_login=="yes":
                    self.logger.info("***************test_valid_admin_login_data_driven passed************************")
                    XLUtils.writeData(self.path,"Sheet1",r,4,"Passed")
                    XLUtils.fillGreenColor(self.path,"Sheet1",r,4)
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.exp_login=="no":
                    self.logger.info("***************test_valid_admin_login_data_driven failed************************")
                    XLUtils.writeData(self.path,"Sheet1",r,4,"Failed")
                    XLUtils.fillRedColor(self.path,"Sheet1",r,4)
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()
            elif act_title!=exp_title:
                if self.exp_login=="yes":
                    self.logger.info("***************test_valid_admin_login_data_driven failed************************")
                    XLUtils.writeData(self.path,"Sheet1",r,4,"Failed")
                    XLUtils.fillRedColor(self.path,"Sheet1",r,4)
                    self.status_list.append("Fail")
                elif self.exp_login=="no":
                    self.logger.info("***************test_valid_admin_login_data_driven passed************************")
                    XLUtils.writeData(self.path,"Sheet1",r,4,"Passed")
                    XLUtils.fillGreenColor(self.path,"Sheet1",r,4)
                    self.status_list.append("Pass")
        
        print("Status list:",self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("***************test_valid_admin_login_data_driven failed************************")
            assert False
        else:
            self.logger.info("***************test_valid_admin_login_data_driven passed************************")
            assert True
            self.driver.close()