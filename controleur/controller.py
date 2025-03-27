from modele import model
from vue import view
from plotly.subplots import  make_subplots

def run():
  
  données_region = model.get_vente_par_region()
  données_produit = model.get_vente_par_produit()
  données_chiffre_affaire_produit = model.get_chiffre_affaire_par_produit()
  
  graph =  make_subplots(rows=2, cols=2, subplot_titles=("quantité vendue par région","quantité de vente par produit","chiffre d'affaire par produit"), specs=[[{"type": "domain"}, {"type": "xy"}], [{"type": "xy"}, {"type": "xy"}]] )
  
  graph.add_trace(view.get_graph_vente_par_region(données_region), row=1, col=1)
  graph.add_trace(view.get_graph_vente_par_produit(données_produit), row=1, col=2)
  graph.add_trace(view.get_graph_chiffre_affaire_par_produit(données_chiffre_affaire_produit), row=2, col=1)
  
  graph.write_html("graphique-des-ventes.html")
  
  print('graphique-des-ventes.html généré avec succès !')
  return 0