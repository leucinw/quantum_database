%NoSave
%chk=HBC1-FaNNFaNN-3.4-dimer.chk
%nproc=8
%Mem=32GB
#p MP2/cc-pvtz  counterpoise=2 IOP(5/13=1) scf=tight Symmetry=None MaxDisk=100GB Opt=tight 

Opt=tight  

0,1 0,1 0,1
  C(Fragment=1)                  1.6949825    -0.1305189     0.0000000
  H(Fragment=1)                  2.8063360    -0.2160965     0.0000000
  N(Fragment=1)                  1.0990588    -1.2949125     0.0000000
  H(Fragment=1)                  1.8208947    -2.0147842     0.0000000
  N(Fragment=1)                  1.3728632     1.1680083     0.0000000
  H(Fragment=1)                  0.3521260     1.4653299     0.0000000
  H(Fragment=1)                  2.1658159     1.7950313     0.0000000
  C(Fragment=2)                 -1.6949825     0.1305189     0.0000000
  H(Fragment=2)                 -2.8063360     0.2160965     0.0000000
  N(Fragment=2)                 -1.0990588     1.2949125     0.0000000
  H(Fragment=2)                 -1.8208947     2.0147842     0.0000000
  N(Fragment=2)                 -1.3728632    -1.1680083     0.0000000
  H(Fragment=2)                 -0.3521260    -1.4653299     0.0000000
  H(Fragment=2)                 -2.1658159    -1.7950313     0.0000000

