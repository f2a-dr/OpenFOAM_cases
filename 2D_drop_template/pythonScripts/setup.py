#!/bin/python3.8

import string
import os

splitName = os.path.split(os.path.realpath(os.path.join(os.getcwd(), os.pardir))) # crea un tuple con il path della cartella del caso
name = str(splitName[1]) # il secondo elemento (posizione 1) è il nome della cartella con il caso

# il nome della cartella viene processato per estrarre il valore di mixing index e del numero di capillarità
elements = name.split("_")
elements[1] = elements[1][:1]+"."+elements[1][1:]
elements[2] = elements[2][:1]+"."+elements[2][1:]

# vengono calcolate le variabili che saranno utilizzate per settare il caso
mixingIndex = float(elements[1])
beta = 2*mixingIndex - 1
Ca = float(elements[2])

#----------Costanti necessarie al calcolo dei numeri adimensionali-----------
mu_w = 1e-1     # viscosità acqua
rho_w = 1000    # densità acqua
sigma = 2.1e-5  # tensione interfacciale
a = 2e-3        # raggio della goccia
