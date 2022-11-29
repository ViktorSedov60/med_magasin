import ast
import random
from time import sleep

import requests

from base.base_page import BasePage
from locators.home_page_locator import HeaderMenuLocator, MenuTestLocator


class HeaderMenuPage(BasePage):
    locators = HeaderMenuLocator()

    def check_logo(self):
        # Проверяем, что мы открыли именно сайт "MED-МАГАЗИН.RU"
        text1 = self.is_visible(self.locators.LOGO).get_attribute('alt')
        return text1

    def check_header_menu(self):
        # Рандомно запрашиваем  меню в заголовке и проверяем возвращаемый код
        item_list = self.are_visible(self.locators.HEADER_MENU)
        data = []
        for item in item_list:
            data.append(item.get_attribute('href'))
        data_index = random.randrange(len(data))
        data = data[data_index]
        request = requests.get(data)
        return request.status_code

    def check_select_city(self):
        # случайно выбираем город из списка и проверяем, что именно он выбран
        self.is_visible(self.locators.SELECT_CITY).click()
        item_list = self.are_visible(self.locators.ITEM_CITY)

        data_index = random.randrange(len(item_list))
        city_item = item_list[data_index]
        city = city_item.text
        city_item.click()

        sleep(1)
        town = self.is_visible(self.locators.SELECT_CITY).text
        return city, town


class MenuTestPage(BasePage):
    locators = MenuTestLocator()


    def check_menu(self):
        # Получаем список групп товаров для использования для поиска в тестировании
        elements = self.is_visible(self.locators.CATALOG_MENU)
        self.move_to_element(elements)
        menu_item_list = self.are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            data.append(item.text)
        data = str(data).replace(" '',", '')  #.replace("''", '').replace(', ', '', 1)

        data1 = ast.literal_eval(data)
        print(data1)
        print(type(data1))

        # return data


        print(len(data1))

        data_index = random.randint(0, len(data1) -1)
        data2 = data1[data_index]

        print(data2)



