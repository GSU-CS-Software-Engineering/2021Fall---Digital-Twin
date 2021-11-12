import os
import sys
import json
import glob

#initialize variables
#Read a json file
with open("DTPipeline/Settings/Temp/fileExtensions.json") as json_file:
    data = json.load(json_file)
fileExtensions = [] #list of known extensions
for item in data['knownFileExtensions']:
    fileExtensions.append(data['knownFileExtensions'][item])

ignoredExtensions = [] #list for ignored file extensions
for item in data['ignoredFileExtensions']:
    fileExtensions.append(data['ignoredFileExtensions'][item])

recipeExtensions = [] #list of known recipe extensions
for item in data['knownRecipeExtensions']:
    fileExtensions.append(data['knownRecipeExtensions'][item])

ignoredRecipeExtensions = [] #list for ignored recipe extensions
for item in data['ignoredRecipeExtensions']:
    fileExtensions.append(data['ignoredRecipeExtensions'][item])

recipeList = []
preProcessedFiles = {} #json dictionary
preProcessedFiles['settingsFile'] = 'default'
preProcessedFiles['conversionFileList'] = {}
fileCount = 0 #global file count for each list

for root, dirs, files in os.walk('DTPipeline/Recipes'):
    for file in files:
        ignoreExt = False
        for iExt in ignoredRecipeExtensions:
            if (file.endsWith(iExt)):
                ignoreExt = True
        if (ignoreExt == False):
            knownExt = False
            for ext in recipeExtensions:
                if (file.endswith(ext)):
                    knownExt = True
                    if (knownExt == True):
                        recipeList.append(os.path.join(root, file))
            if (knownExt == False):
                print("Warning, the extension for the file: "+file+" was not an expected extension.")
                print("To add the extension to the list of expected file extensions, enter the word: add")
                print("To add the extension to the list of ignored file extensions, enter the word: ignore")
                print("To remove "+file+" from the Pre-processed directory, enter the word: remove")
                decision = input("To ignore this file during this run, enter the word: unlist\n")
                validInput = False
                while (validInput == False):
                    if (decision == "add" or decision == "ignore" or decision == "remove" or deicision == "unlist"):
                        validInput = True
                        if (decision == "add"):
                            fileWithExtension = os.path.splitext(file_name)
                            recipeExtensions.append(fileWithExtension[1])
                        elif (decision == "ignore"):
                            fileWithExtension = os.path.splitext(file_name)
                            ignoredRecipeExtensions.append(fileWithExtension[1])
                        elif (decision == "remove"):
                            os.remove(os.path.join(root, file))
                        else:
                            print("Ignoring file: "+file)
                    else:
                        validInput = False
                    if (validInput == False):
                        print("The previous entry: "+decision +" could not be processed.")
                        decision = input("Please enter one of the following keywords: \nadd \nignore \nremove \nunlist \n")


if (len(recipeList) > 1):
    iteration = 0
    validInput = False
    while (validInput == False):
        recipe = input("Warning, multiple recipe files were discovered. \nPlease enter the file name and extension of the recipe for this batch: \n")
        for file in recipeList:
            if ("DTPipeline/Recipes/"+recipe == file):
                validInput = True
                preProcessedFiles['settingsFile'] = file
        if (validInput == False and iteration > 0):
            print("The selected file "+recipe+" was not found, please enter a valid filename from the following: ")
            print(recipeList)

for root, dirs, files in os.walk('DTPipeline/Pre-processed'):
    for file in files:
        if (os.path.exists('jobQueue.json')):
            #Read a json file
            with open('jobQueue.json') as json_file:
                data = json.load(json_file)
                for batchID in data['jobQueue']:
                    for jobID in data['jobQueue'][batchID]:
                        for fileID in data['jobQueue'][batchID][jobID]:
                            if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] != 0 and file != data['jobQueue'][batchID][jobID][fileID]['fileName']):
                                ignoreExt = False
                                for iExt in ignoredExtensions:
                                    if (file.endsWith(iExt)):
                                        ignoreExt = True
                                if (ignoreExt == False):
                                    knownExt = False
                                    for ext in fileExtensions:
                                        if (file.endswith(ext)):
                                            knownExt = True
                                            if (knownExt == True):
                                                #If file extension is known, add it to the proper location in the json object
                                                preProcessedFiles[listCount]['conversionFileList'][fileCount]['filePath'] = path
                                                preProcessedFiles[listCount]['conversionFileList'][fileCount]['fileName'] = file
                                                fileCount += 1
                            else:
                                print("File: "+file+" has already been added to the queue, skipping.")
        else:
            ignoreExt = False
            for iExt in ignoredExtensions:
                if (file.endsWith(knownExt)):
                    ignoreExt = True
            if (ignoreExt == False):
                knownExt = False
                for ext in fileExtensions:
                    if (file.endswith(ext)):
                        knownExt = True
                        if (knownExt == True):
                            #If file extension is known, add it to the proper location in the json object
                            preProcessedFiles[listCount]['conversionFileList'][fileCount]['filePath'] = path
                            preProcessedFiles[listCount]['conversionFileList'][fileCount]['fileName'] = file
                            fileCount += 1
                if (knownExt == False):
                    print("Warning, the extension for the file: "+file+" was not an expected extension.")
                    print("To add the extension to the list of expected file extensions, enter the word: add")
                    print("To add the extension to the list of ignored file extensions, enter the word: ignore")
                    print("To remove "+file+" from the Pre-processed directory, enter the word: remove")
                    decision = input("To ignore this file during this run, enter the word: unlist\n")
                    validInput = False
                    while (validInput == False):
                        if (decision == "add" or decision == "ignore" or decision == "remove" or deicision == "unlist"):
                            validInput = True
                            if (decision == "add"):
                                fileWithExtension = os.path.splitext(file_name)
                                fileExtensions.append(fileWithExtension[1])
                            elif (decision == "ignore"):
                                fileWithExtension = os.path.splitext(file_name)
                                ignoredExtensions.append(fileWithExtension[1])
                            elif (decision == "remove"):
                                os.remove(os.path.join(root, file))
                            else:
                                print("Ignoring file: "+file)
                        else:
                            validInput = False
                        if (validInput == False):
                            print("The previous entry: "+decision +" could not be processed.")
                            decision = input("Please enter one of the following keywords: \nadd \nignore \nremove \nunlist \n")
try:
    #Write file to disk
    with open('fileListUnsorted.json', 'w') as outfile:
        json.dump(preProcessedFiles, outfile)
except FileExistsError:
    print("File already exists")

try:
    data['knownFileExtensions'] = fileExtensions #list of known extensions
    data['ignoredFileExtensions'] = ignoredExtensions #list for ignored extensions
    data['knownRecipeExtensions'] = recipeExtensions #list of known recipe extensions
    data['ignoredRecipeExtensions'] = ignoredRecipeExtensions #list for ignored recipe extensions
    #Write file to disk
    with open('DTPipeline/Settings/Temp/ProcessingState.json', 'w') as outfile:
        json.dump(data, outfile)
except FileExistsError:
    print("File already exists")

#Set the process state to 3
from ProcessState import setProcessState
setProcessState(3)
