#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

class Mysql:
    """
    db_sql : varible to make bdd insert
    db_table : name of the table vill be get data object
    """

    def __def__(self, server = 'db', user='root', pwd='root'):
        self.table = "Scraper_businesswire"
        try:
            self.db_sql = mdb.connect(server, user, pwd)
        except mdb.Error:
            print("Error Mysql")
            sys.exit(1)
        sql = """CREATE DATABASE IF NOT EXISTS businesswire;"""
        self.db_sql.query(sql)

    def add_data(self, data):
        sql = """
CREATE DATABASE IF NOT EXISTS businesswire;
        """

