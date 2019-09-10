#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys

def grid_2d_org(gridDim, inputNonZeroGrid, monoListName):
    xDim = int(gridDim[0]) #no. of column
    yDim = int(gridDim[1]) #no. of row
    initList = [[0]*xDim]*yDim
    data = np.array(initList)
    # read in the non-zero values
    for i in range(len(inputNonZeroGrid)):
      xIdx = int(inputNonZeroGrid[i][0])  
      yIdx = int(inputNonZeroGrid[i][1])  
      data[xIdx][yIdx] += 1

    # create discrete colormap
    cmap = colors.ListedColormap(['white', 'blue', 'yellow', 'green'])
    bounds = [0,1,2,3,4]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)
    
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
    ax.set_xticks(np.arange(-0.5, 46.5, 1))
    ax.set_yticks(np.arange(-0.5, 46.5, 1))
    for i in range(1,46+1,1):
      plt.text(-0.25+i-1,-1.0, str(i), fontsize=5, rotation='vertical')
      plt.text(-1.75, 0.25+i-1, str(i), fontsize=5)
      plt.text(46.75, 0.25+i-1, (str(i)+' '+ monoListName[i-1]), fontsize=5)
    plt.tick_params(
    axis= 'both',      # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,        # ticks along the bottom edge are off
    labelleft=False,        # ticks along the bottom edge are off
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
    plt.savefig("test.png", dpi=300)
    plt.show()
    return

def nonZeroGridOrg(monolist, complist):
    monoList = open(monolist).readlines()
    for i in range(len(monoList)):
        monoList[i]=monoList[i][:-1]
    nonZeroGrid = [] 
    lines = open(complist).readlines()
    for i in range(len(lines)):
        mono1 = lines[i].split("-")[0]
        mono2 = lines[i].split("-")[1][:-1]
        # each monomer in the monolist?
        if mono1 not in monoList:
            print(mono1 + " is not in monomer list")
        if mono2 not in monoList:
            print(mono2 + " is not in monomer list")

        idx1 = int(monoList.index(mono1))    
        idx2 = int(monoList.index(mono2))
        if idx2 < idx1:
            tmp = idx1
            idx1 = idx2
            idx2 = tmp
        nonZeroGrid.append([idx1, idx2])
    return nonZeroGrid,monoList

def grid_2d_ion(gridDim, inputNonZeroGrid, ionListName, orgListName):
    yDim = int(gridDim[0]) #no. of column
    xDim = int(gridDim[1]) #no. of row
    initList = [[0]*xDim]*yDim
    data = np.array(initList)
    # read in the non-zero values
    for i in range(len(inputNonZeroGrid)):
      xIdx = int(inputNonZeroGrid[i][0])  
      yIdx = int(inputNonZeroGrid[i][1])  
      data[xIdx][yIdx] += 1

    # create discrete colormap
    cmap = colors.ListedColormap(['white', 'blue', 'yellow', 'green'])
    bounds = [0,1,2,3,4]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    fig, ax = plt.subplots()
    ax.imshow(data, cmap=cmap, norm=norm)
    
    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
    ax.set_xticks(np.arange(-0.5, xDim+0.5, 1))
    ax.set_yticks(np.arange(-0.5, yDim+0.5, 1))
    for i in range(1,xDim+1,1):
      plt.text(-0.25+i-1,-0.75, orgListName[i-1], fontsize=8, rotation=46)
    for i in range(1,yDim+1,1):
      plt.text(-1.0, 0.1+i-1, ionListName[i-1], fontsize=8)
      #plt.text(yDim+0.75, 0.25+i-1, (str(i)+' '+ monoListName[i-1]), fontsize=5)
    plt.tick_params(
    axis= 'both',      # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,        # ticks along the bottom edge are off
    labelleft=False,        # ticks along the bottom edge are off
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
    plt.savefig("test.png", dpi=300)
    plt.show()
    return

def nonZeroGridIon(ionlist, orglist, complist):
    ionList = open(ionlist).readlines()
    orgList = open(orglist).readlines()
    for i in range(len(ionList)):
        ionList[i]=ionList[i][:-1]
    for i in range(len(orgList)):
        orgList[i]=orgList[i][:-1]
    nonZeroGrid = [] 
    lines = open(complist).readlines()
    for i in range(len(lines)):
        mono1 = lines[i].split("-")[0]
        mono2 = lines[i].split("-")[1][:-1]
        # each monomer in the monolist?
        if mono1 not in ionList:
            print(mono1 + " is not in ion list")
        if mono2 not in orgList:
            print(mono2 + " is not in organic list")

        idx1 = int(ionList.index(mono1))    
        idx2 = int(orgList.index(mono2))
        nonZeroGrid.append([idx1, idx2])
    return nonZeroGrid,ionList,orgList

#execute
grid = nonZeroGridOrg(sys.argv[1], sys.argv[2])
grid_2d_org([len(grid[1]),len(grid[1])],grid[0], grid[1])

#grid = nonZeroGridIon(sys.argv[1], sys.argv[2],sys.argv[3])
#grid_2d_ion([len(grid[1]),len(grid[2])], grid[0], grid[1], grid[2])
