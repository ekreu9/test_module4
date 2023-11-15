from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")    
    FIELD_CONFIRM_ADD_BOOK_TO_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>.alertinner strong")
    FIELD_BASKET_TOTAL_SUM = (By.CSS_SELECTOR, "#messages>div:nth-child(3)>.alertinner strong")
    PRICE_OF_THE_BOOK = (By.CSS_SELECTOR, "#content_inner>article>div:nth-child(1)>div:nth-child(2)>.price_color")
    NAME_OF_THE_BOOK = (By.CSS_SELECTOR, "#content_inner>article>div:nth-child(1)>div:nth-child(2)>h1")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>.btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    

class BasketPageLocators():
    BASKET_STATUS = (By.CSS_SELECTOR, "div.content>div#content_inner>p")
    BUTTON_RESUME_PURCHASE = (By.CSS_SELECTOR, "div.content>div#content_inner>p a")
    PURCHASE_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    
    
