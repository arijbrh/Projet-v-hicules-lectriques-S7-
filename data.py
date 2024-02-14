import pandas as pd
import numpy as np
import plotly.express as px

"""///traitement df1///"""

df1 = pd.read_csv ('consolidation-etalab-schema-irve-v-2.1.0-20230114.csv') #datachargingstations
#df1.to_excel('chargingstations.xlsx')

df1['id']=df1['consolidated_code_postal']
def clean(x):
    x= x//1000
    return x
df1['id']=df1['id'].apply(clean)
#df1=df1['id'].value_counts().reset_index(name='counts')
#print(df1[df1['index'].isnull()])
#df1['index']=df1['index'].astype(int)
#df1['id']=df1['id'].astype(int)
df1=df1.groupby('id').sum().reset_index()
df1=df1[['id','nbre_pdc']]
df1['id']=df1['id'].astype(int)
#df1.to_excel('chargingstationsgroupby.xlsx')
#df1['id']=df1['code_insee_commune']
#df1 = df1.astype(dtype= {"id":"str"})

#def clean(x):
#    x= x[0:2]
#   return x
#df1['id']=df1['id'].apply(clean)
#df1=df1['id'].value_counts().reset_index(name='counts')
#df1['scalecount']=np.log10(df1['counts'])


#df1.to_excel('chargingstations2.xlsx')

"""fin traitement df1"""



"""traitement df2 et df5"""
#df2.to_excel('trafficdata.xlsx')
df2 = pd.read_csv ('tmja-2019.csv', sep=";") #datatrafic
df5=df2[['depPrD','TMJA']]
df5=df5.groupby('depPrD').sum().reset_index()
df5.rename(columns={'depPrD':'depart'}, inplace=True)

"""fin traitement df2 et df5"""


"""traitement df3"""
df3 =pd.read_csv('Departements.csv', sep=";") #datapopulations

df3.drop(df3[df3['CODDEP'] =='2A'].index, inplace = True)
df3.drop(df3[df3['CODDEP'] =='2B'].index, inplace = True)
df3.drop(df3[df3['CODDEP'] =='na'].index, inplace = True)
df3 = df3.astype(dtype= {"CODDEP":"int64"})
df3.rename(columns={'CODDEP':'depart'}, inplace=True)
#df3.to_excel('departementsdata.xlsx')
"""fin traitement df3"""





df4=pd.read_excel('vehiculesfrance.xlsx')
df4.drop(df4[df4['depart'] =='2A'].index, inplace = True)
df4.drop(df4[df4['depart'] =='2B'].index, inplace = True)
df4.drop(df4[df4['depart'] =='na'].index, inplace = True)
df4 = df4.astype(dtype= {"depart":"int64", "nb_vp_rechargeables_el":"int64","nb_vp_rechargeables_gaz":"int64","nb_vp":"int64"})


df1.rename(columns={'id':'depart'}, inplace=True)
df1.drop(df1[df1['depart'] =='2A'].index, inplace = True)
df1.drop(df1[df1['depart'] =='2B'].index, inplace = True)
df1.drop(df1[df1['depart'] =='na'].index, inplace = True)

df1 = df1.astype(dtype= {"depart":"int64"})
result = pd.merge(df5, df1, on="depart")
df5=result #trafic et bornes de recharge
df5['logtraffic']=np.log10(df5['TMJA'])
df5['metric']=np.log10(df5['nbre_pdc'])/df5['logtraffic']
#df5.to_excel('trafficpardepartement.xlsx')
"""fin traitement df4 et df5merged"""

"""traitement df6 gdp"""
df6=pd.read_excel('scoringdata.xlsx')
df6 = df6.astype(dtype= {"depart":"int64", "gdp":"int64"})

#df1.to_excel('chargingstationsdf1todelete.xlsx')

#print(df1)
print(df4.dtypes)
#print(df5.head())
#print(df4.dtypes)
#print(df5.dtypes)
