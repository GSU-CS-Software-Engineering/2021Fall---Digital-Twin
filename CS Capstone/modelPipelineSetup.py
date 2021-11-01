import os


print("Running directory check...")
dirName = ["DTPipeline","DTPipeline/pre-processed","DTPipeline/processed","DTPipeline/Settings","DTPipeline/Settings/Batch Settings"]
missingDir = []
for dir in dirName:
    if not os.path.exists(dir):
        missingDir.append(dir)
if (len(missingDir) > 0):
    print("The following directories could not be found: ")
    for dir in missingDir:
        print(dir)
    print("")
else:
    print("All directories were successfully validated.")

print("Running File check...")
fileName = ["DTPipeline/Settings/Batch Settings/dummySettings.txt"]
missingFile = []
for file in fileName:
    if not os.path.exists(file):
            missingFile.append(file)
if (len(missingFile) > 0):
    print("The following files could not be found: ")
    for file in missingFile:
        print(file)
    print("")
else:
    print("All files were successfuly validated.")

if (len(missingDir) > 0 or len(missingFile) > 0):
    result = input("Would you like to set up the listed required directories and files? (Y/N)\n")
    while ((result != 'Y' and result != 'y' and result != 'N' and result != 'n')):
        result = input("Please enter a decision (Y/N): ")
    if (result == 'Y' or result == 'y'):
        for dir in missingDir:
            #Create target Directory if it does not already exist
            if not os.path.exists(dir):
                os.mkdir(dir)
                print("Directory " +dir +" created.")
            else:
                print("Directory " +dir +" already exists")
        for file in missingFile:
            #Create target file if it does not already exist
            try:
                #Write file to disk
                with open(file, 'w') as outfile:
                    print("File " +file +" created.")
            except FileExistsError:
                print("File " +file +" already exists")

    else:
        print("First time setup aborted.\nExiting.")
