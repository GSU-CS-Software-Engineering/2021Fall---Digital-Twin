import os
import json
import subprocess

#Read a json file
with open('jobQueue.json') as json_file:
    data = json.load(json_file)
    for batchID in data['jobQueue']:
        print("Batch ID: " +str(batchID))
        for jobID in data['jobQueue'][batchID]:
            print("Job ID: " +str(jobID))
            filePriority = 1
            for fileID in data['jobQueue'][batchID][jobID]:
                print("File ID: " +str(fileID))
                if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] == filePriority):
                    #Initialize command
                    subprocess.run(["python3", "dummyDeltaGen.py",
                    str(data['jobQueue'][batchID][jobID][fileID]['fileName']),
                    str(data['jobQueue'][batchID][jobID][fileID]['filePathNP']),
                    str(data['jobQueue'][batchID][jobID][fileID]['filePathP']),
                    str(data['jobQueue'][batchID][jobID][fileID]['filePathSettings']),
                    str(data['jobQueue'][batchID][jobID][fileID]['filePriority'])
                    ])

                    #Confirm data that should be processed by DeltaGen
                    print('Priority: ' +str(data['jobQueue'][batchID][jobID][fileID]['filePriority']))
                    print('Name: ' +str(data['jobQueue'][batchID][jobID][fileID]['fileName']))
                    print('File path non-processed: ' +str(data['jobQueue'][batchID][jobID][fileID]['filePathNP']))
                    print('File path processed: ' +str(data['jobQueue'][batchID][jobID][fileID]['filePathP']))
                    print('File path settings: ' +str(data['jobQueue'][batchID][jobID][fileID]['filePathSettings']))
                    print('')
                    #Set the priority to 0 when file has been processed
                    data['jobQueue'][batchID][jobID][fileID]['filePriority'] = 0
                    filePriority += 1
                else:
                    print("File priority mismatch.")
