import pickle
import pandas as pd
import sys
sys.path.append(sys.argv[1])
from signal_udfs import unpickle

#Import variables from wrapper
file_handle = sys.argv[2]
save_handle = sys.argv[3]
event_dict = unpickle([sys.argv[4]])[0]

#Create dictionary for binned data
data_dict = {'File Name': file_handle, 'B1 Active Time-In Pokes': 0, 'B1 Active Time-Out Pokes': 0, 'B1 Inactive Time-In Pokes': 0, 'B1 Inactive Time-Out Pokes': 0, 'B1 Total Active Pokes': 0, 'B1 Total Inactive Pokes': 0, 'B1 Puffs': 0, 'B2 Active Time-In Pokes': 0, 'B2 Active Time-Out Pokes': 0, 'B2 Inactive Time-In Pokes': 0, 'B2 Inactive Time-Out Pokes': 0, 'B2 Total Active Pokes': 0, 'B2 Total Inactive Pokes': 0, 'B2 Puffs': 0, 'B3 Active Time-In Pokes': 0, 'B3 Active Time-Out Pokes': 0, 'B3 Inactive Time-In Pokes': 0, 'B3 Inactive Time-Out Pokes': 0, 'B3 Total Active Pokes': 0, 'B3 Total Inactive Pokes': 0, 'B3 Puffs': 0, 'B4 Active Time-In Pokes': 0, 'B4 Active Time-Out Pokes': 0, 'B4 Inactive Time-In Pokes': 0, 'B4 Inactive Time-Out Pokes': 0, 'B4 Total Active Pokes': 0, 'B4 Total Inactive Pokes': 0, 'B4 Puffs': 0, 'Active Time-In Pokes': 0, 'Active Time-Out Pokes': 0, 'Total Active Pokes': 0, 'Inactive Time-In Pokes': 0, 'Inactive Time-Out Pokes': 0, 'Total Inactive Pokes': 0, 'Total Puffs': 0, 'Discrimination Index': 0}
#Group data in 4 30 minute bins
if event_dict['Events'] != 'NaN':
	#temp_time = -999
	ts = 0
	puff_time = 'NaN'
	time_check = 'NaN'
	for event_num, event in enumerate(event_dict['Events']):
		ts = float(event_dict['Time (s)'][event_num])
		#time_check = ts - temp_time
		if event == 'Puff':
			puff_time = ts
			if ts <= 1800: #Puff Block 1
				data_dict['B1 Puffs'] += 1
				data_dict['Total Puffs'] += 1
			if ts > 1800 and ts <= 3600: #Puff Block 2
				data_dict['B2 Puffs'] += 1
				data_dict['Total Puffs'] += 1
			if ts > 3600 and ts <= 5400: #Puff Block 3
				data_dict['B3 Puffs'] += 1
				data_dict['Total Puffs'] += 1
			if ts > 5400: #Puff Block 4
				data_dict['B4 Puffs'] += 1
				data_dict['Total Puffs'] += 1
		if event == 'Active Poke':
			if ts <= 1800: #Active Block 1
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B1 Active Time-In Pokes'] += 1
						data_dict['B1 Total Active Pokes'] += 1
						data_dict['Active Time-In Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
					if time_check < 60:
						data_dict['B1 Active Time-Out Pokes'] += 1
						data_dict['B1 Total Active Pokes'] += 1
						data_dict['Active Time-Out Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
				else:
					data_dict['B1 Active Time-In Pokes'] += 1
					data_dict['B1 Total Active Pokes'] += 1
					data_dict['Active Time-In Pokes'] += 1
					data_dict['Total Active Pokes'] += 1    
			if ts > 1800 and ts <= 3600: #Active Block 2
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B2 Active Time-In Pokes'] += 1
						data_dict['B2 Total Active Pokes'] += 1
						data_dict['Active Time-In Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
					if time_check < 60:
						data_dict['B2 Active Time-Out Pokes'] += 1
						data_dict['B2 Total Active Pokes'] += 1
						data_dict['Active Time-Out Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
				else:
					data_dict['B2 Active Time-In Pokes'] += 1
					data_dict['B2 Total Active Pokes'] += 1
					data_dict['Active Time-In Pokes'] += 1
					data_dict['Total Active Pokes'] += 1 
			if ts > 3600 and ts <= 5400: #Active Block 3
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B3 Active Time-In Pokes'] += 1
						data_dict['B3 Total Active Pokes'] += 1
						data_dict['Active Time-In Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
					if time_check < 60:
						data_dict['B3 Active Time-Out Pokes'] += 1
						data_dict['B3 Total Active Pokes'] += 1
						data_dict['Active Time-Out Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
				else:
					data_dict['B3 Active Time-In Pokes'] += 1
					data_dict['B3 Total Active Pokes'] += 1
					data_dict['Active Time-In Pokes'] += 1
					data_dict['Total Active Pokes'] += 1 
			if ts > 5400: #Active Block 4
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B4 Active Time-In Pokes'] += 1
						data_dict['B4 Total Active Pokes'] += 1
						data_dict['Active Time-In Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
					if time_check < 60:
						data_dict['B4 Active Time-Out Pokes'] += 1
						data_dict['B4 Total Active Pokes'] += 1
						data_dict['Active Time-Out Pokes'] += 1
						data_dict['Total Active Pokes'] += 1
				else:
					data_dict['B4 Active Time-In Pokes'] += 1
					data_dict['B4 Total Active Pokes'] += 1
					data_dict['Active Time-In Pokes'] += 1
					data_dict['Total Active Pokes'] += 1 
		if event == 'Inactive Poke':
			if ts <= 1800: #Inactive Block 1
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B1 Inactive Time-In Pokes'] += 1
						data_dict['B1 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-In Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
					if time_check < 60:
						data_dict['B1 Inactive Time-Out Pokes'] += 1
						data_dict['B1 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-Out Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
				else:
					data_dict['B1 Inactive Time-In Pokes'] += 1
					data_dict['B1 Total Inactive Pokes'] += 1
					data_dict['Inactive Time-In Pokes'] += 1
					data_dict['Total Inactive Pokes'] += 1 
			if ts > 1800 and ts <= 3600: #Inactive Block 2
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B2 Inactive Time-In Pokes'] += 1
						data_dict['B2 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-In Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
					if time_check < 60:
						data_dict['B2 Inactive Time-Out Pokes'] += 1
						data_dict['B2 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-Out Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
				else:
					data_dict['B2 Inactive Time-In Pokes'] += 1
					data_dict['B2 Total Inactive Pokes'] += 1
					data_dict['Inactive Time-In Pokes'] += 1
					data_dict['Total Inactive Pokes'] += 1 
			if ts > 3600 and ts <= 5400: #Inactive Block 3
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B3 Inactive Time-In Pokes'] += 1
						data_dict['B3 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-In Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
					if time_check < 60:
						data_dict['B3 Inactive Time-Out Pokes'] += 1
						data_dict['B3 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-Out Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
				else:
					data_dict['B3 Inactive Time-In Pokes'] += 1
					data_dict['B3 Total Inactive Pokes'] += 1
					data_dict['Inactive Time-In Pokes'] += 1
					data_dict['Total Inactive Pokes'] += 1 
			if ts > 5400: #Inactive Block 4
				if puff_time != 'NaN':
					time_check = ts - puff_time
					if time_check >= 60:
						data_dict['B4 Inactive Time-In Pokes'] += 1
						data_dict['B4 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-In Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
					if time_check < 60:
						data_dict['B4 Inactive Time-Out Pokes'] += 1
						data_dict['B4 Total Inactive Pokes'] += 1
						data_dict['Inactive Time-Out Pokes'] += 1
						data_dict['Total Inactive Pokes'] += 1
				else:
					data_dict['B4 Inactive Time-In Pokes'] += 1
					data_dict['B4 Total Inactive Pokes'] += 1
					data_dict['Inactive Time-In Pokes'] += 1
					data_dict['Total Inactive Pokes'] += 1

#Calculate discrimination index
if event_dict['Events'] != 'NaN':
	data_dict['Discrimination Index'] = ((float(data_dict['Total Active Pokes']) - float(data_dict['Total Inactive Pokes'])))/((float(data_dict['Total Active Pokes']) + float(data_dict['Total Inactive Pokes'])))

#Dump pickle of binned data
pickle.dump(data_dict,open('data_dict.pkl','wb'))
