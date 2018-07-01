#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:22:39 2017

filename: run_application.py

description: Main file to run dashboard application

author: Timo Klingler
"""

import dashboard

import webbrowser

url = "http://127.0.0.1:8050"
webbrowser.get('safari').open(url, new = 2)

dashboard.app.run_server()
