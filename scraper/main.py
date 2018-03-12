#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from data_class import *
import time
from mysql_class import *

class Scraper:
    """
    calss to manage scrapping
    """

    def __def__(self):
        self.data = Data()
        self.mysql = Mysql()

    def get_data_object(self, link):
        """
        return data object with values saved
            """
        browser = webdriver.Firefox()
        browser.get(link)
        try:
            self.data.set_title(browser.find_element_by_css_selector("h1.epi-fontLg"))
        except NoSuchElementException:
            print("\ttitle missing")
        self.data.set_extracte_date(time.time())
        self.data.set_url(link)
        try:
            self.data.set_date_post(browser.find_element_by_css_selector("time"))
        except NoSuchElementException:
            print("\tdate missing")
        try:
            self.data.set_compagny_name(browser.find_element_by_css_selector("div.bw-release-companyinfo h3 span"))
        except NoSuchElementException:
            print("\tcompagny name missing")
        try:
            self.data.set_ticket_code(browser.find_element_by_css_selector("div#cic a span"))
        except NoSuchElementException:
            print("\tticket code missing")
        try:
            self.data.add_hash_tag(browser.find_elements_by_css_selector("ul.hash-tags li a.hash-tag"))
        except NoSuchElementException:
            print("\thash tag missing")
        try:
            self.data.add_cash_tag(browser.find_elements_by_css_selector("ul.cash-tags li a.cash-tag"))
        except NoSuchElementException:
            print("\tcash tag missing")
        try:
            self.data.set_content(browser.find_element_by_css_selector("div.bw-release-story"))
        except NoSuchElementException:
            print("\tcontent missing")
        return self.data

    def save_data_object(self, link):
        """
        save data object and add it in BDD
        """
        self.get_data_object(link)
        self.mysql.add_data(self.data)


    def get_links_pages(self, link):
        """
        get all links from the pages have to be scrap
        """
        browser = webdriver.Firefox()
        browser.get(link)
        list_links = browser.find_elements_by_css_selector("div#headlines ul.bwNewsList li a.bwTitleLink")
        for list_link in list_links:
            self.save_data_object(list_link.get_attribute("href"))

scraper = Scraper()
scraper.get_links_pages("https://www.businesswire.com/portal/site/home/news/multimedia/")
