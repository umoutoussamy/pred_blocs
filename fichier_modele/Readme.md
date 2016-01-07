# Nouvelle méthode de prédiction de Protein Blocks (NMPPB)

Ce programme permet de produire des modéle pour la prédiction de proteine blocs.
 Il a été réalisé dans le cadre d'un projet long
pour le Master M2BI de l'Université Paris Diderot.

## Contents

1. Projet_long_5_MOUTOUSSAMY

  1.1 aamtx ->  dossier ou seront ajouter l'ensemble des fichiers pssm

  1.2 pir_pb  ->  dossier ou seront ajouter l'ensemble des fichiers des blocs

  1.3 fichier_modele  ->  contient l'ensemble des scripts
2. Readme.txt
3. Rapport_projet_5_MOUTOUSSAMY.pdf

## Overview

  Ce programme permet de produire 2 types de modéle. Un modéle dit SVM, car il 
  utilise des programme SVM (support vecteur machine, et des modéle MLP, 
  utilisant des programmes de reseau de neurone.


  Format de fichier nécéssaire:

    .aamtx : 
    tout les fichiers aamtx (pssm) doivent se trouver dans le dossier aamtx
    ce sont les fichier contenant les information que nous allons utiliser pour 
    l'apprentissage et la prediction.

    .pir_pb :
    tout les fichiers pir_pb doivent se trouver dans le fichier pir_pb, ce sont
    des fichier contenant la sequence en bloque correspondant à chaque proteine 
    de la pssm (aamtx)


## System requirements

 NMPPB nécessite python, il a été développé sous Macintosh, mais est 
   multi-plate-forme.

   Il nécessite les modules suivant:
  
   Modules  Actions
  ----------------------------------------------------------------------------
    sys   passage d'arguments, gestion de l'entrée/sortie standard...
    os    dialogue avec le système d'exploitation.
    numpy   fonctions d’ algèbre linéaire...
    LIBSVM  fonction d'apprentissage 

Pour l’installation de numpy peut importe le système d’exploitation: 

  http://docs.scipy.org/doc/numpy/user/install.html

et suivre les instructions.

Pour l’installation de LIBSVM : 

## Notes on use

Le dossier comporte le script bash suivant : luncher.sh, qui permet de lancer 
presque l'ensemble des programmes, mais il néssésite l'utilisation d'un tag 
(en argument), afin de pouvoir produire le modéle désiré:

  Argument  Type              Description
  ----------------------------------------------------------------------------
  -svm            support vecteur     Indique que l'on veut un modéle type svm
      machine

  -mlp      multi layer       Indique que l'on veut un modéle type mlp
      perceptron   

  !ATTENTION!  Les balises précédente ne peuvent pas être cumulée  !ATTENTION!  


exemple : ./luncher.sh              —> incorrecte
      ./luncher.sh  -svm -mlp   —> incorrecte


      ./luncher.sh  -svm      —> correcte
      ./luncher.sh  -mlp      —> correcte

## Extension et traitement du sujet

Sujet : 
  Le sujet n’a pas été traité dans son intégralité :

  La première partie: le modéle SVM ne prend pas en compte le poids de chaque 
  classe

  La seconde partie: le modéle MLP prend en compte le poids de chaque classe, 
  mais elle n'est pas optimisé, les classes les moins présente prennent plus
  de "place" aprés normalisation.

## Commande d’exécution du fichier
1) Décompresser le fichier

  Placer le fichier « Projet_long_5_MOUTOUSSAMY.tar.gz » sur le bureau, 
  et faire un double clic pour le décompresser.

  2) Trouver le fichier
  
  Tout d’abord, changer le directory (dans le terminal) pour vous rendre dans 
  le fichier « Projet_long_5_MOUTOUSSAMY ». Si vous ouvrez le terminal et que 
  le fichier se trouve sur le bureau, taper :
 
    cd Desktop/all_files_projet_5_MOUTOUSSAMY/Projet_long_5_MOUTOUSSAMY

  Si vous vous trouvez déjà sur le bureau, taper uniquement :

    cd all_files_projet_5_MOUTOUSSAMY/Projet_long_5_MOUTOUSSAMY

  3) Lancer le programme 

  Pour lancer le programme, taper les ligne de commande suivante : 

    cd fichier_modele

    ./luncher.sh  -svm 

  Le fichier bash va automatiquement produire les donnée nécéssaire et les 
  resultas. ATTENTION !!!! les resultats ne seront pas sauvegarder !!!
 

résumer : décompression/désarchivage 

    cd all_files_projet_5_MOUTOUSSAMY/Projet_long_5_MOUTOUSSAMY
    cd fichier_modele
    ./luncher.sh  -svm

## Contact



Auteur : Igor Ulrich MOUTOUSSAMY

Email : umoutoussamy@gmail.com