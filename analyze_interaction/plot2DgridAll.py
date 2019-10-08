#!/usr/bin/env python3

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys

def grid_2d(gridDim, inputNonZeroGrid, monoList1, monoList2):
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
      plt.text(-0.25+i-1,-1.0, monoList2[i-1], fontsize=5, rotation=90)
    for i in range(1,yDim+1,1):
      plt.text(-7.5, 0.3+i-1, monoList1[i-1], fontsize=5)
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

def nonZeroGrid(monolist1, monolist2, complist):
    monoList1 = open(monolist1).readlines()
    monoList2 = open(monolist2).readlines()
    for i in range(len(monoList1)):
        monoList1[i]=monoList1[i][:-1]
    for i in range(len(monoList2)):
        monoList2[i]=monoList2[i][:-1]
    nonZeroGrid = [] 
    lines = open(complist).readlines()
    for i in range(len(lines)):
        mono1 = lines[i].split("-")[0]
        mono2 = lines[i].split("-")[1][:-1]
        # each monomer in the monolist?
        if mono1 not in monoList1:
            print(mono1 + " is not in monoList1")
        if mono2 not in monoList2:
            print(mono2 + " is not in monoList2")

        idx1 = int(monoList1.index(mono1))    
        idx2 = int(monoList2.index(mono2))
        if (idx1<38 and idx2<38):
          if idx2 < idx1:
            tmp = idx1
            idx1 = idx2
            idx2 = tmp
        nonZeroGrid.append([idx1, idx2])
    return nonZeroGrid,monoList1,monoList2

#execute
grid = nonZeroGrid(sys.argv[1], sys.argv[2],sys.argv[3])
grid_2d([len(grid[1]),len(grid[2])], grid[0], grid[1], grid[2])
