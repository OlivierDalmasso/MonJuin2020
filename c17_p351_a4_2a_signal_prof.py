#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# 1C17 Activité 4                                                    CORRECTION
# Réaliser : Représentation d'un signal sinusoïdal
# Question 2 a et 2 b
# =============================================================================

import numpy  as np
from matplotlib import pyplot as plt
from math import pi

# =============================================================================
#                                        CORRECTION INITIATION ET INTERMEDIAIRE
# =============================================================================
"""
A = float(input('A = '))        # Amplitude en m
T = float(input('T = '))        # Période en s
tmax = float(input('tmax = '))  # Durée maximale en s

t = np.linspace(0,tmax,256) # Domaine des abscisses en s de 0 à tmax
y = A*np.cos((2*pi/T)*t)    # Domaine des ordonnées en m équation y=f(t)

plt.title('Signal sinusoïdal')  # Titre du graphe
plt.xlabel('$t$ (en s)')        # Label de l'axe des abscisses
plt.ylabel('$y$ (en m)')        # Label de l'axe des ordonnées
plt.xlim(0,tmax)                # Bornes de l'axe des abscisses
plt.ylim(-1.5*A,1.5*A)          # Bornes de l'axe des ordonnées
plt.grid()                      # Affiche une gille
plt.plot(t,y,'r')               # Trace la courbe y=f(t) en rouge
plt.show()                      # Affiche la figure
"""

# =============================================================================
#                                                           CORRECTION CONFIRME
# =============================================================================

def signal(A,T,tmax):
    """
    A = amplitude en m,
    T = période en s,
    tmax = durée de représentation en s
    """
    t = np.linspace(0,tmax,256)
    y = A*np.cos((2*pi/T)*t)
    plt.xlabel('$t$ (en s)')
    plt.ylabel('$y$ (en m)')
    plt.xlim(0,tmax)
    plt.ylim(-1.5*A,1.5*A)
    plt.grid()
    plt.plot(t,y)
    return plt.show()

# =============================================================================
# Pour que les courbes illustrant l'influence de l'amplitude et de la période
# s'affichent sur une fenêtre unique de visualisation, paramétrer le logiciel
# en mode automatique en entrant la commande magique  %matplotlib auto   dans
# la console avant d'exécuter le programme.
# =============================================================================
    
# Influence de l'amplitude
plt.subplot(2,1,1)
plt.title('Influence de l\'amplitude', loc = 'left')
for i in np.arange(1,11,2):
    signal(i,2.4,10)

# Influence de la période
plt.subplot(2,1,2)
plt.title('Influence de la période', loc = 'left')
for i in np.arange(1.5,2.6,0.5):
    signal(1.8,i,10)

