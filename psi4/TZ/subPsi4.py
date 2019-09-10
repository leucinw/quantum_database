#!/usr/bin/env python
import os,sys
import threading

def sub_sapt(psi4):
  fname = psi4.split(".psi4")[0]
  cmdstr = "psi4 -n 4 -i %s.psi4 -o %s.log "%(fname, fname)
  os.system(cmdstr)
  return True

nstart = int(sys.argv[1])
nend = int(sys.argv[2])

filelist = open("filelist.txt").readlines()[nstart:nend]
for i in filelist:
  i = i.split(".psi4")[0] + ".log"
  print(i,end=" ")
threadlist = []
for i in range(len(filelist)): 
  threadlist.append("t_%02d"%i)
for i in range(len(threadlist)):
  threadlist[i] = threading.Thread(target=sub_sapt,args=(filelist[i], ))
for i in range(len(threadlist)):
  threadlist[i].start() 
for i in range(len(threadlist)):
  threadlist[i].join()
