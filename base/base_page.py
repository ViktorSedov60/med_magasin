from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator):
        return wait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def are_visible(self, locator):
        return wait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def is_present(self, locator):
        return wait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def are_present(self, locator):
        return wait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def is_not_visible(self, locator):
        return wait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def is_clickable(self, locator):
        return wait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()



    def drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    def drag_and_drop(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def window_stop(self):
        self.driver.execute_script("window.stop();")



