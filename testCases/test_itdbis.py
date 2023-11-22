import time
from pageObjects.Loginpage import LoginPage
from pageObjects.Homepage import HomePage
from pageObjects.ITDBIS import ITDBIS


class TestITDBIS:
    baseURL = "http://elogmanager.westindia.cloudapp.azure.com/"
    username = "AD001"
    password = "syn12345"

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

        #ITDBIS
        self.qapage = ITDBIS(self.driver)
        self.qapage.ClickQC()
        time.sleep(1.3)
        self.qapage.ClickIT()
        time.sleep(1.3)
        self.qapage.scrolldown()
        time.sleep(1.3)
        self.qapage.ClickDBIS()
        time.sleep(1.3)
        self.qapage.ClickAddnew()
        time.sleep(1.3)
        self.qapage.SetSiteBlock()
        time.sleep(1.3)
        self.qapage.SetFoldername("DataBackup 11052023")
        time.sleep(1.3)
        self.qapage.setremarks("IT server added")
        time.sleep(1.3)
        self.qapage.Subbtn()
        time.sleep(1.3)
        self.qapage.esigusername("AD001")
        time.sleep(1.3)
        self.qapage.esigpassword("syn12345")
        time.sleep(1.3)
        self.qapage.esigsave()
        time.sleep(1.3)
        self.qapage.scroll()
        time.sleep(1.3)
        self.qapage.clickgrid()
        time.sleep(1.3)
        self.qapage.SetLstoffiles("Datas")
        time.sleep(1.3)
        self.qapage.SetIntegTest("105MB")
        time.sleep(1.3)
        self.qapage.Backupdate()
        time.sleep(1.3)
        self.qapage.calendarBackupdate()
        time.sleep(1.3)
        self.qapage.SubEnd()
        time.sleep(1.3)
        self.qapage.esigusername("AD001")
        time.sleep(1.3)
        self.qapage.esigpassword("syn12345")
        time.sleep(1.3)
        self.qapage.esigsave()
        time.sleep(1.3)
        self.qapage.scroll()
        time.sleep(1.3)
        self.qapage.clickgrid()
        time.sleep(1.3)
        self.qapage.setReview("Reviewed")
        time.sleep(1.3)
        self.qapage.SubReview()
        time.sleep(1.3)
        self.qapage.esigusername("AD001")
        time.sleep(1.3)
        self.qapage.esigpassword("syn12345")
        time.sleep(1.3)
        self.qapage.esigsave()
        time.sleep(1.3)
        self.qapage.scroll()
        time.sleep(1.3)
        self.qapage.clickgrid()
        time.sleep(1.3)
        self.qapage.activitylog()
        time.sleep(1.3)
        self.qapage.backbtn()
        time.sleep(1.3)
        self.qapage.clickPlusIcon()
        time.sleep(1.3)
        self.qapage.fromdate()
        time.sleep(1.3)
        self.qapage.calendarfromdate()
        time.sleep(1.3)
        self.qapage.todate()
        time.sleep(1.3)
        self.qapage.calendartodate()
        time.sleep(1.3)
        self.qapage.calendarsearch()
        time.sleep(1.3)
        self.qapage.calendersearchref()
        time.sleep(1.3)
        self.qapage.sort_asc()
        time.sleep(1.3)
        self.qapage.sort_desc()
        time.sleep(1.3)
        self.qapage.show_entries()
        time.sleep(1.3)
        self.qapage.exportbtn()
        time.sleep(1.3)
        self.qapage.scrollnext()
        time.sleep(1.3)
        self.qapage.scrollprev()
        time.sleep(1.3)
        self.qapage.dynamicfltr("Block-2")
        time.sleep(3)
        self.driver.close()
        assert True
