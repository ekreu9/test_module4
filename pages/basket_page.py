from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_text_about_basket_is_empty(self):
        basket_status = self.browser.find_element(*BasketPageLocators.BASKET_STATUS).text
        assert "empty" in basket_status, "Basket is not empty"

        ##assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), "Basket is not empty"


    def should_be_basket_be_empty(self):
        button_for_resume_purchase = self.browser.find_element(*BasketPageLocators.BUTTON_RESUME_PURCHASE).text
        assert "Continue" in button_for_resume_purchase, "Button for resume is not there, basket is not empty"
        ##assert self.is_element_present(*BasketPageLocators.BUTTON_RESUME_PURCHASE), "Button for resume is not there, basket is not empty"


    def should_not_be_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PURCHASE_IN_BASKET), \
               "Purchase in basket, but should not be"





    
   

    

    


    
