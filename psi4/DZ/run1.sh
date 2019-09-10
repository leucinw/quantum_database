#!/bin/sh
#

begin=$(date +%s)
source /opt/intel/compilerpro-12.0.0.084/bin/compilervars.sh intel64

my_psi4=/home/xzhu216/psi4/psi4-install

export PSI_SCRATCH=/scratch/xy3866

if [ ! -d "$PSI_SCRATCH" ]
then
   mkdir $PSI_SCRATCH
fi

for dist in  "0.95"
do
	psi4 -n 4 -i formicacid_formamide_dimer_${dist}.psi4 -o formicacid_formamide_dimer_${dist}.log & 
done

end=$(date +%s)
spend=$(expr $end - $begin)
echo $spend >> time.txt
