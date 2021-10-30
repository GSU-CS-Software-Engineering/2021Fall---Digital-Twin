import json

#dictionary for holding json file structure
data = {}
data['jobQueue'] = {}
#Number of batches will be equal to the number of unique settings files
numBatches = 2;
numJobs = 5;
numFiles = 20;
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
            #Here we have to manually set the file priority, but this would be done by sorting
            data['jobQueue'][batchID][jobID][fileID]['filePriority'] = fileID + 1
            data['jobQueue'][batchID][jobID][fileID]['fileName'] = 'test' + str(fileID) +".txt"
            data['jobQueue'][batchID][jobID][fileID]['filePathNP'] = 'DTPipeline/pre-processed'
            data['jobQueue'][batchID][jobID][fileID]['filePathP'] = 'DTPipeline/processed'
            data['jobQueue'][batchID][jobID][fileID]['filePathSettings'] = 'DTPipeline/Settings/Batch Settings/dummySettings.txt'
try:
    #Write file to disk
    with open('jobQueue.json', 'w') as outfile:
        json.dump(data, outfile)
except FileExistsError:
    print("Directory jobQueue.json already exists")
