#!/usr/bin/python
# -*- coding: ISO-8859-15 -*-
import os

UN_MEGA = 1024*1024
def scan_rep(repertoire, extension):
    """ scan le repertoire courant a la recherche
    de fichiers de plus de 1mo """
    for racine, reps, fichiers in os.walk(repertoire, topdown=True):
        for fichier in fichiers:
            if fichier.endswith('.%s' % extension):
                nom_complet = os.path.join(racine, fichier)
                taille = os.path.getsize(nom_complet)
                if taille >= UN_MEGA:
                    print('%s : %.2f Mo' % \
                          (nom_complet, taille/float(UN_MEGA)))
if __name__ == '__main__':
    a=input("Saisir le repertoire a chercher :\t")
    scan_rep(a, 'log')
    os.system("pause")
