import json

#Read a json file
with open('DTPipeline/Settings/Temp/jobQueue.json') as json_file:
    data = json.load(json_file)
    for batchID in data['jobQueue']:
        for jobID in data['jobQueue'][batchID]:
            for fileID in data['jobQueue'][batchID][jobID]:
                if (data['jobQueue'][batchID][jobID][fileID]['filePriority'] != 0):
                    print('File Priority: ' +str(data['jobQueue'][batchID][jobID][fileID]['filePriority']))
                    print('Name: ' +data['jobQueue'][batchID][jobID][fileID]['fileName'])
                    print('File path non-processed: ' +data['jobQueue'][batchID][jobID][fileID]['filePathNP'])
                    print('File path processed: ' +data['jobQueue'][batchID][jobID][fileID]['filePathP'])
                    print('File path settings: ' +data['jobQueue'][batchID][jobID][fileID]['filePathSettings'])
                    print('')
