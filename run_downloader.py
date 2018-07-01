#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:25:22 2017

filename: run_downloader.py

description: Main file to execute crawler

author: Timo Klingler
"""

import crawler
import credentials

crawler.run_crawler(credentials.url, 
                    credentials.inst, 
                    credentials.user, 
                    credentials.pwd)
