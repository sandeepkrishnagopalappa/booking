
import time
from config import *
from pom.register import Register
from Library.basefixture import Driver_init

class Test_demo(Driver_init):

    def test_object(self):

        assert url == self.driver.current_url, "URL did not match"

        obj = Register(self.driver)
        obj.alert_ok()
        obj.click_on_flight()
        obj.window_switch()

        actual_flight_page_title = obj.window_switch()
        assert actual_flight_page_title.lower() == expected_flight_page_title.lower(), "Title did not match"

        res_of_round_button= obj.round_trip()
        time.sleep(15)
        assert res_of_round_button == True, "Round trip radio button is not selected"

        obj.station_from_sending_keys()
        obj.station_from_click()
        obj.station_to_sending_keys()
        time.sleep(5)
        obj.station_to_click()
        obj.start_date_select()
        obj.return_date_click()
        obj.apirl_month_select()
        obj.return_date_select()
        time.sleep(5)

        res_of_search_button = obj.search()
        assert res_of_search_button == True, "Book button is not displayed"

        time.sleep(5)
        res_of_book_button=obj.book()
        assert res_of_search_button == True, "GST pop button not displayed"

        obj.gst_pop_up()
