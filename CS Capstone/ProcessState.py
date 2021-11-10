import os
import json
import sys

def getProcessState():
    #Read a json file
    with open("DTPipeline/Settings/Temp/ProcessingState.json") as json_file:
        data = json.load(json_file)
    return data

#A function for tracking what state the pipeline is currently in
def setProcessState(stateID):
    try:
        data = getProcessState()
        #Write file to disk
        file = "DTPipeline/Settings/Temp/ProcessingState.json"
        with open(file, 'w') as outfile:
            data['ProcessingState'] = stateID
            json.dump(data, outfile)
            print("Processing State Updated: " +str(stateID))
    except FileExistsError:
        print("Error overwriting file: " +file)
