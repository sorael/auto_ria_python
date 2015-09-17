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
        self.wait.until(lambda x: driver.find_element_by_id("marks"))
        Select(driver.find_element_by_id("marks")).select_by_visible_text(self.reg("marks", search_options["mark"]))
        self.wait.until(lambda x: driver.find_element_by_id("models"))
        Select(driver.find_element_by_id("models")).select_by_visible_text(self.reg("models", search_options["model"]))
        self.wait.until(lambda x: driver.find_element_by_xpath("//label[@for='with_photo']"))
        driver.find_element_by_xpath("//label[@for='with_photo']").click()
        self.wait.until(lambda x: driver.find_element_by_id("regionCenters"))
        Select(driver.find_element_by_id("regionCenters")).select_by_visible_text(search_options["region"])
        self.wait.until(lambda x: driver.find_element_by_id("year"))
        Select(driver.find_element_by_id("year")).select_by_visible_text(search_options["year"])
        self.wait.until(lambda x: driver.find_element_by_id("yearTo"))
        Select(driver.find_element_by_id("yearTo")).select_by_visible_text(search_options["year_to"])
        self.wait.until(lambda x: driver.find_element_by_id("priceFrom"))
        driver.find_element_by_id("priceFrom").clear()
        driver.find_element_by_id("priceFrom").send_keys(search_options["price_from"])
        self.wait.until(lambda x: driver.find_element_by_id("priceTo"))
        driver.find_element_by_id("priceTo").clear()
        driver.find_element_by_id("priceTo").send_keys(search_options["price_to"])

    def click_search_button(self):
        driver = self.driver
        driver.find_element_by_css_selector("button.button-primary").click()

    def check_text_on_search_form(self):
        driver = self.driver
        search_list = []
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='leftFilterPriceRange']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='leftFilterPriceRange']/a[1]").text)
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='psmarka-0']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='psmarka-0']/a[1]").text)
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='psmodel-0']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='psmodel-0']/a[1]").text)
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='yearRange-0']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='yearRange-0']/a[1]").text)
        # search_list.append(driver.find_element_by_xpath("//span[@data-id='leftFilterCategory']/a[1]").text)
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='state-0']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='state-0']/a[1]").text)
        self.wait.until(lambda x: driver.find_element_by_xpath("//span[@data-id='topFilterWithPhoto']/a[1]"))
        search_list.append(driver.find_element_by_xpath("//span[@data-id='topFilterWithPhoto']/a[1]").text)

        return search_list

    def count(self):
        driver = self.driver
        return len(driver.find_elements_by_xpath("//div[@class='m_head-ticket']"))

    def result_equals_search_options(self, mark, model):
        driver = self.driver
        elements = driver.find_elements_by_xpath("//div[@class='item ticket-title']")
        auto = "%s %s" % (mark, model)
        for element in elements:
            t = element.find_element_by_class_name("address").get_attribute("title")
            if t[:len(auto)] != auto:
                return False
        return True
