#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:37:02 2017

filename: xlsconvert.py

description: Convert broken xls file to csv and move it to working directory

author: Timo Klingler
"""

import credentials
import subprocess
from time import strftime

def run_xlsconvert():

    filename = "search-" + strftime("%d-%b-%Y") + ".xls"
    subprocess.call(["ssconvert", filename, "data.csv"], cwd = credentials.path_download)
    subprocess.call(["mv", credentials.csv, credentials.path_cwd], cwd = credentials.path_download)
    print("Conversion to .csv complete.")

