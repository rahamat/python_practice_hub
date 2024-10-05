import glob
import os
from project1 import *


""" Project 2
    Traverse through folder tree and filter pdf files
Requirements
    Add sub-folders called “One”, “Two”, “Three” under the folder called “/content”
    Add PDF files under each of the sub-folders
    Load all PDF files under the sub-folders and load the PDF content
    Write the content to a text file called “output.txt” under each sub-folder respectively
Error Handling
    Take care of case where folder is not available
    Take care of case where PDF file is not present in a sub-folder
    Take care of case where the output.txt file is not available in a sub-folder
"""


print()
print("Current working directory :  " + os.getcwd())
rootPath = "content"
print()



for dir in listDirectories(rootPath):
    pdfFiles = glob.glob(dir + "/*.pdf", recursive=False)
    for read_file_path in pdfFiles:
        print("\t" + read_file_path +" is written to text file")
        try:
            validate_paths({dir : 'dir',read_file_path : 'file'})
        except ValueError as e:
            print(e)  
            sys.exit(1)
        reader = open_pdf(read_file_path)
        numberOfPages = no_pages_in_pdf(reader)
        print("No of pages in pdf : " , numberOfPages)
        print("writing pdf in to the path " , write_file_path)
        f = openFile(write_file_path, "w")
        for pg_no in range(1, numberOfPages):
            writeToFile(f,read_page_in_pdf(reader,pg_no))
            writeToFile(f, "\n~~~~~~~~~~~~~page~~separator~~~~~~~~~~~~~~~~~~~~\n")
        closeFile(f);