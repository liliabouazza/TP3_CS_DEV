#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:23:31 2023

@author: cyril.recordon
"""

"""
Affichage par Tkinter
Lilia Bouazza - Cyril Recordon
02/10/2023
Todo: rajouter les canvas
"""
from tkinter import Tk,StringVar,Label,Button,Entry,Frame,PhotoImage



def affichage_mot(mot_cache):
    mot_cache.set(mot_cache)


#Creation de la fenetre principale du jeu
JeuPendu = Tk()
JeuPendu.title('Jeu du pendu')
JeuPendu.geometry('500x500+300+300')

#Creation du widget mot a deviner
mot_cache = StringVar()
affichage_mot(mot_cache)
labelMot = Label(JeuPendu, textvariable = mot_cache, fg = 'red')
labelMot.pack(side = 'top', pady = 5)


#Creation d'un bouton pour quitter
bouttonQuitter = Button(JeuPendu, text='Quitter', command=JeuPendu.destroy)
bouttonQuitter.pack(side ='bottom', pady = 5)

#Creation du bouton pour proposer la lettre
bouttonProposer = Button(JeuPendu, text = 'proposer',)
bouttonProposer.pack(side = 'bottom', pady = 5)

#Creation du widget d'entrée
lettre = Entry (JeuPendu, textvariable='lettre',bg='grey',fg='white')
lettre.pack(side = 'bottom', pady = 5)

#Creation d'un label
labelIndication = Label(JeuPendu, text='propsez une lettre :', fg='blue')
labelIndication.pack(side='bottom', pady = 5)

#Creation d'une sous-fenetre
sousFenetre = Frame (JeuPendu,borderwidth = 5, relief = 'groove', bg = 'black')
sousFenetre.pack(side = 'right' )

#Creation du canvas
Image = PhotoImage(file = "bonhomme1.gif")


JeuPendu.mainloop()