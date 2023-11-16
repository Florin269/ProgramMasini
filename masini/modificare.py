import pandas 

CALE ='curs17/'

def adauga_coloana_noua():
    df= pandas.read_csv(CALE + 'masini.csv')
    df['Popularitate'] = df['TOTAL_VEHICULE'].apply(lambda x: 'popular' if x > 100 else 'nepopular')
    df.to_csv(CALE + 'masini.csv', index=False)

# adauga_coloana_noua()


def modificare_judet():
    df=pandas.read_csv(CALE + 'masini.csv')
    județe_de_inlocuit = ["DOLJ", "OLT", "GORJ", "VALCEA", "MEHEDINTI"]
    df['JUDET'] = df['JUDET'].replace(județe_de_inlocuit,'Oltenia',regex=True)
    df.to_csv(CALE +'masini.csv', index=False)


# modificare_judet()

def modificare_benzina():
    df=pandas.read_csv(CALE + 'masini.csv')
    combustibil_de_inlocuit = ["BENZINA+GPL", "BENZINA+GNC"]
    df['VALUE_NAME'] = df['VALUE_NAME'].replace(combustibil_de_inlocuit[0],'BENZINA',regex=True)
    df.to_csv(CALE +'masini.csv', index=False)

# modificare_benzina()

