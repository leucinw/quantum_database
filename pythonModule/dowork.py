#!/usr/bin/env python


import os,sys
sys.path.append('/home/xy3866/quantum_database/')
import numpy as np
from pythonModule.readChemFile import *
from pythonModule.readDataFile import *
from pythonModule.operation import *
from pythonModule.chemFileConvert import *

#XYZ2COM_BSSE("A_C_base.xyz", 13, "0,1 0,1 0,1") 
XYZ2COM_BSSE("AcOHMinus_benzene.xyz", 6, "-1,1 -1,1 0,1") 
XYZ2COM_BSSE("benzene_methylguanidine_v.xyz", 13, "1,1 1,1 0,1") 
#XYZ2COM_BSSE("U_U_base.xyz", 12, "0,1 0,1 0,1") 
#XYZ2COM_BSSE("formamide_formamide_dimer.xyz", 6, "0,1 0,1 0,1") 
#XYZ2COM_BSSE("formamide_formamide_dimer.xyz", 6, "0,1 0,1 0,1") 
#XYZ2COM_BSSE("A24-13-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-14-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-17-dimer.xyz", 8, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-18-dimer.xyz", 5, "0,1 0,1 0,1", optCartesian=True)  
#XYZ2COM_BSSE("A24-19-dimer.xyz", 5, "0,1 0,1 0,1", optCartesian=True)  
#XYZ2COM_BSSE("A24-23-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-5-dimer.xyz", 4, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-9-dimer.xyz", 4, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-10-dimer.xyz", 12, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-12-dimer.xyz", 10, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-14-dimer.xyz", 12, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-15-dimer.xyz", 15, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-18-dimer.xyz", 12, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-21-dimer.xyz", 12, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-22-dimer.xyz", 13, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-3-dimer.xyz", 5, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-4-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-6-dimer.xyz", 12, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-7-dimer.xyz", 15, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("S22-9-dimer.xyz", 6, "0,1 0,1 0,1") 
 
#LOG2COM_BSSE("A24-18-dimer.out") 
#LOG2COM_BSSE("A24-19-dimer.out") 
#LOG2COM_BSSE("S22-12-dimer.out") 
#LOG2COM_BSSE("S22-14-dimer.out") 
#LOG2COM_BSSE("S22-15-dimer.out") 
#LOG2COM_BSSE("S22-18-dimer.out") 
#LOG2COM_BSSE("S22-21-dimer.out") 
#LOG2COM_BSSE("S22-22-dimer.out") 
#LOG2COM_BSSE("S22-6-dimer.out") 
#LOG2COM_BSSE("S22-7-dimer.out") 

#for files in os.listdir("."):
#  if ".out" in files:
#    lines = readWholeFile(files)
#    if "Normal termination" in lines[-1]:
#      print files
#      os.system("mv %s ../Converged_Dimer"%files)

#for files in os.listdir("."):
#  if ".out" in files:
#    LOG2XYZ(files)

##XYZ2PSI4("A24-11-dimer.xyz", 6,  "0 1", "0 1", "TZ") 
##XYZ2PSI4("A24-13-dimer.xyz", 6,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-14-dimer.xyz", 6,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-17-dimer.xyz", 8,  "0 1", "0 1", "TZ")  
###XYZ2PSI4("A24-18-dimer.xyz", 5,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-19-dimer.xyz", 5,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-23-dimer.xyz", 6,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-5-dimer.xyz", 4,   "0 1", "0 1", "TZ")  
##XYZ2PSI4("A24-9-dimer.xyz", 4,   "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-10-dimer.xyz", 12, "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-12-dimer.xyz", 10, "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-14-dimer.xyz", 12, "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-15-dimer.xyz", 15, "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-18-dimer.xyz", 12, "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-21-dimer.xyz", 12, "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-22-dimer.xyz", 13, "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-3-dimer.xyz", 5,   "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-4-dimer.xyz", 6,   "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-6-dimer.xyz", 12,  "0 1", "0 1", "TZ")  
###XYZ2PSI4("S22-7-dimer.xyz", 15,  "0 1", "0 1", "TZ")  
##XYZ2PSI4("S22-9-dimer.xyz", 6,   "0 1", "0 1", "TZ") 

