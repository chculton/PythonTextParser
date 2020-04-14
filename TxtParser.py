# re is python library regex, install with 'pip install regex'
import re;
import os;

# Initialize storage for parsed file data
textFileData = [];

# Get local directory
localDirectory = os.path.dirname(os.path.realpath(__file__));
fileToReadPath = localDirectory+"\\FileToParse.txt";

# Read file into reader variable
file = open(fileToReadPath);
try:
    for line in file: # Iterate through each line, storing data found between ':' and ';' in result
        result = re.search(':(.*);', line);
        textFileData.append(result.group(1)); # Store data in storage array
finally: # Close the file once reading is complete
    file.close()

# Print data stored in textFileData to the console
print(textFileData);
