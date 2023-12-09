import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class HRTNIR:
    lnk_rm1_xpath = "//span[normalize-space()='Quality Control']"
    lnk_rm_xpath = "//span[normalize-space()='Human Resources']"
    lnk_ot_xpath = "//span[normalize-space()='Training Need Identification Record']"
    btn_adnew_id = "btnAddnew"
    txtbox_ts_id = "TIRData_TrainingSubject"
    dro_promt_id = "TIRData_Proposedmonth"
    txtbox_noe_id = "TIRData_EmployeeName"
    txtbox_emc_id = "TIRData_EmployeeCode"
    txtbox_des_id = "TIRData_Designation"
    txtbox_not_id = "TIRData_TraineeName"
    txtbox_dot_id = "TIRData_TraineeDesignation"
    txtbox_re_id = "TIRData_Remarks"
    btn_sub_id = "btnSubmit"
    txtbox_esus_name = "txtUserName"
    txtbox_espa_name = "txtPassword"
    btn_sv_id = "btnESave"

    txtbox_revrem_id = "TIRData_ReviewRemarks"
    btn_subrev_id = "btnReview"
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
    tog_qu_id = "kt_quick_user_toggle"
    btn_lo_lt = "Log Out"

    def __init__(self, driver):
        self.driver = driver

    def ClickQC(self):
        self.driver.find_element(By.XPATH, self.lnk_rm1_xpath).click()

    def ClickHR(self):
        self.driver.find_element(By.XPATH, self.lnk_rm_xpath).click()

    def ClickTNIR(self):
        self.driver.find_element(By.XPATH, self.lnk_ot_xpath).click()

    def ClickAddnew(self):
        self.driver.find_element(By.ID, self.btn_adnew_id).click()

    def TrainSub(self, TS):
        self.driver.find_element(By.ID, self.txtbox_ts_id).send_keys(TS)

    def Promotr(self):
        drop_down_field = self.driver.find_element(By.ID, self.dro_promt_id)
        select = Select(drop_down_field)
        select.select_by_visible_text("April")

    def NaofEmp(self, NOE):
        self.driver.find_element(By.ID, self.txtbox_noe_id).send_keys(NOE)

    def EmpCo(self, EMC):
        self.driver.find_element(By.ID, self.txtbox_emc_id).send_keys(EMC)

    def Des(self, DES):
        self.driver.find_element(By.ID, self.txtbox_des_id).send_keys(DES)

    def NoT(self, NOT):
        self.driver.find_element(By.ID, self.txtbox_not_id).send_keys(NOT)

    def DoT(self, DOT):
        self.driver.find_element(By.ID, self.txtbox_dot_id).send_keys(DOT)

    def Remarks(self, RE):
        self.driver.find_element(By.ID, self.txtbox_re_id).send_keys(RE)

    def Subbtn(self):
        self.driver.find_element(By.ID, self.btn_sub_id).click()

    def esigusername(self, eus):
        self.driver.find_element(By.NAME, self.txtbox_esus_name).send_keys(eus)

    def esigpassword(self, epas):
        self.driver.find_element(By.NAME, self.txtbox_espa_name).send_keys(epas)

    def esigsave(self):
        self.driver.find_element(By.ID, self.btn_sv_id).click()

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0,200)", "")
        init = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[5]")
        self.driver.execute_script("arguments[0].scrollIntoView();", init)

    def clickgrid(self):
        grid_entries = self.driver.find_element(By.CSS_SELECTOR, "tr.odd")
        actions = ActionChains(self.driver)
        actions.double_click(grid_entries)
        actions.perform()

    def reviewremarks(self,revrem):
        self.driver.find_element(By.ID, self.txtbox_revrem_id).send_keys(revrem)

    def SubReview(self):
        self.driver.find_element(By.ID, self.btn_subrev_id).click()

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

    def sidebar(self):
        self.driver.find_element(By.ID, self.tog_qu_id).click()

    def Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_lo_lt).click()




