#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb

class Mysql:
    """
    db_sql : varible to make bdd insert
    db_table : name of the table vill be get data object
    """

    def __init__(self, server = 'db', user='root', pwd='root'):
        self.db = MySQLdb.connect(server, user, pwd)
        self.cursor = self.db.cursor()
        sql = """CREATE DATABASE IF NOT EXISTS businesswire;"""
        self.cursor.execute(sql)

    def add_data(self, data):
        print("Data => " + data.url)

    def __del__(self):
        self.close()
