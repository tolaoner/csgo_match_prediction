#function that creates json file and writes the data on it
def write_to_json(filename,data_list):
	import json
	with open(f'{filename}.json','w') as jsonfile:
		json.dump(data_list, jsonfile)
