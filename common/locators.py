from selenium.webdriver.common.by import By

class BasePageLocators(object):
    ETSY_LOGO = (By.XPATH, "//span[contains(@class, 'etsy-icon') and @id='logo']")

class SearchPageLocators(object):
    SEARCH_TEXTBOX = (By.XPATH, "//input[@data-id='search-query' and @name='search_query']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and @value='Search']")
    SEARCH_RESULTS = (By.XPATH, "//h1[contains(@class, 'wt-text-caption')]")
    TOP_NAV_CATEGORY_LINK = (By.XPATH, "//li[contains(@class, 'top-nav-item')]//a//span[contains(text(), 'Home & Living')]")