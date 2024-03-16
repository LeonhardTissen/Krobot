import json

def saveAsJson(parsedData):
	# Save the json data to a file with indentations
	data = json.dumps(parsedData, indent=4)
	with open('save.json', 'w') as file:
		file.write(data)
		file.close()
