import os
import sys
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
                    if (sys.argv[1] == "1"):
                        from shutil import copyfile
                        try:
                            #Copy file to disk
                            from shutil import copy
                            #Check if the file exists before copying
                            #If it exists, loop (#) until filename(#) does not already exist
                            fileExists = os.path.exists("DTPipeline/BackupCopies/"+str(data['jobQueue'][batchID][jobID][fileID]['fileName']))
                            if (fileExists):
                                i = 0
                                #Split filepath/filename and extension
                                temp = str(data['jobQueue'][batchID][jobID][fileID]['fileName']).split('.')
                                while (fileExists):
                                    fileExists = os.path.exists("DTPipeline/BackupCopies/"+temp[0]+"("+str(i)+")."+temp[1])
                                    if (fileExists != True):
                                        file = open("DTPipeline/BackupCopies/"+temp[0]+"("+str(i)+")."+temp[1], 'x')
                                        file.close()
                                        copy(str(str(data['jobQueue'][batchID][jobID][fileID]['filePathNP'])+'/'+str(data['jobQueue'][batchID][jobID][fileID]['fileName'])), str("DTPipeline/BackupCopies/"+temp[0]+"("+str(i)+")."+temp[1]))
                                        print("Copying File: "+temp[0]+"("+str(i)+")."+temp[1])
                                    i += 1
                            else:
                                file = open("DTPipeline/BackupCopies/"+str(data['jobQueue'][batchID][jobID][fileID]['fileName']), 'x')
                                file.close()
                                copy(str(str(data['jobQueue'][batchID][jobID][fileID]['filePathNP'])+'/'+str(data['jobQueue'][batchID][jobID][fileID]['fileName'])),str("DTPipeline/BackupCopies/"+str(data['jobQueue'][batchID][jobID][fileID]['fileName'])))
                                print("Copying File: ",str(data['jobQueue'][batchID][jobID][fileID]['fileName']))
                        except FileExistsError:
                            print("Directory "+str(data['jobQueue'][batchID][jobID][fileID]['fileName'])+" already exists and could not be overwritten.")
                    #Initialize command
                    subprocess.run(["python3", "DummyDeltaGen.py",
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
                    try:
                        #Write file to disk
                        with open('jobQueue.json', 'w') as outfile:
                            json.dump(data, outfile)
                    except FileExistsError:
                        print("Directory jobQueue.json already exists and could not be overwritten.")
                elif (data['jobQueue'][batchID][jobID][fileID]['filePriority'] == 0):
                    print("File already processed in queue, skipping...")
                else:
                    print("File priority mismatch.")
#Set the process state to 5
from ProcessState import setProcessState
setProcessState(5)
