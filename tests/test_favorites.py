import pytest
from selenium import webdriver
from base_page import BasePage
from search_page import SearchPage

@pytest.mark.usefixtures("web_driver")
class TestFavorites():

    def test_add_favorite_without_signin(self):
        base_page = BasePage(self.driver)
        search_page = SearchPage(self.driver)
        
        #navigate to etsy and search for an item
        assert base_page.nav_to_etsy()
        assert search_page.search_for_item("BMW E28 Keychain")
        
        #retrieve all favorite icons from search results, click the first instance, verify join etsy modal displays
        fav_buttons = self.driver.find_elements_by_xpath("//ul[contains(@class, 'responsive-listing-grid')]" +
            "//li//div[@data-favorite-button-wrapper]//button[contains(@class, 'favorite-listing-button')]")
        fav_buttons[0].click()
        assert self.driver.find_element_by_xpath("//div[@data-join-neu-overlay-container]")