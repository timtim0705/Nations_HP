import sys;
import os;
import subprocess;
import shutil;

# convertSolution [model_name] [csv_type] [var1, var2, ......]
# Converts [model_name].sl4 to [model_name].csv of [csv_type]
# Filter to only include results for [var1, var2, ......] by storing them in a .map file
 
# Input & Dependency: sltoht.exe, [model_name].sl4
# Output: [model_name.csv]

# Yuhan Guo
# 11/7/2022
'''
model_name = str(sys.argv[1])       # 1st argument passed is the shared filename stem for the model and all its related files.
                                    # Eg. 'GTAP.exe' with 'GTAP.cmf' should pass 'GTAP'
csv_type = str(sys.argv[2])         # eg. SES, SSS, etc. (see GEMPACK mannual 37.1, )
variables = sys.argv[3::]           # Rest are variables for .map file
'''

def convertSolution(model_name, csv_type):      
    # Calling sltoht.exe to convert .sl4 to .csv (See GEMPACK mannual 39.4 for details)
    # Format: sltoht.exe -[CSV type] -map=[map file name].map [sl4 file name] [output file name].csv
    subprocess.run(['sltoht.exe',\
                    '-' + csv_type,\
                    '-map=' + model_name + '.map',\
                    model_name,\
                    model_name + '.csv'])

# Creates .map file via given variables
# Note: variable of the form [var1:var2:var3:var4] will put var1-4 in a table as columns, while [var1, var2, var3, ...] will put each one in its own table.
#       both format can be used together, [var1:var2:var3:var4] will simply be treated as a single item.
# Example: [var1:var2:var3, var4, var5:var6] will put var1-3 side-by-side on the 1st table, var4 by itself on the 2nd, and var5-6 side-by-side on the 3rd
def makeMap(model_name, variables=[]):
    if(os.path.isfile(model_name + '.map') and len(variables) > 0):
        os.remove(model_name + '.map')
    try:
        with open(model_name + '.map', 'w+') as mf:
            for var in variables:
                mf.write(str(var) + '\n')
    except:
        print('Error writing .map file.')
        raise

# Cleans the SES format .csv file to keep it pandas-friendly
# Specifically, removes comment lines and trailing space/commas
def cleanSES(model_name):
    try:
        shutil.copy(model_name + '.csv', model_name + '-copy.csv')
        with open(model_name + '.csv', 'w+') as tf:
            with open(model_name + '-copy.csv', 'r') as sf:
                lines = sf.readlines()
                for line in lines:
                    if(len(line.lstrip()) > 0 and line.lstrip()[0] == '!'): # Skipping comment lines
                        continue
                    tf.write(line.rstrip(', \n') + '\n')                    # Copying while stripping trailing commas and spaces
        os.remove(model_name + '-copy.csv')
    except:
        print('Error cleaning .csv file.')
        raise

# TODO Placeholder
def cleanSSS(model_name):
    pass

    
# Different sltoht.exe options produce CSV with different format 
# which requires different cleaning procedures
def cleanCSV(model_name, csv_type):
    csv_type = csv_type.upper()
    if(csv_type == 'SES'):
        cleanSES(model_name)
    elif(csv_type == 'SSS'):
        cleanSSS(model_name)
    else:
        print('Unknown CSV type')
            
'''
makeMap(model_name, variables)
convertSolution(model_name, csv_type)
cleanCSV(model_name, csv_type)
'''