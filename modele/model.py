import pandas as pd
from pandasql import sqldf

def load_data():
  return pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')



def get_vente_par_region():
  données = load_data()
  query = "SELECT region, SUM(qte) AS vente FROM données GROUP BY region"
  return sqldf(query, locals())


def get_vente_par_produit():
  données = load_data()
  query = "SELECT produit, SUM(qte) AS vente FROM données GROUP BY produit"
  
  return sqldf(query, locals())


def get_chiffre_affaire_par_produit():
  données = load_data()
  query = "SELECT produit, SUM(prix * qte) AS chiffre_affaires FROM données GROUP BY produit"
  return sqldf(query, locals())