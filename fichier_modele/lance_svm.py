#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Igor Ulrich MOUTOUSSAMY"
__version__  = "1.0.0"
__copyright__ = "copyleft"
__date__ = "2015/12"

#================================  MODULES  ====================================
#===============================================================================
import numpy as np 
import sys
import os
from svmutil import *

#===============================  FONCTIONS  ===================================
#===============================================================================

#==========================FONCTIONS DE VERIFICATIONS===========================
def error_args():
	"""Cette fonction permet d'afficher une message d'erreur. Ce message permet
	à l'utilisateur de prendre connaissance des arguments à entrer.
	"""
	sys.exit("""
	ERREUR! Les arguments donnés sont incorrect!
	Voici les arguments à entrer (dans l'ordre que vous souhaitez:

	Argument 	Type	       	    Description
	----------------------------------------------------------------------------
	-svm          	support vecteur     Indique que l'on veut un modéle type svm
			machine

	-mlp    	multi layer 	    Indique que l'on veut un modéle type mlp
			perceptron   

	!ATTENTION!  Les balises précédente ne peuvent pas être cumulée  !ATTENTION!  
	 
	""")

def check_args():
	"""Cette fonction permet de contrôler les arguments passer à la ligne de 
	commande.
	Retourne: une liste conteant les argument : 
	[mode]
	"""
	args = [0] # liste permettant de stocker les arguments
	j = 0
	for i in range(len(sys.argv)): # Parcourt des argument
		if sys.argv[i] == "-svm": #test le mode 1
			j = j+1	

		if sys.argv[i] == "-mlp": #test le mode 2
			j = j+2

	if j < 1 or j > 2 :
		error_args()
		pass
	elif j == 1:
		args[0] = 1
		pass
	else:
		args[0] = 2
		pass
	if args[0] == 0: 
			error_args()
			pass
	return args

#========================|FONCTIONS PREPARATION FICHIER|========================

def produit_files_pred():
	"""
	Cette fonction permet de produire les fichiers qui sous le format utilisé 
	par les 2 outils (Libsvm et Theanos)
	Elle ne prend aucun arguement en entrer, elle récupére directment les 
	fichiers dans le dossier
	Retourne: 2 fichiers formatée.
	"""
	mtx = np.genfromtxt('ensemble_fichier.aamtx')
	nac = np.genfromtxt('ensemble_fichier.pir_pb')
	#print nac

	outf = open("entree_libsvm.block", "w")
	outf2 = open("entree_mlp.block", "w")

	for i, ligne in enumerate(nac):  
		li = (ligne)
		li2 = (ligne)
        
        # get the 20*11 vector
		for j, el in enumerate(np.asarray(mtx[i:i+11,:]).reshape(-1)):
			j = j+1
			#print j
			li = "%s %i:%.3f"%(li, j, el)
			li2 = "%s %.3f"%(li2, el)
		outf.write(li + "\n")
		outf2.write(li2 + "\n")
	outf.close()
	outf2.close()

def fct_svm():
	"""
	Cette fonction permet d'effectuer l'apprentissage, de produire le modéle et 
	de tester le modéle.
	Elle ne prend aucun arguement en entrer, elle récupére directment les 
	fichiers dans le dossier. 
	Retourne: l'accuracy du modéle et le nombre de bien-prédit.
	"""
	y, x = svm_read_problem('./entree_libsvm.block')

	tot_ligne = len(y)

		# #apprentissage
	m = svm_train(y[:(tot_ligne/3*2)], x[:(tot_ligne/3*2)], '-c 4')

		# #Test de prediction
	p_label, p_acc, p_val = svm_predict(y[((tot_ligne/3*2)+1):tot_ligne], 
		x[((tot_ligne/3*2)+1):tot_ligne], m)



#=================================  MAIN  ======================================
#===============================================================================

if __name__ == '__main__':

	args_check = check_args() #Vérification les arguments rentrée

	mode_choix = args_check[0]

	#print args_check[1]

	produit_files_pred()
	

	if mode_choix  == 1: #svm mode
		fct_svm()
		pass

	else :
		print '''l\'implémentation du script de prediction mlp est toujours
		 en cour, pour le moment celui-ci est dans un fichier à part 
		 : mlp_16class.py'''
		pass

