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

#===============================  FONCTIONS  ===================================
#===============================================================================
def isole_seq(blocks_file):
	"""
	Cette fonction permet d'isoler la sequence des blocs, elle prend en entrée 

	Retourne: 1 fichiers formatée contenant uniquement la sequence. (*bloc_1)
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
				pass
			pass
		i = i+1
	file_blocks.close()

def reduit_seq(blocks_file):
	"""
	Cette fonction permet d'isoler la sequence des blocs condante (sans les 5 
	premier et dernier blocs), elle prend en entrée le fichier formater *bloc_1 

	Retourne: 1 fichiers formatée contenant uniquement la sequence. (*bloc_2)
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
	Cette fonction permet de codé la sequence en classe de 0 à 16, pour chaque
	bloc, et les dispose en colonne. 
	Elle prend en entrée le fichier formater *bloc_2 

	Retourne: 1 fichiers formatée contenant uniquement la sequence. (*bloc_3)
	"""
	seq_block = open("%sblocks_2"%blocks_file[:-6], "r")
			
	outf = open("%sblocks_3"%blocks_file[:-6], "w")
	
	for ligne in seq_block:
		for i in xrange(len(ligne)):
			if ligne[i] == '-':
				outf.write("0" + "\n")
				pass
			elif ligne[i] == 'a':
				outf.write("1" + "\n")
				pass
			elif ligne[i] == 'b':
				outf.write("2" + "\n")
				pass
			elif ligne[i] == 'c':
				outf.write("3" + "\n")
				pass
			elif ligne[i] == 'd':
				outf.write("4" + "\n")
				pass
			elif ligne[i] == 'e':
				outf.write("5" + "\n")
				pass
			elif ligne[i] == 'f':
				outf.write("6" + '\n')
				pass
			elif ligne[i] == 'g':
				outf.write("7" + '\n')
				pass
			elif ligne[i] == 'h':
				outf.write("8" + '\n')
				pass
			elif ligne[i] == 'i':
				outf.write("9" + '\n')
				pass
			elif ligne[i] == 'j':
				outf.write("10" + '\n')
				pass
			elif ligne[i] == 'k':
				outf.write("11" + '\n')
				pass
			elif ligne[i] == 'l':
				outf.write("12" + '\n')
				pass
			elif ligne[i] == 'm':
				outf.write("13" + '\n')
				pass
			elif ligne[i] == 'n':
				outf.write("14" + '\n')
				pass
			elif ligne[i] == 'o':
				outf.write("15" + '\n')
				pass
			elif ligne[i] == 'p':
				outf.write("16" + '\n')
				pass
			else :
				pass
		 	pass
		pass
	pass

#=================================  MAIN  ======================================
#===============================================================================

if __name__ == '__main__':

	blocks_file = sys.argv[1]
	isole_seq(blocks_file)
	reduit_seq(blocks_file)
	conver_blocks_num(blocks_file)




