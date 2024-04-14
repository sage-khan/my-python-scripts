#The provided Python code is a script that automates the conversion of PDF files to text files using the pdftotext command-line tool. 
#It's structured to be run in a directory containing PDF files, and it will convert each PDF file it finds into a corresponding text file with similar naming but a .txt extension.

#import libraries
import os #This module provides a portable way of using operating system-dependent functionality. In this script, it's used to interact with the file system.
import subprocess #This module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It's used here to run external commands (specifically pdftotext).


#This function takes a single argument, pdf_file, which is the path to a PDF file. 
#It constructs the corresponding text file name by replacing the .pdf extension with .txt. 
#It then constructs a command to run the pdftotext utility with options:
#-layout: Preserves the original physical layout of the text as much as possible.
#-nopgbrk: Does not insert page break characters between pages.
#The command is executed using subprocess.run, which runs the command described by the list of arguments.

def convert_pdf_to_text(pdf_file):
    # Generate txt filename by replacing '.pdf' with '.txt'
    txt_file = pdf_file.replace('.pdf', '.txt')
    
    # Use pdftotext command to convert pdf to txt with flags -layout and -nopgbrk
    command = ['pdftotext', '-layout', '-nopgbrk', pdf_file, txt_file]
    subprocess.run(command)


def main(): #main: This function orchestrates the whole process.
    # Get current directory 
    current_dir = os.getcwd() #os.getcwd(): Retrieves the current working directory.

    # List all files in the current directory
    files = os.listdir(current_dir) #os.listdir(current_dir): Lists all files in the current directory.

    # Filter out only pdf files
    pdf_files = [f for f in files if f.endswith('.pdf')] #List comprehension: Filters the list of files to include only those that end with .pdf.

    # Convert each pdf file to txt #Loop: For each PDF file found, it calls convert_pdf_to_text to convert it to a text file, and then prints a message indicating the conversion
    for pdf_file in pdf_files:
        convert_pdf_to_text(pdf_file)
        print(f"Converted {pdf_file} to {pdf_file.replace('.pdf', '.txt')}")  #Confirms the conversion of pdf to text

#This block ensures that the main function is called only if the script is executed as the main program. 
#It prevents main from being called if the script is imported as a module in another script.
if __name__ == "__main__":
    main()   
