#Analyzes photometry data from electronic vapor self-administration
#Requires .csv of MED-PC data

import os
import subprocess

#OPTIONS
input_folder = 'C:/Users/Tim/Documents/Python/EVSA/input_folder'
output_folder = 'C:/Users/Tim/Documents/Python/EVSA/output_folder'
udf_path = 'C:/Users/Tim/Documents/Python/UDFs'

#Main wrapper loop
input_files = os.listdir(input_folder)

for file_name in input_files:
	print('Processing: ' + file_name + '...')
	file_handle = input_folder + '/' + file_name
	save_handle = output_folder + '/' + file_name
	subprocess.call(['python', 'evsa_extract.py', file_handle, save_handle])
	subprocess.call(['python', 'evsa_blocks.py', udf_path, file_handle, save_handle, 'event_dict.pkl'])
	subprocess.call(['python', 'evsa_output.py', udf_path, file_handle, save_handle, 'data_dict.pkl'])

print('Done')