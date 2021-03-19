
class Generic_method:

    def click_on_element(self,driver,locator):
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).click()

    def enter_text(self,driver,locator,*,values):
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).send_keys(str(values))

    def validate_check_radio_button(self,driver,locator):
        locator_type, locator_value = locator
        return driver.find_element(locator_type, locator_value).is_selected()

    def validate_element_display(sel,driver,locator):
        locator_type, locator_value = locator
        return driver.find_element(locator_type, locator_value).is_displayed()

    def get_page_title(self, driver):
        return driver.title






