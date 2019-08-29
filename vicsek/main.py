#!/usr/bin/python3
import numpy as np
from lib import *
import sys
import matplotlib.pyplot as plt

# Génération des graphique en une fois
def dessine_vecteur(coords, thetas):

	# couleur aléatoire
	couleurs = ["b", "g", "y", "m", "c", "pink", "purple", "seagreen",
			"salmon", "orange", "paleturquoise", "midnightblue",
			"crimson", "lavender"]

	
	for i,(x,y) in enumerate(coords):

		c = couleurs[i % len(couleurs)]

		# point	
		plt.scatter(x,y,color=c,marker=".")

		# queue
		theta = thetas[i]
		v = angle_vers_vecteur(theta)
		x1 = x - (0.025 * v[0])
		y1 = y - (0.025 * v[1])
		plt.plot([x,x1], [y,y1], color=c)

	return



def sauvegarde_graphique(path, N, eta, r):

	# axes de 0 à 1
	plt.axis([0,1,0,1])

	# supprime l'affichage des ticks
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])

	# titre 
	plt.title("$\eta$ = " + str(eta) + " N = " + str(N) + " r = " + str(r))

	# sauvegarde
	plt.savefig(path)
	plt.close()

	# efface pour le prochain graph
	plt.cla()

	return

# générer directement les graphiques
gen_graph = int(sys.argv[4])

# nombre de particule
N = int(sys.argv[1])

# intensité du bruit
eta = float(sys.argv[2])

# rayon dans lequel chercher des voisins
r = float(sys.argv[3])


delta_t = 0.05

# temps
t = 0.
# borne supérieur du temps
T = 5.

# Ici chaque poisson a un numéro pour pouvoir récuppérer leur vitesse et leur position

# Création de coordonnées des particules (ici poisson)
# particules[i][0] = x (compris entre 0 et 1)
# particules[i][1] = y  (compris entre 0 et 1)
particules = np.random.uniform(0,1,size=(N,2))


# Création d'angles aléatoires (pris entre -π et π) pour chaque vecteur vitesse des poissons
thetas = np.zeros((N,1))
for i,theta in enumerate(thetas):
	thetas[i,0] = angle_aleatoire()

while t < T:

	progress = round(t/T * 100)
	sys.stdout.write("Progression: %d%%   \r" % (progress) )
	sys.stdout.flush()
	
	if (gen_graph):
		dessine_vecteur(particules, thetas)
		sauvegarde_graphique("graph/%.2f.jpg" % t, N, eta, r)
	else:
		output = np.concatenate((particules,thetas),axis=1)
		np.savetxt("coords/%.2f.txt" % t, output)


	for i,(x,y) in enumerate(particules):

		# Obtention du voisinage de la particule
		voisinage = voisins(particules, r, x, y)

		# Obtention de la moyenne des angles du voisinage
		moy = moyenne(thetas, voisinage)

		# Obtention du vecteur bruit aléatoire
		nx = angle_aleatoire()
		ny = angle_aleatoire()
		bruit = eta * np.array([nx,ny])


		particules[i,:] += delta_t * (moy + bruit)
		thetas[i] = vecteur_vers_angle(moy + bruit)

		# Vérifier que les coordonnées soient bien entre 0 et 1 
		if particules[i,0] < 0:
			particules[i,0] = 1 + particules[i,0]

		if particules[i,0] > 1:
			particules[i,0] = particules[i,0] - 1

		if particules[i,1] < 0:
			particules[i,1] = 1 + particules[i,1]

		if particules[i,1] > 1:
			particules[i,1] = particules[i,1] - 1

	
	t += delta_t