#!/usr/bin/python
import numpy as np 
from math import atan2, pi, sin, cos, sqrt

def vecteur_vers_angle(v):
	x = v[0]
	y = v[1]
	return atan2(y,x) # https://docs.python.org/3/library/math.html#math.atan2


# genérer un angle aléatoire entre -pi et pi
def angle_aleatoire():		
	theta = np.random.uniform(-pi,pi)
	return theta


def angle_vers_vecteur(theta):
	x = cos(theta)
	y = sin(theta)
	
	v1 = np.array([x,y])
	v2 = np.array([0,0])
	uv = vecteur_unitaire(v1,v2)

	return uv

def vecteur_unitaire(v1, v2):
	vecteur = v1 - v2
	dist = distance(v1[0], v1[1], v2[0],v2[1])
	uv = vecteur / dist
	return uv

def distance(x1, y1, x2, y2):
	return sqrt((x1 - x2)**2 + (y1 - y2)**2)



# renvoie tout les voisins et lui-même pour faire la moyenne
def voisins(particules, r, x0, y0):

	voisins = []

	for i,(x1,y1) in enumerate(particules):
		dist = distance(x0, y0, x1, y1)

		if dist < r:
			voisins.append(i)

	return voisins

def moyenne(thetas, voisins):
	
	n_voisins = len(voisins)
	moy_vecteur = np.zeros(2)

	for index in voisins:
		theta = thetas[index,0]
		theta_vec = angle_vers_vecteur(theta)
		moy_vecteur += theta_vec

	moy_vecteur = moy_vecteur / n_voisins

	return moy_vecteur