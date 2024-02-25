#!/bin/bash
while true 
do 
echo "What do you want to do sir?"
echo "1: creat a bash file"
echo "2: creat a normal file"
echo "3: creat a new directorie"
echo "4: Exit"

read INPUT 

case $INPUT in 
	1) echo "How many files do you want?"
	read count 
	while [ "$count" -gt  0 ];
	do
		echo "please enter a new file name"
		read b
		touch $b
		chmod u+x $b
		echo "#!/bin/bash" > $b
		echo "File created ....Done!"
		count=$(($count -1)) 
	done 
		;;
 
	2)echo "How many file do you want"
	  read file
 		while [ "$file" -gt 0 ];
		do
			echo "name for the file please!!"
			read f
			touch $f
			echo "file created ..."
			file=$(($file -1))
	done 
		;;



	3)echo "How many directories you want make sir !"
	  read dk
		while [ "$dk"  -gt 0 ];
		 do 
			echo "Name of the new directorie please!!"		
			read mk	
			mkdir $mk
			echo "Directorie made ..Done!!"
			dk=$(($dk -1))


	done ;;


	4) echo "Exit...."
		exit 1 ;;
esac
done 
