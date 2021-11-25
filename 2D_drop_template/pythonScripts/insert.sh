#!/bin/bash

#'pythonScripts/internal_field/internalField'

#awk '/insert here/ { print; print initU; next}1' 0/U.templ > 0/U

awk '//; /insert here/{while (getline line <"initU"){print line}}' 0/U.templ > 0/U


#awk  '/\/\/insert here/ { print }' 'pythonScripts/internal_field/internalField' > pprova

#sed  '/insert here/e cat hello' pprova > pprova #'pythonScripts/internal_field/internalField'' pprova
