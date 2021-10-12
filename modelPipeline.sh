#!/bin/bash
#This will be the basis for the model pipeline script

#October 12,2021 This file will: Create four directories (including 3 subdirectories)



function onInstall(){
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
echo "Creating procced files folder"
mkdir -p "DTPipeline/processed"
else echo "'$DIR' already exists"
fi
}


onInstall
