import pickle
import pandas as pd
import sys
sys.path.append(sys.argv[1])
from signal_udfs import unpickle

#Import variables from wrapper
file_handle = sys.argv[2]
save_handle = sys.argv[3]
data_dict = unpickle([sys.argv[4]])[0]

#Make list of data_dict keys for column headers
col_names = list(data_dict.keys())

#Write column names to output file
main_output = open(save_handle[:-4] + '_main_output.csv', 'w')
main_output.write(','.join(col_names) + '\n')

#Write data to output file
current_line = []

for name in col_names:
	current_line.append(str(data_dict[name]))
main_output.write(','.join(current_line) + '\n')
