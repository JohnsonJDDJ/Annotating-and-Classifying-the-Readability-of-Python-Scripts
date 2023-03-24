from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # for checking the correct error message


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[href*="password-reset"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    SIGN_UP_PASSWORD_REPETITION = (By.CSS_SELECTOR, "[name='registration-password2']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADD_TO_BASKET_BUTTON = (By. CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, ".btn-wishlist")
    PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description")
    PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    AVAILABILITY = (By.CSS_SELECTOR, ".product_main > .availability")
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_INFO_TABLE = (By.CSS_SELECTOR, ".table-striped")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
    NAME_OF_ADDED_PRODUCT = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")


class BasketPageLocators():
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a[href*='basket']")
    VIEW_BASKET_INVALID = (By.CSS_SELECTOR, ".btn-group > a[href*='basket']")  # for checking the correct error message
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    FILLED_BASKET = (By.CSS_SELECTOR, ".basket-items")