import os
import sys
import json
import subprocess

if (os.path.exists('jobQueue.json')):
    dataNew = {}
    dataNew['jobQueue'] = {}
    remainingFiles = 0
    #Read a json file
    with open('jobQueue.json') as json_file:
        data = json.load(json_file)
        newBatchID = 0
        prevBatchID = 0
        for batchID in data['jobQueue']:
            newJobID = 0
            prevJobID = 0
            print("Batch ID: " +str(batchID))
            for jobID in data['jobQueue'][batchID]:
                print("Job ID: " +str(jobID))
                filePriority = 1
                newFileID = 0
                prevFileID = 0
                for fileID in data['jobQueue'][batchID][jobID]:
                    print("File ID: " +str(fileID))
                    if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] == 0):
                        fileExists = os.path.exists(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+'/'+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                        if (fileExists):
                            #delete the file from the pre-processed folder
                            print("Cleaning up unnecessary file: "+"DTPipeline/BackupCopies/"+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                            os.remove(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+'/'+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                        else:
                            i = 0
                            #Split filename and extension
                            temp = data['jobQueue'][batchID][jobID][fileID]['fileName'].split('.')
                            while (fileExists == False or i >= int(sys.argv[1])):
                                i += 1
                                fileExists = os.path.exists(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+'/'+temp[0]+"("+str(i)+")."+temp[1])
                                if (fileExists == True):
                                    print("Cleaning up unnecessary file: "+data['jobQueue'][batchID][jobID][fileID]['filePathNP']+"/"+temp[0]+"("+str(i)+")."+temp[1])
                                    os.remove(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+'/'+temp[0]+"("+str(i)+")."+temp[1])
                    else:
                        if (batchID != prevBatchID):
                            prevBatchID = batchID
                            dataNew['jobQueue'][newBatchID] = {}
                            newBatchID += 1
                        if (jobID != prevJobID):
                            prevJobID = jobID
                            dataNew['jobQueue'][newBatchID][newJobID] = {}
                            newJobID += 1
                        if (fileID != prevFileID):
                            prevFileID = fileID
                            dataNew['jobQueue'][newBatchID][newJobID][newFileID] = {}
                            newFileID += 1
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePriority'] = filePriority
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['fileName'] = data['jobQueue'][batchID][jobID][fileID]['fileName']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathNP'] = data['jobQueue'][batchID][jobID][fileID]['filePathNP']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathP'] = data['jobQueue'][batchID][jobID][fileID]['filePathP']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathSettings'] = data['jobQueue'][batchID][jobID][fileID]['filePathSettings']
                        remainingFiles += 1
                        filePriority +=1

    if (remainingFiles > 0):
        from ProcessState import setProcessState
        setProcessState(0)
    else:
        os.remove("jobQueue.json")
        from ProcessState import setProcessState
        setProcessState(7)
else:
    from ProcessState import setProcessState
    setProcessState(2)
