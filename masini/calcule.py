import pandas
import os
import csv 

CALE = 'curs17/'

def calculeza_total_masini():
    df = pandas.read_csv(CALE + 'masini.csv')
    suma = df['TOTAL_VEHICULE'].sum()
    return suma

# print(calculeza_total_masini())

def calculeaza_total_masini_judet(judet):
    df = pandas.read_csv(CALE + 'masini.csv',keep_default_na=False)
    df = df[(df['JUDET'].str.match(judet))]
    df = df['TOTAL_VEHICULE'].sum()
    return df

# print(calculeaza_total_masini_judet('ALBA'))

def calculeaza_total_masini_catcom(categorie):
    df = pandas.read_csv(CALE + 'masini.csv',keep_default_na=False)
    df = df[(df['CATEGORIE_COMUNITARA'].str.match(categorie))]
    df = df['TOTAL_VEHICULE'].sum()
    return df

# print(calculeaza_total_masini_catcom('M3'))

def calculeaza_total_masini_comb(combustibil):
    df = pandas.read_csv(CALE + 'masini.csv',keep_default_na=False)
    df = df[(df['VALUE_NAME'].str.match(combustibil))]
    df = df['TOTAL_VEHICULE'].sum()
    return df

# print(calculeaza_total_masini_comb('BENZINA'))

