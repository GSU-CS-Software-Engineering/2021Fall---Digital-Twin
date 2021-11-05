import os
import json
import sys

def getProcessState():
    #Read a json file
    with open("DTPipeline/Settings/Temp/ProcessingState.json") as json_file:
        data = json.load(json_file)

#A function for tracking what state the pipeline is currently in
def setProcessState(stateID):
    try:
        #Write file to disk
        file = "DTPipeline/Settings/Temp/ProcessingState.json"
        with open(file, 'w') as outfile:
            data['ProcessingState'] = stateID
            json.dump(data, outfile)
            print("File " +file +" created.")
    except FileExistsError:
        print("Error creating file: " +file)

#Pipeline Calling Stack
setProcessState(1) #Starting state

subprocess.run(["python3", "modelPipelineSetup.py")
#setProcessState(2) #modelPipelineSetup.py finished

subprocess.run(["python3", "CleanupAlgorithm.py")
setProcessState(3) #CleanupAlgorithm.py finished

while (getProcessState() == 0):
    subprocess.run(["python3", "FileIOCheckAlgorithm.py")
    setProcessState(4) #ModelPipelineSetup.py finished

    subprocess.run(["python3", "SortingAlgorithm.py")
    setProcessState(5) #SortingAlgorithm.py finished

    subprocess.run(["python3", "QueuingAlgorithm.py")
    setProcessState(6) #QueuingAlgorithm.py"finished

    subprocess.run(["python3", "CleanupAlgorithm.py")
    #setProcessState(7) #CleanupAlgorithm.py finished

print("Pipeline Exiting")
