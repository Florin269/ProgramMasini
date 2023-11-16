import csv 
import os 
import pandas as pd

CALE_FISIER = "curs17/"

def afisare_masini_judet(localitate):
    df = pd.read_csv(CALE_FISIER + 'masini.csv')
    df = df[(df['JUDET'].str.match(localitate))]
    df = df['TOTAL_VEHICULE'].sum()
    return df


# print(afisare_masini_judet())


def afisare_masini_categorie(categorie):
    df = pd.read_csv(CALE_FISIER + 'masini.csv',keep_default_na=False)
    df = df[(df['CATEGORIE_COMUNITARA'].str.match(categorie))]
    df = df['TOTAL_VEHICULE'].sum()
    return df

# print(afisare_masini_categorie()) 

def afisare_masini_nr():
    df =pd.read_csv(CALE_FISIER + 'masini.csv',keep_default_na=False )
    df = df[df['TOTAL_VEHICULE'] > 10]
    rezultat = df[['MARCA','TOTAL_VEHICULE']]
    return rezultat 


# print(afisare_masini_nr())