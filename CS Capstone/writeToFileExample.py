import os
import sys
import json
import subprocess

#dictionary for holding json file structure
data = {}
data['jobQueue'] = {}
#Number of batches will be equal to the number of unique settings files
numBatches = int(sys.argv[1]);
numJobs = int(sys.argv[2]);
numFiles = int(sys.argv[3]);

for order in range(2):
    #populate dictionaryfor batchID in data['jobQueue']:
    for batchID in range(numBatches):
        print("Batch ID: " +str(batchID))
        #Batch Identifier key for each batch
        data['jobQueue'][batchID] = {}
        for jobID in range(numJobs):
            print("Job ID: " +str(jobID))
            #Job Identifier key for each job within a batch
            data['jobQueue'][batchID][jobID] = {}
            for fileID in range(numFiles):
                print("File ID: " +str(fileID))
                data['jobQueue'][batchID][jobID][fileID] = {}
                if (order == 0):
                    print("Printing test files to Pre-processed directory.")
                    #Here we have to manually set the file priority, but this would be done by sorting
                    data['jobQueue'][batchID][jobID][fileID]['filePriority'] = fileID + 1
                    data['jobQueue'][batchID][jobID][fileID]['fileName'] = 'test' + str(fileID) +".txt"
                    data['jobQueue'][batchID][jobID][fileID]['filePathNP'] = 'DTPipeline/Processed'
                    data['jobQueue'][batchID][jobID][fileID]['filePathP'] = 'DTPipeline/Pre-processed'
                    data['jobQueue'][batchID][jobID][fileID]['filePathSettings'] = 'DTPipeline/Settings/Batch Settings/dummySettings.txt'
                else:
                    #Here we have to manually set the file priority, but this would be done by sorting
                    data['jobQueue'][batchID][jobID][fileID]['filePriority'] = fileID + 1
                    data['jobQueue'][batchID][jobID][fileID]['fileName'] = 'test' + str(fileID) +".txt"
                    data['jobQueue'][batchID][jobID][fileID]['filePathNP'] = 'DTPipeline/Pre-processed'
                    data['jobQueue'][batchID][jobID][fileID]['filePathP'] = 'DTPipeline/Processed'
                    data['jobQueue'][batchID][jobID][fileID]['filePathSettings'] = 'DTPipeline/Settings/Batch Settings/dummySettings.txt'
    try:
        #Write file to disk
        with open('jobQueue.json', 'w') as outfile:
            json.dump(data, outfile)
    except FileExistsError:
        print("File jobQueue.json already exists")
    if (order == 0):
        #Run Queueing Algorithm to write all files to reverse order.
        subprocess.run(["python3", "QueuingAlgorithm.py", "0"])
