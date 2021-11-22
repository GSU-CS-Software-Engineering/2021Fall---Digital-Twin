import os
import json
import sys

def getProcessState():
    #Read a json file
    processingState = open("DTPipeline/Settings/Temp/ProcessingState.json", 'r')
    with processingState as processingStateInFile:
        data = json.load(processingStateInFile)
        print("Retrieved process state: "+str(data['ProcessingState']))
        processingState.close()
    return int(data)

#A function for tracking what state the pipeline is currently in
def setProcessState(stateID):
    try:
        data = getProcessState()
        #Write file to disk
        processingState = open("DTPipeline/Settings/Temp/ProcessingState.json", 'w')
        with processingState as processingStateOutFile:
            data['ProcessingState'] = stateID
            json.dump(data, processingStateOutFile)
            processingState.close()
            print("Processing State Updated: " +str(stateID))
    except FileExistsError:
        print("Error overwriting file: " +file)
