from selenium.webdriver.common.by import By
class LoginPage:
    txtbox_username_id = "txtUserID"
    txtbox_password_name = "UserData.Password"
    button_login_id = "kt_login_signin_submit"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.send_keys(username)

    def setPassword(self, password):
        passwordtxt = self.driver.find_element(By.NAME, self.txtbox_password_name)
        passwordtxt.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()