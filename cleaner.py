 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:18:55 2017¨

filename: cleaner.py

description: This file cleans the data set and makes it useable for analysis

@author: Timo
"""

import query
import variables
import credentials

import numpy as np
import pandas as pd

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

from genderize import Genderize

"""
Global Cleaning
"""

def clean_dataset(df):

    df["Last Name"] = df["Last Name"].apply(lambda x: hash(x))
    df["First Name"] = df["First Name"].apply(lambda x: hash(x))

    def rev_dict(dictionary):

        reversed_dict = {}
        rev_proc = dict([reversed(i) for i in dictionary.items()])
        reversed_dict.update(rev_proc)

        return reversed_dict

    def extract_dicts():

        dict_list = []

        for key in variables.var_dict.keys():
            if variables.var_dict[key] is None:
                pass
            else:
                dict_list.append(variables.var_dict[key])

        return dict_list

    def extract_colnames(dates = False):

        feature_names = []

        for key in variables.var_dict.keys():
            feature_names.append(key)

        if dates == True:
            return [s for s in feature_names if "Date" in s]
        else:
            return [s for s in feature_names if "Date" not in s]


    def feature_cleaner(df, names, dicts):

        for elem1, elem2 in zip(names, dicts):
            if sum(df[elem1].isnull()) != len(df[elem1].isnull()):
                df[elem1].replace(elem2, inplace = True)
            else:
                pass

        return df

    def date_cleaner(df, names):

        for element in names:
            df[str(element)] = pd.to_datetime(df[str(element)])

        return df

    df.columns = df.columns[:4].append(df.columns[4:].str.split(".").str[1])
    df.replace('-', np.nan, inplace = True)
    df.rename(columns = rev_dict(query.query_dict), inplace = True)

    df = feature_cleaner(df, extract_colnames(), extract_dicts())
    df = date_cleaner(df, extract_colnames(dates = True))

    return df

def run_local_cleaner(df, col, gender = False):

    def age_calculator(df, column):

        age_list = []
        sys_date = time.strftime("%Y-%m-%d")
        sys_date = datetime.strptime(sys_date, '%Y-%m-%d')

        for element in df[column]:
            if type(element) is pd._libs.tslib.Timestamp:
                age_list.append(relativedelta(sys_date, element).years)
            else:
                    age_list.append(element)

        return age_list

    def date_cleaner(df, names):

        for element in names:
            df[str(element)] = pd.to_datetime(df[str(element)])

    def get_gender(df, column):

        name_list = []
        genderdict_list = []
        gender_list = []

        for name in df[column]:
            name_list.append(name)

        name_list = [name_list[i:i + 10] for i in range(0, len(name_list), 10)]

        for element in name_list:
            genderdict_list.append(Genderize().get(element))

        for gender in genderdict_list:
            for key in gender:
                gender_list.append(key['gender'])

        return gender_list

    for name in col:
        if gender == True and name == "First Name":
            df["Gender"] = pd.Series(get_gender(df, name), index = df.index, name = "Gender")
        elif name == "Study ID":
            df = df[df['Study ID'].str.contains("[L][Z][R][0-9]+")]
        elif name == "Date of Birth":
            df.loc[name] = pd.Series(age_calculator(df, name), index = df.index)
            df = df.rename(columns = {"Date of Birth" : "Age"})
        elif name == "Radiologist":
            df = df[df[name] != "Dr. Nemo"] # Index at 214
        elif name == "Intake":
            date_cleaner(df, name)
        elif name == "CT Evaluation":
            date_cleaner(df, name)
        else:
            pass

    return df
#
df = pd.read_csv(credentials.csv)
df = clean_dataset(df)

collist = ["First Name", "Study ID", "Date of Birth", "Radiologist"]
df = run_local_cleaner(df, collist, gender = False)
