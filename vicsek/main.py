#!/usr/bin/python3
import numpy as np
from lib import *
import sys

# nombre de particule
N = int(sys.argv[1])

# intensité du bruit
eta = float(sys.argv[2])

# neighbor radius
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

	print(t)
	# save coordinates & corresponding thetas to text file
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