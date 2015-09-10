# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import re


class Application(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.driver.get("https://auto.ria.com/")

    def reg(self, loc, text):
        driver = self.driver
        marks = driver.find_element_by_id(loc)
        options = marks.find_elements_by_tag_name('option')
        for option in options:
            text_from_tag = option.text
            try:
                text_to_ret = re.search("%s \(.*\)" % text, text_from_tag)
                if option.text == text_to_ret.group():
                    return text_to_ret.group()
            except:
                pass

    def fill_fields_to_search(self, search_options):
        driver = self.driver
        Select(driver.find_element_by_id("marks")).select_by_visible_text(self.reg("marks", search_options["mark"]))
        Select(driver.find_element_by_id("models")).select_by_visible_text(self.reg("models", search_options["model"]))
        driver.find_element_by_xpath("//label[@for='with_photo']").click()
        Select(driver.find_element_by_id("regionCenters")).select_by_visible_text(search_options["region"])
        Select(driver.find_element_by_id("year")).select_by_visible_text(search_options["year"])
        Select(driver.find_element_by_id("yearTo")).select_by_visible_text(search_options["year_to"])
        driver.find_element_by_id("priceFrom").clear()
        driver.find_element_by_id("priceFrom").send_keys(search_options["price_from"])
        driver.find_element_by_id("priceTo").clear()
        driver.find_element_by_id("priceTo").send_keys(search_options["price_to"])

    def click_search_button(self):
        driver = self.driver
        driver.find_element_by_css_selector("button.button-primary").click()

    def check_text_on_search_form(self):
        driver = self.driver
        search_list = []
        search_list.append(driver.find_element_by_xpath("//span[@data-id='leftFilterPriceRange']/a[1]").text)
        search_list.append(driver.find_element_by_xpath("//span[@data-id='psmarka-0']/a[1]").text)
        search_list.append(driver.find_element_by_xpath("//span[@data-id='psmodel-0']/a[1]").text)
        search_list.append(driver.find_element_by_xpath("//span[@data-id='yearRange-0']/a[1]").text)
        # search_list.append(driver.find_element_by_xpath("//span[@data-id='leftFilterCategory']/a[1]").text)
        search_list.append(driver.find_element_by_xpath("//span[@data-id='state-0']/a[1]").text)
        search_list.append(driver.find_element_by_xpath("//span[@data-id='topFilterWithPhoto']/a[1]").text)
        return search_list

    def count(self):
        driver = self.driver
        return len(driver.find_elements_by_xpath("//div[@class='m_head-ticket']"))
