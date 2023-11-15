from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def correct_book_add_to_basket(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_OF_THE_BOOK).text
        name_book_in_field = self.browser.find_element(*ProductPageLocators.FIELD_CONFIRM_ADD_BOOK_TO_BASKET).text
        assert name_book == name_book_in_field, "Title of book not found"


    def correct_sum_in_the_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_BOOK).text
        total_sum_in_field = self.browser.find_element(*ProductPageLocators.FIELD_BASKET_TOTAL_SUM).text
        assert book_price == total_sum_in_field, "SUM IS NOT CORRECT"

    

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.FIELD_CONFIRM_ADD_BOOK_TO_BASKET), \
               "Success message is presented, but should not be"


    def should_element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.FIELD_CONFIRM_ADD_BOOK_TO_BASKET), \
               "Success message is presented, but should not be"



    
