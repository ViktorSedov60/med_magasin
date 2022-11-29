from time import sleep

from pages.home_page import HeaderMenuPage, MenuTestPage


class TestHomePage:
    class TestHeader:
        def test_header_menu(self, driver):
            header_menu = HeaderMenuPage(driver, 'https://www.med-magazin.ru/')
            header_menu.open()
            text = header_menu.check_logo()
            status = header_menu.check_header_menu()
            city, town = header_menu.check_select_city()
            assert text == 'MED-МАГАЗИН.RU'
            assert status == 200
            assert city == town


    class TestMenu:
        def test_menu(self, driver):
            header_menu = MenuTestPage(driver, 'https://www.med-magazin.ru/')
            header_menu.open()
            data = header_menu.check_menu()
            # print(len(data))
            # print(data)




