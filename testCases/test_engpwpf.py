import time
from pageObjects.Loginpage import LoginPage
from pageObjects.Homepage import HomePage
from pageObjects.ENGPWPF import ENGPWPF
from utilities.readProperties import ReadConfig


class TestENGPWPF:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # LoginPage
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # HomePage Logbook
        self.hm = HomePage(self.driver)
        self.hm.Clicklogbook()

        #ENGPWPF
        self.engpage = ENGPWPF(self.driver)
        self.engpage.ClickQC()
        time.sleep(1.3)
        self.engpage.ClickEng()
        time.sleep(1.3)
        self.engpage.ClickPWPF()
        time.sleep(1.3)
        self.engpage.ClickAddnew()
        time.sleep(1.3)
        self.engpage.TyofFilter()
        time.sleep(1.3)
        self.engpage.CleaningStatus()
        time.sleep(1.3)
        self.engpage.FilterReplaby("Kumar")
        time.sleep(1.3)
        self.engpage.Floor()
        time.sleep(1.3)
        self.engpage.Remarks("Filter added")
        time.sleep(1.3)
        self.engpage.Subbtn()
        time.sleep(1.3)
        self.engpage.esigusername("UF001")
        time.sleep(1.3)
        self.engpage.esigpassword("syn12345")
        time.sleep(1.3)
        self.engpage.esigsave()
        time.sleep(1.3)
        self.engpage.scroll()
        time.sleep(1.3)
        self.engpage.clickgrid()
        time.sleep(1.3)
        self.engpage.SubReview()
        time.sleep(1.3)
        self.engpage.esigusername("UF001")
        time.sleep(1.3)
        self.engpage.esigpassword("syn12345")
        time.sleep(1.3)
        self.engpage.esigsave()
        time.sleep(1.3)
        self.engpage.scroll()
        time.sleep(1.3)
        self.engpage.clickgrid()
        time.sleep(1.3)
        self.engpage.activitylog()
        time.sleep(1.3)
        self.engpage.backbtn()
        time.sleep(1.3)
        self.engpage.clickPlusIcon()
        time.sleep(1.3)
        self.engpage.fromdate()
        time.sleep(1.3)
        self.engpage.calendarfromdate()
        time.sleep(1.3)
        self.engpage.todate()
        time.sleep(1.3)
        self.engpage.calendartodate()
        time.sleep(1.3)
        self.engpage.calendarsearch()
        time.sleep(1.3)
        self.engpage.calendersearchref()
        time.sleep(1.3)
        self.engpage.sort_asc()
        time.sleep(1.3)
        self.engpage.sort_desc()
        time.sleep(1.3)
        self.engpage.show_entries()
        time.sleep(1.3)
        self.engpage.exportbtn()
        time.sleep(1.3)
        self.engpage.scrollnext()
        time.sleep(1.3)
        self.engpage.scrollprev()
        time.sleep(1.3)
        self.engpage.dynamicfltr("Partially Cleaned")
        time.sleep(1.3)
        self.engpage.sidebar()
        time.sleep(1.3)
        self.engpage.Logout()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Login Page":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

