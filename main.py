import pandas as pd
import numpy as np
import plotly.express as px
df1 = pd.read_csv ('consolidation-etalab-schema-irve-v-2.0.3-20221004.csv')
df2 = pd.read_csv('tmja-2019.csv', sep=";")
#print(df2.keys())
#print(df2['TMJA'])
#df2.to_excel('trafficdata.xlsx')
#print(df1)
#df1.to_excel('chargingstations.xlsx')
df3 =pd.read_csv('Departements.csv', sep=";")
#df3.to_excel('departementsdata.xlsx')

