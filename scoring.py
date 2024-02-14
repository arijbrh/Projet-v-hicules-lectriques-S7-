import pandas as pd
import numpy as np
from data import df1, df3, df4, df5, df6
def scoring(depart):
    score=0
    #5 criteres: chargingstations, vehiculeselec, gpd, population, traffic
    def score1(depart): #score charging stations
        maxdf1=max(df1['nbre_pdc'].values)
        s = df1.at[df1.index[df1.depart==depart].values[0], 'nbre_pdc']/maxdf1
        return s
    def score2(depart): #score vehiculeselec
        maxdf4=max(df4['nb_vp_rechargeables_el'].values)
        if len(df4[df4.depart==depart]) > 0:
            s = df4.at[df4.index[df4.depart==depart].values[0], 'nb_vp_rechargeables_el']/maxdf4
        else:
            s = 0
        return s
    def score3(depart): #score traffic
        maxdf5=max(df5['TMJA'].values)
        if len(df5[df5.depart==depart]) > 0:
            s = df5.at[df5.index[df5.depart==depart].values[0], 'TMJA']/maxdf5
        else:
            s = 0
        return s
    def score4(depart): #score population
        maxdf3=max(df3['PTOT'].values)
        if len(df3[df3.depart==depart]) > 0:
            s = df3.at[df3.index[df3.depart==depart].values[0], 'PTOT']/maxdf3
        else:
            s = 0
        return s
    def score5(depart): #score pib
        maxdf6=max(df6['gdp'].values)
        if len(df6[df6.depart==depart]) > 0:
            s = df6.at[df6.index[df6.depart==depart].values[0], 'gdp']/maxdf6
        else:
            s = 0
        return s

    score= score1(depart)+score2(depart)+score3(depart)+score4(depart)+score5(depart)






    return score

def score1(depart): #score charging stations
    maxdf1=max(df1['nbre_pdc'].values)
    s = df1.at[df1.index[df1.depart==depart].values[0], 'nbre_pdc']/maxdf1
    return s
def score2(depart): #score vehiculeselec
    maxdf4=max(df4['nb_vp_rechargeables_el'].values)
    if len(df4[df4.depart==depart]) > 0:
        s = df4.at[df4.index[df4.depart==depart].values[0], 'nb_vp_rechargeables_el']/maxdf4
    else:
        s = 0
    return s
def score3(depart): #score traffic
    maxdf5=max(df5['TMJA'].values)
    if len(df5[df5.depart==depart]) > 0:
        s = df5.at[df5.index[df5.depart==depart].values[0], 'TMJA']/maxdf5
    else:
        s = 0
    return s
def score4(depart): #score population
    maxdf3=max(df3['PTOT'].values)
    if len(df3[df3.depart==depart]) > 0:
        s = df3.at[df3.index[df3.depart==depart].values[0], 'PTOT']/maxdf3
    else:
        s = 0
    return s
def score5(depart): #score pib
    maxdf6=max(df6['gdp'].values)
    if len(df6[df6.depart==depart]) > 0:
        s = df6.at[df6.index[df6.depart==depart].values[0], 'gdp']/maxdf6
    else:
        s = 0
    return s
print(scoring(5))

#add scoring to df1

df1 = df1.merge(df3[['depart','PTOT']], on='depart', how='left')
df1 = df1.merge(df4[['depart','nb_vp_rechargeables_el']], on='depart', how='left')
df1 = df1.merge(df5[['depart','TMJA']], on='depart', how='left')
df1=df1.merge(df6[['depart','gdp']], on='depart', how='left')
df1['score'] = df1['depart'].map(scoring)
df1['score1'] = df1['depart'].map(score1)
df1['score2'] = df1['depart'].map(score2)
df1['score3'] = df1['depart'].map(score3)
df1['score4'] = df1['depart'].map(score4)
df1['score5'] = df1['depart'].map(score5)



print(df1.head)
#df1.to_excel('scoringexcel.xlsx')