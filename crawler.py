#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:10:13 2017

filename: crawler.py

description: Web crawler to fetch data from the I-ELCAP database

author: Timo Klingler
"""

import query
import credentials

from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import os.path
from time import strftime

def run_crawler(url, inst, user, pwd):

    # Initialize Webdriver and Input Login Information
    print("Initializing crawler...")
    browser = webdriver.PhantomJS()

    browser.get(url)

    institution = Select(browser.find_element_by_name("inst"))
    username = browser.find_element_by_name("instkey")
    password = browser.find_element_by_name("perskey")
    submit = browser.find_element_by_xpath("//input[@type='button']")

    sleep(randint(2, 10))
    institution.select_by_value(str(inst))
    username.send_keys(str(user))
    password.send_keys(str(pwd))
    submit.click()
    print("Login complete.")

    # Administration Page

    sleep(randint(2, 10))
    administration = browser.find_element_by_xpath("//input[@value='Administration']")
    administration.click()
    print("Step 1 complete.")

    # Next Page

    sleep(randint(2, 10))
    database = browser.find_element_by_xpath("//input[@value = 'Database Search']")
    database.click()
    print("Step 2 complete.")

    # Database Page

    sleep(randint(2, 10))
    search = browser.find_element_by_name("sf_aq")
    submit_query = browser.find_element_by_xpath("//input[@value='Submit Search']")

    search.send_keys(query.run_query(query.query_dict))
    submit_query.click()
    print("Input complete.")

    # Get Xpath

    get_xpath = browser.page_source
    get_xpath = BeautifulSoup(get_xpath, 'lxml')
    get_xpath = get_xpath.find_all("a", attrs = {"href": re.compile("javascript:subViewResult")})

    xpath_list = []

    for item in get_xpath:
        xpath_list.append(item.get_text())

    xpath_no = xpath_list[xpath_list.index('NEXT>') - 1]

    print("Found Xpath Key.")

    # Get CT Evaluation

    show_results = browser.find_element_by_xpath('//*[@id="pagedone"]/p[2]/table[1]/tbody/tr[3]/td/center/a[' + xpath_no + ']')
    show_results.click()

    html = browser.page_source
    get_data = BeautifulSoup(html, 'lxml')
    get_data

    table = get_data.find("div", attrs = {'id':'pagedone'})
    table = table.find("tbody")
    text_list = []

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [element.text.strip() for element in cols]
        text_list.append([element for element in cols if element]) # Get rid of empty values

    text_list = [item for item in text_list if len(item) > 1]
    text_list = text_list[2:]
    text_list = [[word.replace('-', '') for word in item] for item in text_list]
    text_list = [item for item in text_list if len(item) > 2]

    headers = ["Study ID", "SR", "Last Name", "First Name", "MRN", "Intake", "IR", "CT Evaluation", "CR"]
    df = pd.DataFrame(text_list, columns = headers)
    df.drop(["SR", "IR", "CR"], axis = 1, inplace = True)

    df[df == ''] = np.NaN
    df = df.fillna(method='ffill')

    df["Intake"] = pd.to_datetime(df["Intake"])
    df["CT Evaluation"] = pd.to_datetime(df["CT Evaluation"])

    df = df.sort_values(by = "CT Evaluation", ascending = False)

    df.to_csv("update.csv")

    print("CT Evaluations scraped.")

    # Download Data

    sleep(randint(2, 10))
    download = browser.find_element_by_xpath("//input[@value='Download Data']")
    download.click()
    print("Download complete.")

     # Close Crawler
    sleep(randint(2, 10))
    if os.path.exists(credentials.path_cwd + "/update.csv"):
        browser.quit()
        print("Crawling complete.")

    return
