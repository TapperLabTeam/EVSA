import pandas as pd
import sys
import pickle

#Import variables from sys input
file_handle = sys.argv[1]
save_handle = sys.argv[2]

#Import data from input file
imported_data = []

for line in open(file_handle):
    line = line.strip().split(',')
    imported_data.append(line[0])

#Collect events and timestamps
event_dict = {'Events': [], 'Time (s)': []}

event_start = 0
timestamp_start = 0
temp_time = 0 #Used for ending timestamp collection

for item in imported_data:
    if item == '989898':
        event_start = 1
    if item == '878787':
        event_start = 0
        timestamp_start = 1
    if event_start == 1 and timestamp_start == 0 and item != '989898':
        event_dict['Events'].append(item)
    if event_start == 0 and timestamp_start == 1 and item != '878787':
        if float(item) > temp_time or float(item) == temp_time:
            temp_time = float(item)
            event_dict['Time (s)'].append(item)
        if float(item) < temp_time:
            break
            
#Decode event types

        
#Save decoded event log as .csv
if event_dict['Events'] != []:
	decoded = []
	for item in event_dict['Events']:
		if item == '111':
			decoded.append('Active Poke')
		if item == '222':
			decoded.append('Inactive Poke')
		if item == '333':
			decoded.append('Puff')
	event_dict['Events'] = decoded
	event_dict_df = pd.DataFrame.from_dict(event_dict)
	event_dict_df.to_csv(save_handle[:-4] + '_event_log.csv', index = False)

if event_dict['Events'] == []:
	print('**NO EVENTS RECORDED FOR' + ' ' + file_handle)
	event_dict['Events'] = 'NaN'
	event_dict['Time (s)'] = 'NaN'
	event_dict_output = open(save_handle[:-4] + '_event_log.csv', 'w')
	title_line = ['Events', 'Time (s)']
	line_2 = ['NaN', 'NaN']
	event_dict_output.write(','.join(title_line) + '\n')
	event_dict_output.write(','.join(line_2) + '\n')

pickle.dump(event_dict, open('event_dict.pkl','wb'))