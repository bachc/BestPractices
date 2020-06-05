"""
This tool makes folder structures based on an excel input file

Note: Folders that do not have subfolders need to be labelled as
"Not applicable" in the subfolder column.

Created 03/15/2020 cbach
Modified to allow multiple spreadsheets

Todo:
- enable hierarchical structure support
- enable richer readme file generation
- pep8 checking of file itself
"""

import os
import pandas as pd


def make_folders(FOLDER_INPUT, basedir, folderbase, FolderNumbering=True):
    #this needs some documentation - for now, use examples in ___main___
    for line in range(0,len(FOLDER_INPUT)):
        FolderTemp=basedir+folderbase  #String used to build the folder info
        try: os.mkdir(FolderTemp) #this will throw an error if the folder is already there!
        except: pass
        if FolderNumbering:
            FolderTemp+=str(FOLDER_INPUT.loc[line,"ID"])+"_"
        #Make folders
        FolderTemp+=FOLDER_INPUT.loc[line,"Folder"]
        if not FOLDER_INPUT.loc[line,"Subfolder"]=='Not applicable':
             FolderTemp+="_"+FOLDER_INPUT.loc[line,"Subfolder"]
        try:
            os.mkdir(FolderTemp) #this will throw an error if the folder is already there!
            print("Making ", FolderTemp)
        except:
            print("Folder " +FolderTemp +" already there or something else doesn't work quite right")
        try:
            text_file = open(FolderTemp+"\\readme.txt", "w")
            n = text_file.write(FOLDER_INPUT.loc[line,"Readme"])
            text_file.close()
        except:
            print("Folder " +FolderTemp +" can't write readme file - is it open?")


if __name__ == '__main__':
    # MAE 4344 Generic Structure
    FOLDER_INPUT= pd.read_excel("GenericFolderStructures.xlsx","MAE4344")
    FolderNumbering=True
    basedir=os.getcwd()
    folderbase="\\MAE4344\\"
    make_folders(FOLDER_INPUT, basedir, folderbase, FolderNumbering=True)
    
    # MSPhD Generic Structure
    FOLDER_INPUT= pd.read_excel("GenericFolderStructures.xlsx","MSPhD")
    FolderNumbering=True
    basedir=os.getcwd()
    folderbase="\\MSPhD\\"
    make_folders(FOLDER_INPUT, basedir, folderbase, FolderNumbering=True)

    # MAE3153 Generic Structure
    FOLDER_INPUT= pd.read_excel("GenericFolderStructures.xlsx","MAE3153")
    FolderNumbering=True
    basedir=os.getcwd()
    folderbase="\\MAE3153\\"
    make_folders(FOLDER_INPUT, basedir, folderbase, FolderNumbering=True)