#for dist in [0.7, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1]:
#  XYZ2XYZ("A24-11-dimer.xyz", 6, [1], [10], dist)
#  XYZ2XYZ("A24-13-dimer.xyz", 6, [1], [9], dist)
#  XYZ2XYZ("A24-14-dimer.xyz", 6, [5,6], [8,9], dist)
#  XYZ2XYZ("A24-17-dimer.xyz", 5, [1], [6], dist)
#  XYZ2XYZ("A24-19-dimer.xyz", 5, [1], [6], dist)
#  XYZ2XYZ("A24-23-dimer.xyz", 6, [5, 6], [11, 12], dist)
#  XYZ2XYZ("A24-5-dimer.xyz", 4, [1,4], [5,7], dist)
#  XYZ2XYZ("A24-9-dimer.xyz", 4, [1,2], [6,8], dist)
#  XYZ2XYZ("S22-10-dimer.xyz", 12, [1,2,3,4,5,6], [16], dist)
#  XYZ2XYZ("S22-12-dimer.xyz", 10, [3,6], [12, 14], dist)
#  XYZ2XYZ("S22-18-dimer.xyz", 12, [1,2,3,4,5,6], [16], dist)
#  XYZ2XYZ("S22-3-dimer.xyz", 5, [1], [6], dist)
#  XYZ2XYZ("S22-4-dimer.xyz", 6, [1], [7], dist)
#  XYZ2XYZ("S22-9-dimer.xyz", 6, [1, 2], [7, 8], dist)

#for dist in [0.7, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1]:
#  XYZ2PSI4("A24-11-dimer_%s.xyz"%str("%.2f"%dist), 6,  "0 1", "0 1", "DZ") 
#  XYZ2PSI4("A24-13-dimer_%s.xyz"%str("%.2f"%dist), 6,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-14-dimer_%s.xyz"%str("%.2f"%dist), 6,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-17-dimer_%s.xyz"%str("%.2f"%dist), 8,  "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("A24-18-dimer_%s.xyz"%str("%.2f"%dist), 5,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-19-dimer_%s.xyz"%str("%.2f"%dist), 5,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-23-dimer_%s.xyz"%str("%.2f"%dist), 6,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-5-dimer_%s.xyz"%str("%.2f"%dist), 4,   "0 1", "0 1", "DZ")  
#  XYZ2PSI4("A24-9-dimer_%s.xyz"%str("%.2f"%dist), 4,   "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-10-dimer_%s.xyz"%str("%.2f"%dist), 12, "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-12-dimer_%s.xyz"%str("%.2f"%dist), 10, "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-14-dimer_%s.xyz"%str("%.2f"%dist), 12, "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-15-dimer_%s.xyz"%str("%.2f"%dist), 15, "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-18-dimer_%s.xyz"%str("%.2f"%dist), 12, "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-21-dimer_%s.xyz"%str("%.2f"%dist), 12, "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-22-dimer_%s.xyz"%str("%.2f"%dist), 13, "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-3-dimer_%s.xyz"%str("%.2f"%dist), 5,   "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-4-dimer_%s.xyz"%str("%.2f"%dist), 6,   "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-6-dimer_%s.xyz"%str("%.2f"%dist), 12,  "0 1", "0 1", "DZ")  
#  #XYZ2PSI4("S22-7-dimer_%s.xyz"%str("%.2f"%dist), 15,  "0 1", "0 1", "DZ")  
#  XYZ2PSI4("S22-9-dimer_%s.xyz"%str("%.2f"%dist), 6,   "0 1", "0 1", "DZ") 
