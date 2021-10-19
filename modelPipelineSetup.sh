#!/bin/bash
#This will be the basis for the model pipeline script

#October 12,2021 This file will: Create four directories (including 3 subdirectories)



function onInstall(){

if [ ! -d "DTPipeline" ] || [ ! -d "DTPipeline/pre-processed/" ] || [ ! -d "DTPipeline/settings" ] || [ ! -d "DTPipeline/processed" ];
then 
	# Print statement requesting input (without going to a new line)
	echo -e "The required directories could not be found.\nPerform first time setup? (Y/N)"
	# Retrieve user input
	gateway=1
	while [[ $gateway = 1 ]]
	do
		
		read decision

		if [ $decision != "Y" ] && [ $decision != "y" ] && [ $decision != "N" ] && [ $decision != "n" ];
		then
			echo "Please enter a valid response: (Y/N)"
		else
			gateway=0
			break
		fi
	done

	if [[ $decision = "Y" ]] || [[ $decision = "y" ]];
	then
		echo "Creating required directories..."

		DIR="DTPipeline"

		if [ ! -d $DIR ]
		then
		echo "Creating official model pipeline directory"
		mkdir "DTPipeline"
		else
		echo "'$DIR' already exists"
		fi

		DIR="DTPipeline/pre-processed/"
		if [ ! -d $DIR ]
		then
		#an if statement to check if the directory already exists
		echo "Creating pre-processed folder"
		mkdir -p "DTPipeline/pre-processed/"

		else echo "'$DIR' already exists"
		fi

		DIR="DTPipeline/settings"

		if [ ! -d $DIR ]
		then
		mkdir -p "DTPipeline/settings"
		echo "Creating settings folder"
		else echo "'$DIR' already exists"
		fi
		DIR="DTPipeline/processed"
		if [ ! -d $DIR ]
		then
		echo "Creating processed files folder"
		mkdir -p "DTPipeline/processed"
		else echo "'$DIR' already exists"
		fi
	else
		echo -e "First time setup aborted.\nExiting."
	fi
else
	echo "All directories successfully validated."
fi
}


onInstall
