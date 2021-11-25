# Tridimensional drop simulation

## Description
This folder constitutes a template for setting up a tridimensional OpenFOAM simulation to evaluate the breakup of a suspended drop under the influence of ax external imposed flow field.
The simulation uses the Volume Of Fluid (VOF) technique, implemented through the solver `interFoam`, shipped with OpenFOAM.

## Case creation
To set up the a new case the folder must be copied with and named according to the following syntax:

`MI_XY_ZW`

Where `XY` is the value of the Mixing Index that will be imposed to the external field, that will be interpreted in the following way:

`XY` means Mixing Index = `X.Y`

Where `X` is a single digit, while `Y` can contain any numer of digits.
So for imposing a mixing index of 0.6 the name will contain `XY` = 06, for imposing a mixing index equal to 0.589 the name will contain `XY` = 0589, and for imposing a mixing index equal to 1 the name will contain `XY` = 1 (or `XY`=10).

The value of `ZW` represent the Capillary Number, from which the velocity of the external flow field to impose is calculated. The value in the folder name will be interpreted as follows:

`ZW` means Ca = `Z.W`

Also in this case `Z` is a single digit, while `W` can contain any number of digits.
So for imposing a capillary number equal to 0.189 the name will contain `ZW` = 0189, and for a capillary number of 2.58 the name will contain `ZW` = 258.

### Limitations
With the name parsing implemented in the code is not possble to simulate Capillary numbers equal or greater than 10. To do this the file `pythonScripts/setup.py` must be modified.

## Usage
The basic usage consist in setting up the viscosity of the two phases in `constant/transportProperties`, impose some of the simulation properties (start and end time, time step, ...) in `system/controlDict` and running the various step of the simulation through the executable file with the command `./Allrun`.
This last command recall the various phases of the simulation; those can be also run separately with the command `./preprocessing`, `./processing`, `./postprocessing`.

### Brief folder explanation
In order to achieve a minimum understanding, the role of the folders not usually present in a standard OpenFOAM case is described shortly:

* `pythonScript`: contains most of the shell and python script used to automate the setup of the case, from the folder name parsing to the calculation of the velocity field;
* `logs`: contains logfiles generated directly by OpenFOAM used to check residuals during the simulation;
* `sim_logs`: contains the log of every command used during the simulation, in order to allow debug and identify the cause of unexpected failure of the simulation;
* `postProcessing`: contains the results relative to the tracking of the center of mass of the drop, to use it the CoM function object must be present in the OpenFOAM `src` directory. To avoid its usage it's necessary to disable the calculation in `system/controlDict`.

### Files explanation
Some files present in the main directory can be confusing, here there is a very brief description. Reading the code present the subdirectory in `pythonScripts` can help understand how those are used throughout the simulation.

* `input`: file written by a python script, gives information on adimensional numbers useful in the study and allows to check that the parsing of the directory name was done correctly;
* `U.templ`: dummy file used to initialise the flow field at the initial time step, used and regenerated at every run, DELETING IT WILL BREAK THE SIMULATION;
* `post.py`: used to load some default in Paraview for visualization, to be used it must be modified according to the absolute path of the simulation.

## More information and references
More detailed explanation on the simulations, the results and the thoretical approach can in be found in [Francesco De Roma's Master thesis](https://webthesis.biblio.polito.it/19884/)
