from selenium.webdriver.common.by import By

class HomePage():
      lnk_logbook_xpath = "//a[@href='/QualityControl/RawMaterial']//span[@class='nav-icon py-2 w-auto']//span[@class='svg-icon svg-icon-3x']//img"

      def __init__(self,driver):
          self.driver=driver

      def Clicklogbook(self):
          self.driver.find_element(By.XPATH,self.lnk_logbook_xpath).click()