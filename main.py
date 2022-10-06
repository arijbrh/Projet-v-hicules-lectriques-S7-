import pandas as pd
df1 = pd.read_csv ('consolidation-etalab-schema-irve-v-2.0.3-20221004.csv')
df2 = pd.read_csv('tmja-2019.csv', sep=";")
#print(df2.keys())
#print(df2['TMJA'])
df2.to_excel('trafficdata.xlsx')