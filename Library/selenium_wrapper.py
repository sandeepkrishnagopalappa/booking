from selenium.webdriver.


class element_to_be_enabled:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        loctype, locvalue = self.locator
        element = driver.find_element(loctype, locvalue)
        return True if element.is_enabled() else False

def _wait(enabled=True, visible=True):
    def wait(func):
        def wrapper(*args, **kwargs):
            locator, = args
            w = WebDriverWait(driver, 10)
            if visible:
                w.until(ec.visibility_of_element_located(locator))
            if enabled:
                w.until(element_to_be_enabled(locator))
            return func(*args, **kwargs)
        return wrapper
    return wait