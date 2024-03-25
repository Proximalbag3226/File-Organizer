#Import the librarys for interact with the system
import os 
import shutil

#Create a dictionary that contains the names of the files and your respective extensions
ext = {
    '.txt': 'Documents',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.jpg': 'Images',
    '.png': 'Images',
    '.jpeg': 'Images',
    '.exe': 'executables',  
    }

#Others is for files withe a non registered extension in the dictionary
default = 'others'

#Chose the path of the directory
file_path = input("Please enter the path of the file do you want to organize ").split()

#Create a list of files in the directory
files = os.listdir(file_path)

#We iterate in the list of archives in the file
for file in files:
    
    #Save the extension of the archives
    files_path_origin = os.path.join(file_path)
    
    #Check if the archive in the iteraction is a file and extract the extension and the names
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file)
        name_file = ext.get(extension.lower(), default)
        
        #Create the route to move the archive
        file_path_route = os.path.join(file_path, name_file)
        
        #Check if the route is exist 
        if not os.path.exists(file_path_route):
            os.makedirs(file_path_route)
        else:
            print("The file as already exists please try again ")
        
        #And finaly move the archive 
        shutil.move(files_path_origin, file_path_route)