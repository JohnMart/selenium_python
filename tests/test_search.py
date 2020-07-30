import pytest
from selenium import webdriver
from base_page import BasePage
from search_page import SearchPage

@pytest.mark.usefixtures("web_driver")
class TestSearch():

    def test_search_for_item(self):
        base_page = BasePage(self.driver)
        search_page = SearchPage(self.driver)
        
        #navigate to etsy and search for an item
        assert base_page.nav_to_etsy()
        assert search_page.search_for_item()

    def test_search_for_category(self):
        base_page = BasePage(self.driver)
        search_page = SearchPage(self.driver)
        
        #navigate to etsy and search for items by category
        assert base_page.nav_to_etsy()
        assert search_page.search_for_category()