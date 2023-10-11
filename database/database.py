import csv
import shelve

class Database():

    # Store data from a csv file into a shelve database
    def store(self, databasePath, csvPath):
        with shelve.open(databasePath) as database:
            with open(csvPath, 'r', encoding='utf-8-sig') as csvFile:
                reader = csv.DictReader(csvFile)
                for row in reader:
                    database[row['Id']] = (row['Item'],row['Time'])

    # Get data from the database using Id as the key
    def getSingleData(self, databasePath, key):
        with shelve.open(databasePath) as database:
            return database.get(key)
   