#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:24:12 2021

@author: pdm
"""



import mysql.connector



conn = mysql.connector.connect(host='127.0.0.1',user='username', passwd='password',db='database_name')

print(conn)