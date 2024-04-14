#IMPORT LIBRARIES
import csv
import json
import sys

#DEFINE FUNCTION csv2json
def csv2json(csv_file_path, json_file_path):
    # Set a larger field size limit
    maxInt = sys.maxsize #This sets maxInt to the largest integer a variable can hold, which is typically 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.
    decrement = True

#The loop and try-except block are used to find the highest possible field size that does not cause an OverflowError. 
#This is necessary because, in some cases, setting the field size limit to a very high value might exceed the maximum integer size that the system or Python's CSV module can handle, leading to an OverflowError.
  
    while decrement:
        decrement = False   #The while loop continues as long as the decrement flag is True.
        try:
            csv.field_size_limit(maxInt)    # the code attempts to set the csv.field_size_limit() to maxInt.
        except OverflowError:
            maxInt = int(maxInt/10)      #If an OverflowError occurs (because maxInt is too large), the code catches this exception, reduces maxInt by dividing it by 10, and sets decrement to True to try again with this smaller value.
            decrement = True #This decrementing continues until the csv.field_size_limit() can accept the value without throwing an OverflowError.

    # Open the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        # Read the CSV file into a dictionary
        csv_reader = csv.DictReader(csv_file)
        
        # Create a list to hold all rows. initialize the variable
        data = []
        
        # Iterate over each row in the CSV
        for row in csv_reader:
            # Add the row to the list
            data.append(row)
    
    # Write the data to a JSON file
    with open(json_file_path, mode='w') as json_file:
        # Write the data as JSON
        json.dump(data, json_file, indent=4)

# Define csv file path in variable or you can take input or sysargv
csv_file_path = './final_output.csv'  # Replace with your CSV file path
json_file_path = './final_output.json'  # Replace with desired JSON file path

#run function csv2json with parameters csv and json file paths
csv2json(csv_file_path, json_file_path)
