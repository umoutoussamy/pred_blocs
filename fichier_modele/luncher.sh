#!/bin/sh
# -*- coding: utf-8 -*-

# __author__ = "Igor Ulrich MOUTOUSSAMY"
# __version__  = "1.0.0"
# __copyright__ = "copyleft"
# __date__ = "2015/12"

#Recupére l'argument dans la ligne de commande pour le programme python 
args=("$@")


#========Production des fichiers d'entree des programmes de prédictions=========
cd ../aamtx

#produit le fichier .aamtx 
cat *.aamtx > ensemble_fichier.aamtx
cp ensemble_fichier.aamtx ../fichier_modele/.
rm ensemble_fichier.aamtx

cd ../pir_pb
#produit le fichier .pir_pb
for f in *.pir_pb
do
	./../fichier_modele/code_blocs.py $f
done

rm *blocks_1
rm *blocks_2
cat *blocks_3 > ensemble_fichier.pir_pb
cp ensemble_fichier.pir_pb ../fichier_modele/.
rm ensemble_fichier.pir_pb
rm *blocks_3

#========================Production des modéles et test=========================
cd ../fichier_modele

./lance_svm.py ${args[0]}

rm *block