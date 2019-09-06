#!/usr/bin/env python


import os,sys
import numpy as np
from readChemFile import *
from readDataFile import *
from operation import *
from chemFileConvert import *

#XYZ2COM_BSSE("A24-11-dimer.xyz", 6, "0,1 0,1 0,1") 
#XYZ2COM_BSSE("A24-13-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-14-dimer.xyz", 6, "0,1 0,1 0,1")  
#XYZ2COM_BSSE("A24-17-dimer.xyz", 8, "0,1 0,1 0,1")  
XYZ2COM_BSSE("HBC1-FaNNFaNN-3.4-dimer.xyz", 7, "0,1 0,1 0,1", optCartesian=False)  
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
 
#LOG2COM_BSSE("S22-12-dimer.out") 
#LOG2COM_BSSE("S22-14-dimer.out") 
#LOG2COM_BSSE("S22-15-dimer.out") 
#LOG2COM_BSSE("S22-18-dimer.out") 
#LOG2COM_BSSE("S22-21-dimer.out") 
#LOG2COM_BSSE("S22-22-dimer.out") 
#LOG2COM_BSSE("S22-6-dimer.out") 
#LOG2COM_BSSE("S22-7-dimer.out") 
