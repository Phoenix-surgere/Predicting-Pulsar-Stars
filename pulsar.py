# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:30:41 2020

@author: black
This seems like a super interesting dataset, EDA + Model- wise
"""

import pandas as pd
import zipfile
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

seed = 443
np.random.seed(seed)

zf = zipfile.ZipFile('pulsars.zip') 
pulsars = pd.read_csv(zf.open('pulsar_stars.csv'))

print(pulsars.info())
print(pulsars.columns)
print(pulsars.describe())