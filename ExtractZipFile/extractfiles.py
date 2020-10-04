import os
import zipfile

zipFile = input("Enter zip File name (__.zip)\nif in other directory specify directory  :- ")

if os.path.isfile(zipFile):
        # mention path of zip file
        z_file = zipfile.ZipFile(zipFile)
        # Mention Directory or Folder in which You want to extract files
        z_file.extractall("MY_EXTRACTED_FOLDER")
        #close file after use
        z_file.close()
        print("Extracted Successfully")
else:
        print("File Not exist")

