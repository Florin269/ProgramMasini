#converteste fisierul din csv in json 
#converteste fisierul in fisier text unde fiecare linie este de tipul "Vehicul de tip <CATEGORIE_NATIONALA> din judetul <JUDET> marca <MARCA>: <TOTALVEHICULE> <TOTAL
#converteste un fisier json primit ca parametru in fisier csv (pe caz general)

import os
import pandas
import csv 


CALE = 'curs17/'

def converteste_fisier():
    df=pandas.read_csv(CALE + 'masini.csv')
    df.to_json(CALE + 'masini.json', orient='records', lines=True)


# converteste_fisier()


def converteste_fisier_text():
   with open(CALE + 'masini.csv', 'r') as csv_file:
       lines=csv_file.readlines()


       with  open(CALE + 'masini.txt', 'w') as text_file:
           for line in lines:
               valoare = line.strip().split(',')
               linie_text = f"Vehicul de tip {valoare[3]} din judetul {valoare[1]} marca {valoare[4]}: {valoare[3]} {valoare[7]}\n"
               text_file.write(linie_text)

# converteste_fisier_text()

def converteste_json_to_csv(fisier_json):
    df=pandas.read_json(CALE + fisier_json)
    df.to_csv(CALE + 'exemplu.csv', index=False)


# converteste_json_to_csv('masinigeneral.json')

