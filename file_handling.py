# Managing the file handling functionalities
import os
# OS is used to delete the files
File_A = open("New_File.txt", "w")
File_A.write("Creating a file and saving content in itself...")
File_A.close()
# Now appending the text from it
File_A = open("New_File.txt", "a")
File_A.writelines("\nAdding up new text data in the file for the purpse of practice...")
File_A.close()

if os.path.exists("New_File.txt"):
    os.remove("New_File.txt")
    print("Once we created a file, then check it, if it was present, We delete it....")
else:
    print("File already not exist:)")