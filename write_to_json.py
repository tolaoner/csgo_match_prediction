def write_json(filename,data_list):
	#function that creates json file and writes the data on it
	import json
	with open(f'{filename}.json','w') as jsonfile:
		json.dump(data_list, jsonfile)
