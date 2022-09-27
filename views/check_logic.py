#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:03:07 2021

@author: pdm
"""

import pandas as pd



path='/home/pdm/Documents/ADSN/RCMS/ADSN_RMCS_23-12-2021/CSV/RepairLifeCycleEntry.csv'
df = pd.read_csv(path)
df["Values"]=1
print(df.columns)
pv = pd.pivot_table(df, index=['partnumber'], columns=["TaskStatus"],values=["Values"], aggfunc=sum, fill_value=0)


print(df)
print(pv)