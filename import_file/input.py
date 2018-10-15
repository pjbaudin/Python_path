'''
Import json data
2018-10-15
'''

# Import library
import os
import json

# Set the workign directory
wd = "C:/Users/pierr/Documents/GitHub/Python_Path/import_file"
os.chdir(wd)

# Open file and read json input file
with open('input.json', 'r') as input:
    obj = json.load(input)
    with open('output.txt', 'w') as output:
        output.write(obj['name'] + "'s hobbies:\n")
        for hobby in obj['hobbies']:
            output.write(hobby + "\n")



