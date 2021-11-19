import os
import sys
import json
import subprocess

if (os.path.exists('fileListUnsorted.json')):
    os.remove('fileListUnsorted.json')
if (os.path.exists('DTPipeline/Settings/Temp/jobQueue.json')):
    dataNew = {}
    dataNew['jobQueue'] = {}
    remainingFiles = 0
    #Read a json file
    file = open('DTPipeline/Settings/Temp/jobQueue.json', 'r')
    with open('DTPipeline/Settings/Temp/jobQueue.json') as json_file:
        data = json.load(json_file)
        file.close()
        newBatchID = -1
        prevBatchID = 0
        for batchID in data['jobQueue']:
            newJobID = -1
            prevJobID = 0
            print("Batch ID: " +str(batchID))
            for jobID in data['jobQueue'][batchID]:
                print("Job ID: " +str(jobID))
                filePriority = 1
                newFileID = -1
                prevFileID = 0
                for fileID in data['jobQueue'][batchID][jobID]:
                    remainingFiles += 1
                    print("File ID: " +str(fileID))
                    if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] == 0):
                        fileExists = os.path.exists(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                        if (fileExists):
                            #delete the file from the pre-processed folder
                            print("Cleaning up unnecessary file: "+"DTPipeline/Pre-processed/"+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                            os.remove(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                            remainingFiles -= 1
                        else:
                            i = 0
                            #Split filename and extension
                            temp = data['jobQueue'][batchID][jobID][fileID]['fileName'].split('.')
                            while (fileExists == False or i >= int(sys.argv[1])):
                                i += 1
                                fileExists = os.path.exists(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+temp[0]+"("+str(i)+")."+temp[1])
                                if (fileExists == True):
                                    from shutil import copy
                                    print("Cleaning up possibly unnecessary file (performing backup): "+data['jobQueue'][batchID][jobID][fileID]['filePathNP']+"/"+temp[0]+"("+str(i)+")."+temp[1])
                                    copy(str(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+temp[0]+"("+str(i)+")."+temp[1]), str("DTPipeline/BackupCopies/"+temp[0]+"("+str(i)+")."+temp[1]))
                                    print("Copying File: "+temp[0]+"("+str(i)+")."+temp[1])
                                    os.remove(data['jobQueue'][batchID][jobID][fileID]['filePathNP']+temp[0]+"("+str(i)+")."+temp[1])
                                    remainingFiles -= 1
                                elif (fileExists == False and i < int(sys.argv[1])):
                                    print("A file could not be found before the checking limit, removing file from queue list: "
                                    +"DTPipeline/Pre-processed/"+data['jobQueue'][batchID][jobID][fileID]['fileName'])
                                    data['jobQueue'][batchID][jobID][fileID]['filePiority'] = 0
                                    fileExists = True
                                    remainingFiles -= 1
                    else:
                        if (batchID != prevBatchID):
                            prevBatchID = batchID
                            newBatchID += 1
                            dataNew['jobQueue'][newBatchID] = {}
                        if (jobID != prevJobID):
                            prevJobID = jobID
                            newJobID += 1
                            dataNew['jobQueue'][newBatchID][newJobID] = {}
                        if (fileID != prevFileID):
                            prevFileID = fileID
                            newFileID += 1
                            dataNew['jobQueue'][newBatchID][newJobID][newFileID] = {}

                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePriority'] = filePriority
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['fileName'] = data['jobQueue'][batchID][jobID][fileID]['fileName']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathNP'] = data['jobQueue'][batchID][jobID][fileID]['filePathNP']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathP'] = data['jobQueue'][batchID][jobID][fileID]['filePathP']
                        dataNew['jobQueue'][newBatchID][newJobID][newFileID]['filePathSettings'] = data['jobQueue'][batchID][jobID][fileID]['filePathSettings']
                        filePriority +=1
                        remainingFiles -= 1


    if (remainingFiles > 0):
        from ProcessState import setProcessState
        print("From: "+str(sys.argv[0]))
        setProcessState(0)
    else:
        if (os.path.exists("DTPipeline/Settings/Temp/jobQueue.json")):
            os.remove("DTPipeline/Settings/Temp/jobQueue.json")
        from ProcessState import setProcessState
        print("From: "+str(sys.argv[0]))
        setProcessState(7)
else:
    from ProcessState import setProcessState
    print("From: "+str(sys.argv[0]))
    setProcessState(2)
