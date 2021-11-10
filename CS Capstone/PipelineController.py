import os
import json
import sys
import subprocess

from ProcessState import setProcessState
from ProcessState import getProcessState

defaultArgs = ["0"]

subprocess.run(["python3", "ModelPipelineSetup.py"])
#setProcessState(1) #modelPipelineSetup.py finished
if (os.path.exists("DTPipeline/Settings/Temp/ProcessingState.json")):
    subprocess.run(["python3", "CleanupAlgorithm.py"])
    #If ProcessingState.json exists, but setup was aborted, exit
    if (getProcessState() == -1):
        sys.exit()

    i = 0
    from ProcessState import getProcessState
    while (getProcessState() == 0 or i == 0):
        #subprocess.run(["python3", "FileIOCheckAlgorithm.py", sys.argv[1]])
        setProcessState(3) #ModelPipelineSetup.py finished
        if (i == 0):
            subprocess.run(["python3", "WriteToFileExample.py", "2", "5", "20"])
        #subprocess.run(["python3", "SortingAlgorithm.py"])
        setProcessState(4) #SortingAlgorithm.py finished

        if (len(sys.argv) < 2):
            subprocess.run(["python3", "QueuingAlgorithm.py", str(1)])
            #setProcessState(5) #QueuingAlgorithm.py"finished
        else:
            subprocess.run(["python3", "QueuingAlgorithm.py", str(sys.argv[1])])
            #setProcessState(5) #QueuingAlgorithm.py"finished

        subprocess.run(["python3", "CleanupAlgorithm.py", "10000"])
        #setProcessState(7) #CleanupAlgorithm.py finished
        i += 1

print("Pipeline Exiting")
