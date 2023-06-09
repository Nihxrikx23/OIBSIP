# -*- coding: utf-8 -*-
"""UnemploymentAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dmqc1rQsRPSMMBUfrVLFIHP02MOUOZpG

**NAME:** Niharika Choudhari

**DOMAIN:** Data Science

**TASK:** Unemployement Analysis using Python

**COMPANY:** Oasis Infobyte

**BATCH:** April 2023
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

dataframe = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Unemployment in India.csv")
dataframe = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Unemployment_Rate_upto_11_2020.csv")

#Attributes in the dataset
dataframe.columns

#Top 5 rows in the dataset
dataframe.head(5)

#Check if the dataset has any null values
dataframe.isnull().sum()

#Visualizing the correlation between the features of dataset using a HEATMAP
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(6,4))
sns.heatmap(dataframe.corr())
plt.show()

#Analysing the estimated number of employment and unemployment rate by region
dataframe.columns = ["States", "Date", "Frequency", "Estimated Unemployment Rate",
                     "Estimated Employed", "Estimated Labour Participation Rate", "Region",
               "longitude","latitude"]
plt.title("Estimated Employed People in India")
sns.histplot(x = "Estimated Employed", hue = "Region", data = dataframe)
plt.show()

plt.title("Estimated Unemployed Rate in India")
sns.histplot(x = "Estimated Unemployment Rate", hue = "Region", data = dataframe)
plt.show()

#Dashboard to analyze the unemployment rate of each Indian State by region
unemployment = dataframe[["States", "Region", "Estimated Unemployment Rate"]]
fig = px.sunburst(unemployment, path = ["Region", 'States'], 
                  values = "Estimated Unemployment Rate",
                  width = 600, height = 600, color_continuous_scale = 'RdY1Gn',
                  title = "Unemployment Rate in India")
fig.show()