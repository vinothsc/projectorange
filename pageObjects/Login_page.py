import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Login:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//*[@type='submit']"


    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        self.driver.save_screenshot("C:\\Users\\vinothsc\\PycharmProjects\\projectorange\\screenshots\\image.png")

class account:
    button_add_xpath="//*[text()='Add Employee']"
    textbox_fname_name="firstName"
    textbox_mname_name = "middleName"
    textbox_lname_name = "lastName"
    #button_save_xpath = "//button[@type='submit']"
    checkbox_addinfo_xpath="//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
    textbox_uname_xpath="//*[text()='Username']/../..//*[@class='oxd-input oxd-input--active']"
    textbox_password_xpath="//*[text()='Password']/../..//*[@type='password']"
    textbox_confpassword_xpath="//*[text()='Confirm Password']/../..//*[@type='password']"
    button_saveinfo_xpath="//*[text()=' * Required']/..//*[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def namefill(self):
        self.driver.find_element(By.XPATH,self.button_add_xpath).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME,self.textbox_fname_name).send_keys('vinoth')
        self.driver.find_element(By.NAME, self.textbox_mname_name).send_keys('mname')
        self.driver.find_element(By.NAME, self.textbox_lname_name).send_keys('lname')

    def checkbox_click(self):
        self.driver.find_element(By.XPATH, self.checkbox_addinfo_xpath).click()
    def logindetails(self,name,password):
        #password="Qwerty@1"
        self.driver.find_element(By.XPATH, self.textbox_uname_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.textbox_confpassword_xpath).send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_saveinfo_xpath).click()
        self.driver.save_screenshot("C:\\Users\\vinothsc\\PycharmProjects\\projectorange\\screenshots\\image1.png")
    def click_empsave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()


class Admincheck:
    button_admin_xpath="//*[text()='Admin']"
    textbox_username_xpath="//*[text()='Username']/../..//*[@class='oxd-input oxd-input--active']"
    button_nameserach_xpath="//*[@type='submit']"
    box_checked_xpath="//*[@class='oxd-table-cell oxd-padding-cell'][2]"
    datanotfound_xpath="/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]"
    table='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'

    #Logout_one = "//*[@class='oxd-userdropdown-name']/../../.."
    #Logout_two = "//*[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH,self.button_admin_xpath).click()

    def check_user_name(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)



    def click_namesearch(self,username):
        self.driver.find_element(By.XPATH,self.button_nameserach_xpath).click()
        time.sleep(2)
        notfound=self.driver.find_element(By.XPATH,self.datanotfound_xpath)
        if notfound.text=="No Records Found":
            print("no account cretaeeddddd")
            print(notfound.text)
        else:
            name1=self.driver.find_element(By.XPATH,self.table)
            n2=name1.get_attribute('innerHTML')
            print(n2)
            if n2== username:  #to compare the created account and table feild.
                print("account created successfuly ")
                self.driver.save_screenshot("C:\\Users\\vinothsc\\PycharmProjects\\projectorange\\screenshots\\image.png")

               #logging out the current account.
                Logout_one = "//*[@class='oxd-userdropdown-name']/../../.."
                Logout_two = "//*[text()='Logout']"
                self.driver.find_element(By.XPATH,Logout_one).click()
                self.driver.find_element(By.XPATH,Logout_two).click()


            else:
                print("user name not found")
              #  print(n2.text)

   

    def get_sys_user(self):
      #  varr2 = self.driver.find_element(By.XPATH, self.box_checked_xpath)
        return varr2


