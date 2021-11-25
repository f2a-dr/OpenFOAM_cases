#!/bin/python3.8

from .. import setup

#gamma = 0.105   # shear rate
#alpha = 0          # mixing index

# leggo i centri delle celle e li salvo in x e y 
x = []
y = []

f = open("Cx","r")

for line in f:
    value = line[:-1]
    x.append(float(value))
    
f.close()

f = open("Cy","r")

for line in f:
    value = line[:-1]
    y.append(float(value))

f.close()

# calcolo per FIELD
Ux = []
Uy = []
for i in range(0,len(x)):
    Uy.append(x[i]*stp.gdot)
    Ux.append(y[i]*stp.gdot*stp.beta)

# apro e scrivo il file FIELD
f = open("internalField", "w+")

#f.write("\n")
#f.write("""/*--------------------------------*- C++ -*----------------------------------*\ \n""")
#f.write("| ==========                 |                                                 |\n")
#f.write("| \ \      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
#f.write("|  \ \    /   O peration     | Version:  3.0.1                                 |\n")
#f.write("|   \ \  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
#f.write("|    \ \/     M anipulation  |                                                 |\n")
#f.write("\*---------------------------------------------------------------------------*/\n")
#f.write("FoamFile\n")
#f.write("{\n")
#f.write("    version     8;\n")
#f.write("    format      ascii;\n")
#f.write("    class       dictionary;\n")
#f.write("""    location    "$FOAM_CASE/pythonScripts/internal_field";\n""")
#f.write("    object      internalField;\n")
#f.write("}\n")
#f.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //")
#f.write("\n")
#f.write("vett\n")
#f.write("(\n")

for i in range(0,len(x)):
    f.write("( %.8f %.8f 0 )\n" % (Ux[i],Uy[i]))

##f.write(");\n")
##f.write("\n")
##f.write("// ************************************************************************* //")

f.close()
