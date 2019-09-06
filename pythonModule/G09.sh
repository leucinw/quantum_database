#!/bin/csh
#
#

#Run this script to generate TINKER readable ISA multipole
source /opt/intel/cce/10.1.011/bin/iccvars.csh
source /opt/intel/fce/10.1.011/bin/ifortvars.csh
setenv g09root /opt/g09gh/gaussian
source $g09root/g09/bsd/g09.login
setenv GAUSS_SCRDIR /scratch/xy3866

if ( ! -d "$GAUSS_SCRDIR" ) then
   if ( ! { mkdir $GAUSS_SCRDIR } ) then
      echo "Could not make dir $GAUSS_SCRDIR ! Exit!"
      exit 1
   endif
endif

set s1=`hostname`
set s2=`pwd`
echo "#Job in" $s2 is running on $s1  > job_node.$s1
cat job_node.$s1

g09 HBC1-FaNNFaNN-3.4-dimer.com HBC1-FaNNFaNN-3.4-dimer.out &
#g09 S22-14-dimer.com S22-14-dimer.out &
#g09 S22-15-dimer.com S22-15-dimer.out &
#g09 S22-18-dimer.com S22-18-dimer.out &
#g09 S22-21-dimer.com S22-21-dimer.out &

#g09 S22-22-dimer.com S22-22-dimer.out &
#g09 S22-6-dimer.com S22-6-dimer.out &
#g09 S22-7-dimer.com S22-7-dimer.out &
