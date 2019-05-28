#!/bin/bash

# File that builds EPICS base and synApps from scratch with one call

# First we clone all of the modules
echo "Cloning and checking out all repos"
python3 clone_and_checkout.py
echo "Press enter to continue"
read continue1

# first build the dependencies
echo "Install the dependencies"
./dependencyInstall.sh
echo "Press enter to continue"
read continue2

# Python script for compiling EPICS and SynApps
echo "Starting compilation"
python3 buildEPICS.py
echo "Press enter to continue"
read continue3

# Python script that autogenerates install and uninstall scripts for all selected packages
echo "Creating install.sh and uninstall.sh in directory autogenerated/"
python3 script_generator.py
