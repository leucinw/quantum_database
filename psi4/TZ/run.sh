#!/bin/sh
#

begin=$(date +%s)
for i in {0..7..2}
do
	check_1=0
	file_list=`python subPsi4.py $i $[i+2]`
	while [[ $check_1 = 0 ]]
	do
		for element in $file_list
		do
			check_0=`tail -n 1 $element`
			result=$(echo $check_0 | grep "beer")
			echo $result
			if [[ "$result" != "" ]]
			then
				check_1=1
			else
				check_1=0
			fi
		done
		sleep 6s
		echo $check_1
	done
done
end=$(date +%s)
spend=$(expr $end - $begin)
echo $spend >> time_1.txt
