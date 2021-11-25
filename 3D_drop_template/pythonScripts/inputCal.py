#!/bin/python3.8

import setup as stp

gdot = (stp.Ca*stp.sigma)/(stp.mu_w*stp.a)
MI = (stp.beta+1)/2

Re = (stp.rho_w*gdot*stp.a*(2*stp.a))/(stp.mu_w)
We = (stp.rho_w*(gdot*stp.a)**2*2*stp.a)/(stp.sigma)

f=open("../input","w+")
f.write("/*-------------Calculation parameter-------------*/\n")
f.write("double beta="+str(stp.beta)+";\t // Parametro campo di moto legato a MI\n")
f.write("double gdot="+str(gdot)+";\t // shear rate\n")
f.write("\n")
f.write("/*-------------Information parameter-------------*/\n")
f.write("//double MI="+str(MI)+";\t // Mixing Index\n")
f.write("//double Ca="+str(stp.Ca)+";\t // capillary number\n")
f.write("//double We="+str(We)+";\t // Weber number\n")
f.write("//double Re="+str(Re)+";\t // Reynolds number\n")

f.close()

#g=open("customProperties", "w+")
#
#g.write("/*--------------------------------*- C++ -*----------------------------------*\ \n")
#g.write("| ==========                 |                                                 |\n")
#g.write("| \ \      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
#g.write("|  \ \    /   O peration     | Version:  8                                     |\n")
#g.write("|   \ \  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
#g.write("|    \ \/     M anipulation  |                                                 |\n")
#g.write("\*---------------------------------------------------------------------------*/\n")
#g.write("FoamFile\n")
#g.write("{\n")
#g.write("    version     2.0;\n")
#g.write("    format      ascii;\n")
#g.write("    class       dictionary;\n")
#g.write("""    location    "constant";\n""")
#g.write("    object      customProperties;\n")
#g.write("}\n")
#g.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
#
#g.write("gdot\t"+str(gdot)+"\n")
#g.write("stp.beta\t"+str(stp.beta)+"\n")
#
#g.write("// ************************************************************************* //\n")
#
#g.close()
