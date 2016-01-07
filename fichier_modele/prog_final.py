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
#import Tkinter
#import random
import pylearn2
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

	-pssm		balise		    Indique le fichier d'entrée PSSM 
					    (Suivie de la PSSM) 

	-blocks		balise		    Indique le fichier d'information blocks 
					    (Suivie du fichier d'allignement standart)
	 
	""")

def check_args():
	"""Cette fonction permet de contrôler les arguments passer à la ligne de 
	commande.
	Retourne: une liste conteant les argument : 
	[seq, nombre_de_pas, temp]
	"""
	args = [0, 0, 0] # liste permettant de stocker les arguments
	j = 0
	for i in range(len(sys.argv)): # Parcourt des argument
		if sys.argv[i] == "-svm": #test le mode 1
			j = j+1	

		if sys.argv[i] == "-mlp": #test le mode 2
			j = j+2

		if sys.argv[i] == "-pssm": #test le fichier pssm
			j = j+3
			args[0] = sys.argv[i + 1]
		if sys.argv[i] == "-blocks": #test le fichier "blocks"
			j = j+4
			args[1] = sys.argv[i + 1]
			pass

	# Affichage d'un message d'erreur si aucun fichier .xtc n'est donné
	#print j

	if j < 8 or j > 9 :
		error_args()
		pass
	elif j == 8:
		args[2] = 8
		pass
	else:
		args[2] = 9
		pass
	#print args
	if args[0] == 0 or args[1] == 0 or args[2] == 0: 
			error_args()
			pass
	return args

#========================|FONCTIONS PREPARATION FICHIER|========================

def isole_seq(blocks_file):
	"""
	"""
	file_blocks = open(blocks_file, "r")
	i = 0
	outf = open("%sblocks_1"%blocks_file[:-6], "w")
	for ligne in file_blocks.readlines() :
		if i > 1:
			if ligne[0]==">":
				break
			else :
				outf.write(ligne)
				print ligne
				pass
			pass
		i = i+1
	file_blocks.close()

def reduit_seq(blocks_file):
	"""
	"""
	blocks_1 = open("%sblocks_1"%blocks_file[:-6], "r")
	i = 0
	outf = open("%sblocks_2"%blocks_file[:-6], "w")
	for ligne in blocks_1.readlines() :
		if i == 0:
			temp = ligne[5:]
			outf.write(temp)
			pass
		elif ligne[-2] == '*':
			temp = ligne[:-7]
			outf.write(temp)
			pass
		else:
			outf.write(ligne)
		i = i+1
	outf.close()
	blocks_1.close()

def conver_blocks_num(blocks_file):
	"""
	"""
	seq_block = open("%sblocks_2"%blocks_file[:-6], "r")
			
	outf = open("%sblocks_3"%blocks_file[:-6], "w")
	
	for ligne in seq_block:
		for i in xrange(len(ligne)):
			if ligne[i] == '-':
				outf.write("0" + "\n")
				pass
			elif ligne[i] == 'p':
				outf.write("1" + "\n")
				pass
			elif ligne[i] == 'f':
				outf.write("2" + "\n")
				pass
			elif ligne[i] == 'b':
				outf.write("3" + "\n")
				pass
			elif ligne[i] == 'e':
				outf.write("4" + "\n")
				pass
			elif ligne[i] == 'c':
				outf.write("5" + "\n")
				pass
			elif ligne[i] == 'd':
				outf.write("6" + '\n')
				pass
			elif ligne[i] == 'h':
				outf.write("7" + '\n')
				pass
			elif ligne[i] == 'i':
				outf.write("8" + '\n')
				pass
			elif ligne[i] == 'a':
				outf.write("9" + '\n')
				pass
			elif ligne[i] == 'k':
				outf.write("10" + '\n')
				pass
			elif ligne[i] == 'l':
				outf.write("11" + '\n')
				pass
			elif ligne[i] == 'm':
				outf.write("12" + '\n')
				pass
			elif ligne[i] == 'g':
				outf.write("13" + '\n')
				pass
			elif ligne[i] == 'o':
				outf.write("14" + '\n')
				pass
			elif ligne[i] == 'n':
				outf.write("15" + '\n')
				pass
			elif ligne[i] == 'j':
				outf.write("16" + '\n')
				pass
			else :
				pass
		 	pass
		pass
	pass

def produit_files_pred(blocks_file, pssm_file):
	"""
	"""
	mtx = np.genfromtxt("%s"%pssm_file)
	nac = np.genfromtxt("%sblocks_3"%blocks_file[:-6])
	print nac

	outf = open("entree_libsvm.block", "w")
	outf2 = open("entree_mlp.block", "w")

	for i, ligne in enumerate(nac):  
		li = (ligne)
		li2 = (ligne)
        
        # get the 20*11 vector
		for j, el in enumerate(np.asarray(mtx[i:i+11,:]).reshape(-1)):
			j = j+1
			print j
			li = "%s %i:%.3f"%(li, j, el)
			li2 = "%s %.3f"%(li2, el)
		outf.write(li + "\n")
		outf2.write(li2 + "\n")
	outf.close()
	outf2.close()

def fct_svm():
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

	pssm_file = args_check[0]
	blocks_file = args_check[1]
	mode_predic = args_check[2]

	#print args_check[1]

	isole_seq(blocks_file)
	reduit_seq(blocks_file)
	conver_blocks_num(blocks_file)
	produit_files_pred(blocks_file, pssm_file)
	

	if mode_predic == 8: #svm mode
		fct_svm()
		pass

	else : 
		
		pass











