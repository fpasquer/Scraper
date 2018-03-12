#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
this class manage data went scraped
"""

def check_data_exist(data):
    """
    check si data is empty
    """
    if data is not None:
        if data.text is not None:
            return True
    return False

class Data:
    """
    title : titre de l'article
    extracte_date : date de la copie de l'article (timestamp)
    date_post : date de l'article
    compagny_name : nom de l'entreprise
    ticket_code : code ticket de l'entreprise
    hash_tag : hash_tag du post
    cash_tag : cash_tag du post
    url : url du post
    content : contenu de l'article
    """

    def __init__(self):
        self.title = ""
        self.extracte_date = ""
        self.date_post = ""
        self.compagny_name = ""
        self.ticket_code = ""
        self.hash_tag = ""
        self.cash_tag = ""
        self.url = ""
        self.content = ""

    def set_title(self, title):
        """
        set the title of the current object
        """
        if check_data_exist(title) is True:
            self.title = title.text

    def set_extracte_date(self, extracte_date):
        """
        set the extracte_date of the current object
        """
        if extracte_date is not None:
            self.extracte_date = extracte_date

    def set_compagny_name(self, compagny_name):
        """
        set the compagny_name of the current object
        """
        if check_data_exist(compagny_name) is True:
            self.compagny_name = compagny_name.text

    def set_ticket_code(self, ticket_code):
        """
        set the ticket_code of the current object
        """
        if check_data_exist(ticket_code) is True:
            self.ticket_code = ticket_code.text

    def set_date_post(self, date_post):
        """
        set the date_post of the current object
        """
        if check_data_exist(date_post) is True:
            self.date_post = date_post.text

    def add_hash_tag(self, hash_tags):
        """
        add hash_tag of the current object
        """
        for hash_tag in hash_tags:
            if check_data_exist(hash_tag) is True:
                self.hash_tag += hash_tag.text

    def add_cash_tag(self, cash_tags):
        """
        add cash_tag of the current object
        """
        for cash_tag in cash_tags:
            if check_data_exist(cash_tag) is True:
                self.cash_tag += cash_tag.text

    def set_url(self, url):
        """
        set the url of the current object
        """
        if url is not None:
            self.url = url

    def set_content(self, content):
        """
        set the content of the current object
        """
        if check_data_exist(content) is True:
            self.content = content.text
