
from Library.web_utility import Generic_method
from Library.file_library import xl_data
from Library.basefixture import *
import time

class Register(Driver_init):
    data = xl_data()
    variable1, keys = data.read_locators(file_name, sheet_name)
    ObjectGen = Generic_method()

    def __init__(self, driver):
        self.driver = driver

    def alert_ok(self):
        reg1 = Register.variable1["alert_ok"]
        Register.ObjectGen.click_on_element(self.driver, reg1)

    def click_on_flight(self):
        reg2 = Register.variable1["click_on_flight"]
        Register.ObjectGen.click_on_element(self.driver, reg2)
        # self.driver.find_element_by_link_text("FLIGHTS").click()  # flights

    def window_switch(self):
        win_handles = self.driver.window_handles
        time.sleep(3)
        self.driver.switch_to.window(win_handles[1])
        time.sleep(3)
        return self.ObjectGen.get_page_title(self.driver)

    def round_trip(self):
        reg3 = Register.variable1["round_trip"]
        Register.ObjectGen.click_on_element(self.driver, reg3)
        return Register.ObjectGen.validate_element_display(self.driver, Register.variable1["return_date_click"])
        # self.driver.find_element_by_xpath("//label[@for='Round-Trip']").click()

    def station_from_sending_keys(self):
        reg4 = Register.variable1["station_from_sending_keys"]
        Register.ObjectGen.enter_text(self.driver, reg4, values="Chennai")
        # self.driver.find_element_by_xpath("//input[@id='stationFrom']").send_keys("Chennai")  # station_from_sending_keys

    def station_from_click(self):
        reg5 = Register.variable1["station_from_click"]
        Register.ObjectGen.click_on_element(self.driver, reg5)
        # self.driver.find_element_by_xpath("//div[text()='Chennai (MAA)']").click()  # station_from_click

    def station_to_sending_keys(self):
        reg6 = Register.variable1["station_to_sending_keys"]
        Register.ObjectGen.enter_text(self.driver, reg6, values="Mumbai")
        # self.driver.find_element_by_xpath("//input[@id='stationTo']").send_keys("Mumbai")  # station_to_sending_keys

    def station_to_click(self):
        reg7 = Register.variable1["station_to_click"]
        Register.ObjectGen.click_on_element(self.driver, reg7)
        # self.driver.find_element_by_xpath("//div[text()='Mumbai (BOM)']").click()  # station_to_click

    def start_date_select(self):
        reg8 = Register.variable1["start_date_select"]
        Register.ObjectGen.click_on_element(self.driver, reg8)
        # self.driver.find_element_by_xpath("(//table)[2]//tr[4]//td[4]").click()  # start_date_select

    def return_date_click(self):
        reg9 = Register.variable1["return_date_click"]
        Register.ObjectGen.click_on_element(self.driver, reg9)
        # self.driver.find_element_by_xpath("//input[@id='returnDate']").click()  # return_date_click

    def apirl_month_select(self):
        reg10 = Register.variable1["apirl_month_select"]
        Register.ObjectGen.click_on_element(self.driver, reg10)
        # self.driver.find_element_by_xpath("(//div[@class='date-table-right'])[2]//table//tr[2]//td").click()  # apirl_month_select

    def return_date_select(self):
        reg11 = Register.variable1["return_date_select"]
        Register.ObjectGen.click_on_element(self.driver, reg11)
        # self.driver.find_element_by_xpath( "//*[@id='Return-Date']/datepickermodifi/div/div[2]/div[2]/table/tbody/tr[2]/td[7]").click()  # return_date_select

    def search(self):
        reg12 = Register.variable1["search"]
        Register.ObjectGen.click_on_element(self.driver, reg12)
        return Register.ObjectGen.validate_element_display(self.driver, Register.variable1["book"])
        # self.driver.find_element_by_xpath("/html/body/app-root/app-index/div[2]/div[3]/div/div/div/div[2]/form/button").click()  # search

    def book(self):
        reg13 = Register.variable1["book"]
        Register.ObjectGen.click_on_element(self.driver, reg13)
        return Register.ObjectGen.validate_element_display(self.driver, Register.variable1["gst_pop_up"])
        # self.driver.find_element_by_xpath("//button[@class='btn btn-md text-primary white btn-rounded waves-effect waves-light m-0 font-14']").click()  # book

    def normal_fair(self):
        reg14 = Register.variable1["continue"]
        Register.ObjectGen.click_on_element(self.driver, reg14)
        #self.driver.find_element_by_xpath("//*[@id="modalflexiFare"]/div/div/div[3]/button[2]").click()

    def gst_pop_up(self):
        reg15 = Register.variable1["gst_pop_up"]
        Register.ObjectGen.click_on_element(self.driver, reg15)
        # self.driver.find_element_by_xpath("//*[@id='GSTModal']/div/div/div[3]/button[2]").click()  # gst_pop_up
