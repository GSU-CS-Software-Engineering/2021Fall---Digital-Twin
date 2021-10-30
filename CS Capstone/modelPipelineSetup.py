import os

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
    result = input("Would you like to set up the listed required directories? (Y/N)\n")
    while ((result != 'Y' and result != 'y' and result != 'N' and result != 'n')):
        result = input("Please enter a decision (Y/N): ")
    if (result == 'Y' or result == 'y'):
        for dir in missingDir:
            #Create target Directory if it does not already exist
            if not os.path.exists(dir):
                os.mkdir(dir)
                print("Directory " +dir +" created ")
            else:
                print("Directory " +dir +" already exists")
    else:
        print("First time setup aborted.\nExiting.")
else:
    print("All directories were successfully validated.")
