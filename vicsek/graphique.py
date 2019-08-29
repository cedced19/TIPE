#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from lib import angle_vers_vecteur
import glob
import sys

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



def sauvegarde_graphique(file, eta):

	# axes de 0 à 1
	plt.axis([0,1,0,1])

	# supprime l'affichage des ticks
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])

	# titre 
	plt.title("$\eta$ = %.2f" % eta)

	# sauvegarde
	plt.savefig("graph/%s.jpg" % file[7:-4])
	plt.close()

	# efface pour le prochain graph
	plt.cla()

	return


eta = float(sys.argv[2])


for file in glob.glob("coords/*.txt"):
	print(file[7:])

	mat = np.loadtxt(file)
	coords = mat[:,0:2]
	thetas = mat[:,2]
	dessine_vecteur(coords, thetas)
	sauvegarde_graphique(file, eta)
