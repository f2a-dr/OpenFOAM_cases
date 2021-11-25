#!/bin/bash

#---------Calcolo condizioni operative e campo di velocità---------
./inputCal.py
./fieldCalculator.py

#---------Inizializzazione campo di moto interno in file U---------
awk '//; /insert here/{while (getline line <"initU"){print line}}' ../0/U.templ > ../0/U
#cp customProperties ../constant/
