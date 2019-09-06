# quantum_database

## Compare dimers in (S108 database + dimer_added) and BioFragmentDatabase
  - A24 & S22 has been checked 
  - 
  - 
  - 
  - 

## Compare molecules in S108 database and those of biomolecular fragments, including
  - 20 natural amino acids
  - unnatural amino acids
  - nucleic acids
  - sugar
  - lipid (header, tail)

## Optimize the newly added monomers to their local minima
  - MP2/6-311G(d,p) 

## Generate dimers with different interactions
  - consider different conformations for each dimer
  - optimize the dimer at MP2/cc-pvtz level

## Energy decomposition using SAPT2+ at 7 distances
  - use the above optimized geometry
  - SAPT2+/aug-cc-pvtz

## Derive the AMOEBA+ initial parameters using poltype
  - bonded parameters
  - vdw, CT, CP, polarization with new atom classes? 
