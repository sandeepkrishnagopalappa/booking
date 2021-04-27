import pytest
from selenium import webdriver
from config import *
class Driver_init:

    @pytest.fixture(scope='class',autouse=True)
    def driver_init(self,request):

        if browser.upper()=="CHROME":
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            driver=webdriver.Chrome(executable_path,options=options)

        elif browser.upper()=="FIREFOX":
            driver=webdriver.Firefox()

        request.cls.driver=driver
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(40)
        yield
        driver.quit()
