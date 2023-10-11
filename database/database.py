import csv
import shelve

class Database():
    def store(self, databasePath, csvPath):
        with shelve.open(databasePath) as database:
            with open(csvPath, 'r', encoding='utf-8-sig') as csvFile:
                reader = csv.DictReader(csvFile)
                for row in reader:
                    database[row['Id']] = (row['Items'],row['Time'])

    def getSingleData(self, databasePath, item):
        with shelve.open(databasePath) as database:
            return database.get(item)


test = Database()
test.store("database/data.db", "testme.csv")
print(test.getSingleData("database\data.db", '1'))
   