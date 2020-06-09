#import modules
import csv, json

csvFile = 'user_details.csv'
jsonFile = 'user_details.json'

#read csv file and delete password column
data = {}
with open(csvFile, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        user_id = csvRow['user_id']
        data['user_id'] = csvRow
        del csvRow["password"]

root = {}
root["user_details"] = data

#add all data to json file
with open(jsonFile, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
