import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ITBTR():
     lnk_rm1_xpath = "//span[normalize-space()='Quality Control']"
     lnk_rm_xpath = "//span[normalize-space()='Information Technology']"
     btn_adnew_id = "btnAddnew"
     lnk_ot_xpath = "//span[normalize-space()='Backup Tracking Register']"
     txtbox_stn_id = "BackupTrackingData_TapeNo"
     drp_ssn_xpath = "//select[@id='BackupTrackingData_SystemName']"
     drp_sbt_xpath = "//select[@id='BackupTrackingData_BackupType']"
     drp_sbm_xpath = "//select[@id='BackupTrackingData_BackupMode']"
     btn_subm_id = "btnStart"
     txtbox_esus_name = "txtUserName"
     txtbox_espa_name = "txtPassword"
     btn_sv_id = "btnESave"
     txtbox_loc_id = "BackupTrackingData_Location"
     txtbox_Res_id = "BackupTrackingData_BackupResult"
     btn_subend_id = "btnEnd"
     txtbox_revrem_id = "txtReview"
     btn_subrev_id = "btnReview"
     txtbox_apprem_id = "txtApprove"
     btn_subapp_id = "btnApprove"
     btn_aclo_id = "profile-tab-1"
     btn_back_id = "btnBack"
     sym_plic_xpath = "//td[@class='dtr-control sorting_1'][normalize-space()='1']"
     txtbox_frda_name = "FromDate"
     selbox_chda_xpath = "//td[@class='today day']"
     txtbox_toda_name = "ToDate"
     btn_sebt_id = "btnSearch"
     sort_asc_css = "th.sorting.sorting_asc"
     sort_desc_css = "th.sorting.sorting_desc"
     drpd_shen_xpath = "//select[@name='DataTables_Table_0_length']"
     btn_exp_id = "btnExport"
     bt_scrnxt_id = "DataTables_Table_0_next"
     bt_scrprev_id = "DataTables_Table_0_previous"
     txtbox_dyft_xpath = "//input[@type='search']"

     def __init__(self, driver):
         self.driver = driver

     def ClickQC(self):
         self.driver.find_element(By.XPATH, self.lnk_rm1_xpath).click()

     def ClickIT(self):
         self.driver.find_element(By.XPATH, self.lnk_rm_xpath).click()

     def ClickBTR(self):
         self.driver.find_element(By.XPATH, self.lnk_ot_xpath).click()

     def ClickAddnew(self):
         self.driver.find_element(By.ID, self.btn_adnew_id).click()

     def SetTapeNo(self, STN):
         self.driver.find_element(By.ID, self.txtbox_stn_id).send_keys(STN)

     def SetSystemName(self):
         rm_ele = self.driver.find_element(By.XPATH, self.drp_ssn_xpath)
         rmd = Select(rm_ele)
         rmd.select_by_index(3)

     def SetBackuptype(self):
         rm_ele = self.driver.find_element(By.XPATH, self.drp_sbt_xpath)
         rmd = Select(rm_ele)
         rmd.select_by_index(1)

     def SetBackupmode(self):
         rm_ele = self.driver.find_element(By.XPATH, self.drp_sbm_xpath)
         rmd = Select(rm_ele)
         rmd.select_by_index(1)

     def Subbtn(self):
         self.driver.find_element(By.ID, self.btn_subm_id).click()

     def esigusername(self, eus):
         self.driver.find_element(By.NAME, self.txtbox_esus_name).send_keys(eus)

     def esigpassword(self, epas):
         self.driver.find_element(By.NAME, self.txtbox_espa_name).send_keys(epas)

     def esigsave(self):
         self.driver.find_element(By.ID, self.btn_sv_id).click()

     def scroll(self):
         self.driver.execute_script("window.scrollBy(0,200)", "")
         init = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[7]")
         self.driver.execute_script("arguments[0].scrollIntoView();", init)

     def scrolldown(self):
         self.driver.execute_script("window.scrollBy(0,600)", "")
         init = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/div[1]/ul[1]/li[7]/a[1]/span[1]")
         self.driver.execute_script("arguments[0].scrollIntoView();", init)

     def clickgrid(self):
         grid_entries = self.driver.find_element(By.CSS_SELECTOR, "tr.odd")
         actions = ActionChains(self.driver)
         actions.double_click(grid_entries)
         actions.perform()

     def SetLocation(self, LOC):
         self.driver.find_element(By.ID, self.txtbox_loc_id).send_keys(LOC)

     def SetResBackup(self, Res):
         self.driver.find_element(By.ID, self.txtbox_Res_id).send_keys(Res)

     def SubEnd(self):
         self.driver.find_element(By.ID, self.btn_subend_id).click()

     def setReview(self, rer):
         self.driver.find_element(By.ID, self.txtbox_revrem_id).send_keys(rer)

     def SubReview(self):
         self.driver.find_element(By.ID, self.btn_subrev_id).click()

     def setApprove(self, rer):
         self.driver.find_element(By.ID, self.txtbox_apprem_id).send_keys(rer)

     def SubApprove(self):
         self.driver.find_element(By.ID, self.btn_subapp_id).click()

     def activitylog(self):
         self.driver.find_element(By.ID, self.btn_aclo_id).click()

     def backbtn(self):
         self.driver.find_element(By.ID, self.btn_back_id).click()

     def clickPlusIcon(self):
         self.driver.execute_script("window.scrollBy(0,500)", "")
         self.driver.find_element(By.XPATH, self.sym_plic_xpath).click()

     def fromdate(self):
         self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
         self.driver.find_element(By.NAME, self.txtbox_frda_name).click()

     def calendarfromdate(self):
         self.driver.find_element(By.XPATH, self.selbox_chda_xpath).click()

     def todate(self):
         self.driver.find_element(By.NAME, self.txtbox_toda_name).click()

     def calendartodate(self):
         self.driver.find_element(By.XPATH, self.selbox_chda_xpath).click()

     def calendarsearch(self):
         self.driver.find_element(By.ID, self.btn_sebt_id).click()
         self.driver.execute_script("window.scrollBy(0,500)", "")

     def calendersearchref(self):
         self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
         self.driver.find_element(By.ID, self.btn_sebt_id).click()

     def sort_asc(self):
         self.driver.execute_script("window.scrollBy(0,400)", "")
         self.driver.find_element(By.CSS_SELECTOR, self.sort_asc_css).click()

     def sort_desc(self):
         self.driver.find_element(By.CSS_SELECTOR, self.sort_desc_css).click()

     def show_entries(self):
         showentries_ele = self.driver.find_element(By.XPATH, self.drpd_shen_xpath)
         showentries = Select(showentries_ele)
         showentries.select_by_value("25")
         showentries.select_by_index(1)
         self.driver.execute_script("window.scrollBy(0,900)", "")
         time.sleep(3)
         self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

     def exportbtn(self):
         self.driver.find_element(By.ID, self.btn_exp_id).click()

     def scrollnext(self):
         self.driver.execute_script("window.scrollBy(0,500)", "")
         self.driver.find_element(By.ID, self.bt_scrnxt_id).click()
         self.driver.find_element(By.ID, self.bt_scrnxt_id).click()

     def scrollprev(self):
         self.driver.find_element(By.ID, self.bt_scrprev_id).click()
         self.driver.find_element(By.ID, self.bt_scrprev_id).click()
         time.sleep(4)
         self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

     def dynamicfltr(self, dyftr):
         self.driver.find_element(By.XPATH, self.txtbox_dyft_xpath).send_keys(dyftr)




