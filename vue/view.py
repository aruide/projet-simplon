import plotly.graph_objects as go


def get_graph_vente_par_region(données_region):
  return go.Pie(labels=données_region['region'], values=données_region['vente'], name="quantité vendue par région")

def get_graph_vente_par_produit(données_produit):
  return go.Bar(x=données_produit['produit'], y=données_produit['vente'])

def get_graph_chiffre_affaire_par_produit(données_chiffre_affaire_produit):
  return go.Funnel(y=données_chiffre_affaire_produit['produit'], x=données_chiffre_affaire_produit['chiffre_affaires'])