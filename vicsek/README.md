# Modèle de Vicsek

Générer les coordonnées
```
python3 main.py N eta rayon gen_graph
```
où `gen_graph` prend la valeur 0 ou 1

Générer les graphiques
```
python3 graphique.py N eta rayon
```

Générer un film
```
ffmpeg -framerate 4 -pattern_type glob -i "*.jpg" output1.mp4
```
