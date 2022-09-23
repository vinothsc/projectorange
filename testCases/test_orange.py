from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.Login_page import Login
from pageObjects.Login_page import account
from pageObjects.Login_page import Admincheck
import time


class Test_orange:
    baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username="Admin"
    password="admin123"
    fname='vinoth'
    mname='m'
    lname='vicky'
    Nusername="vinoth010"
    Npassword="Qwerty@1"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        login_page_obj=Login(self.driver)
        login_page_obj.set_username(self.username)
        login_page_obj.set_password(self.password)
        login_page_obj.click_login()


   # def test_add_profile(self,setup):
       # Test_orange().test_login()
        account_obj=account(self.driver) #### creat account class object
        account_obj.namefill()
        #account_obj.click_empsave()
        time.sleep(2)
        account_obj.checkbox_click()
        time.sleep(3)
        account_obj.logindetails(self.Nusername,self.Npassword)
        time.sleep(2)


        admin_obj=Admincheck(self.driver)  ####creat admin class object
        admin_obj.click_admin()
        admin_obj.check_user_name(self.Nusername)
        admin_obj.click_namesearch(self.Nusername)
       # admin_obj.log_out_one()
        #admin_obj.log_out_two()
        login_page_obj.set_username(self.Nusername)
        login_page_obj.set_password(self.Npassword)
        login_page_obj.click_login()

















