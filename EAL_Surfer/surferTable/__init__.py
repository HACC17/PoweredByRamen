from utility import *

# init package by connect to db and retrieving config settings
conn = db.connect(dbName)
conn.row_factory = lambda cursor, row: row[0]
conn.text_factory = str
c = conn.cursor()
# get drop down list values from specific columns of config table
listOfChemicalNames = c.execute('SELECT c3 FROM ' + configTableName).fetchall()
listOfChemicalNames.pop(0) # pop off the column header
listOfCASNames = c.execute('SELECT c2 FROM ' + configTableName).fetchall()
listOfCASNames.pop(0) # pop off the column header