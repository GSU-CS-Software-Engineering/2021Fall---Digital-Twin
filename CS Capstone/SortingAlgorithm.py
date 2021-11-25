import os
import sys
import json
import glob
import time

#initialize variables
numBatches = 0
jobID = 0
data = {}

#If there was a previous job, count the number of batches already in the queue
if (os.path.exists('DTPipeline/Settings/Temp/jobQueue.json')):
    #Read a json file
    file1 = open('DTPipeline/Settings/Temp/jobQueue.json', 'r')
    with file1 as json_file1:
        data = json.load(json_file1)
        file1.close()
        for batchID in data['jobQueue']:
            numBatches += 1
        numBatches += 1
        data['jobQueue'][numBatches] = {}

else:
    data['jobQueue'] = {}

#Import and sort list of files to be processed, then append them to jobQueue.json
file2 = open('DTPipeline/Settings/Temp/fileListUnsorted.json', 'r')
with file2 as json_file2:
    unsortedFiles = json.load(json_file2)
    file2.close()
    print("Unsorted files: ", unsortedFiles)
#    time.sleep(3)
    from operator import itemgetter
    sortedFiles = {}
    for listID in unsortedFiles:
        listID = int(listID)
        sortedFiles[str(listID)] = {}
        sortedFiles[str(listID)]['settingsFile'] = unsortedFiles[str(listID)]['settingsFile']
        sortedFiles[str(listID)]['conversionFileList'] = {}
        unsortedList = []
        for fileID in unsortedFiles[str(listID)]['conversionFileList']:
            unsortedList.append(unsortedFiles[str(listID)]['conversionFileList'][str(fileID)]['fileName'])
        unsortedList.sort()
        for i in range(len(unsortedList)):
            sortedFiles[str(listID)]['conversionFileList'][str(i)] = {}
            for j in range(len(unsortedList)):
                if (unsortedList[i] == unsortedFiles[str(listID)]['conversionFileList'][str(j)]['fileName']):
                    sortedFiles[str(listID)]['conversionFileList'][str(i)]['fileName'] = unsortedFiles[str(listID)]['conversionFileList'][str(j)]['fileName']
                    sortedFiles[str(listID)]['conversionFileList'][str(i)]['filePath'] = unsortedFiles[str(listID)]['conversionFileList'][str(j)]['filePath']
    print("Sorted files: ", sortedFiles)
#    time.sleep(10)
    data['jobQueue'][numBatches] = {}
    for listID in sortedFiles:
        listID = int(listID)
        data['jobQueue'][numBatches][listID] = {}
        filePriority = 0
        for fileID in sortedFiles[str(listID)]['conversionFileList']:
            fileID = int(fileID)
            data['jobQueue'][numBatches][listID][fileID] = {}
            data['jobQueue'][numBatches][listID][fileID]['filePriority'] = filePriority
            data['jobQueue'][numBatches][listID][fileID]['fileName'] = sortedFiles[str(listID)]['conversionFileList'][str(fileID)]['fileName']
            data['jobQueue'][numBatches][listID][fileID]['filePathNP'] = sortedFiles[str(listID)]['conversionFileList'][str(fileID)]['filePath'] + '/'
            data['jobQueue'][numBatches][listID][fileID]['filePathP'] = 'DTPipeline/Processed'+'/'
            data['jobQueue'][numBatches][listID][fileID]['filePathSettings'] = sortedFiles[str(listID)]['settingsFile']
            filePriority += 1
    file = open('DTPipeline/Settings/Temp/jobQueue.json', 'w')
    with file as json_file3:
        json.dump(data, json_file3)
        file.close()

if (True):
    #Set the process state to 3
    from ProcessState import setProcessState
    print("From: "+str(sys.argv[0]))
    setProcessState(4)
else:
    print("Something went wrong, exit Queue")
    #Set the process state to -1
    from ProcessState import setProcessState
    print("From: "+str(sys.argv[0]))
    setProcessState(-1)#Tell controller to exit
