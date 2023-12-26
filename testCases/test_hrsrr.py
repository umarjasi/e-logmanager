import time
from pageObjects.Loginpage import LoginPage
from pageObjects.Homepage import HomePage
from pageObjects.HRSRR import HRSRR
from utilities.readProperties import ReadConfig


class TestHRSRR:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # LoginPage
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

        # HRSRR
        self.hrpage = HRSRR(self.driver)
        self.hrpage.ClickQC()
        time.sleep(1.3)
        self.hrpage.ClickHR()
        time.sleep(1.3)
        self.hrpage.scrolldown()
        time.sleep(1.3)
        self.hrpage.ClickSSR()
        time.sleep(1.3)
        self.hrpage.ClickAddnew()
        time.sleep(1.3)
        self.hrpage.SRRName("Mootori")
        time.sleep(1.3)
        self.hrpage.SRRInitial("P")
        time.sleep(1.3)
        self.hrpage.Dept()
        time.sleep(1.3)
        self.hrpage.Desgn("Quality Control")
        time.sleep(1.3)
        self.hrpage.remarks("Signature added")
        time.sleep(1.3)
        self.hrpage.Subbtn()
        time.sleep(1.3)
        self.hrpage.esigusername("UF001")
        time.sleep(1.3)
        self.hrpage.esigpassword("syn12345")
        time.sleep(1.3)
        self.hrpage.esigsave()
        time.sleep(1.3)
        self.hrpage.scroll()
        time.sleep(1.3)
        self.hrpage.clickgrid()
        time.sleep(1.3)
        self.hrpage.reviewremarks("Reviewed")
        time.sleep(1.3)
        self.hrpage.SubReview()
        time.sleep(1.3)
        self.hrpage.esigusername("UF001")
        time.sleep(1.3)
        self.hrpage.esigpassword("syn12345")
        time.sleep(1.3)
        self.hrpage.esigsave()
        time.sleep(1.3)
        self.hrpage.scroll()
        time.sleep(1.3)
        self.hrpage.clickgrid()
        time.sleep(1.3)
        self.hrpage.activitylog()
        time.sleep(1.3)
        self.hrpage.backbtn()
        time.sleep(1.3)
        self.hrpage.clickPlusIcon()
        time.sleep(1.3)
        self.hrpage.fromdate()
        time.sleep(1.3)
        self.hrpage.calendarfromdate()
        time.sleep(1.3)
        self.hrpage.todate()
        time.sleep(1.3)
        self.hrpage.calendartodate()
        time.sleep(1.3)
        self.hrpage.calendarsearch()
        time.sleep(1.3)
        self.hrpage.calendersearchref()
        time.sleep(1.3)
        self.hrpage.sort_asc()
        time.sleep(1.3)
        self.hrpage.sort_desc()
        time.sleep(1.3)
        self.hrpage.show_entries()
        time.sleep(1.3)
        self.hrpage.exportbtn()
        time.sleep(1.3)
        self.hrpage.scrollnext()
        time.sleep(1.3)
        self.hrpage.scrollprev()
        time.sleep(1.3)
        self.hrpage.dynamicfltr("Marketing")
        time.sleep(1.3)
        self.hrpage.sidebar()
        time.sleep(1.3)
        self.hrpage.Logout()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Login Page":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False








