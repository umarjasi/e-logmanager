import pytest
from selenium import webdriver
from pageObjects.Loginpage import LoginPage

class TestLogin:
    baseURL = "http://elogmanager.westindia.cloudapp.azure.com/"
    username = "AD001"
    password = "syn12345"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # LoginPage
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()




