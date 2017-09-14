'''
1. clean up csv files provided by grabbing only data fromc
   chemical 'ACENAPHTHENE' to 'ZINC' (update these values if needed in the future e.g
   new chemical names had been added that precedes ACENAPHTHENE)
   add generic header column in csv files e.g c1, c2, c3... etc. based on cvs one row data count
2. dump cleaned up csv files into sqlite database named 'EAL_SURFER_TABLES_DB.sqlite3', each csv file
   is it's own table in the database
3. run via. 'python parsedFile.py [location of csv files]'
'''

import tempfile
import sys
import os
import csv, sqlite3
import re

chemicalNameStart = 'CENAPHTHENE'
chemicalNameEnd = 'ZINC'
sqliteDBName = 'EAL_SURFER_TABLES_DB.sqlite3'

def create_db(filename):
      #strip extension out of filename to be used
      #as table name
      tableName = os.path.splitext(filename)[0]
      # sub '-' to '_' in for table names
      tableName = tableName.replace('-','_')
      con = sqlite3.connect(sqliteDBName)
      cur = con.cursor()
      headerInfo = ''
      
      # count generic header name per data file (first line of the file)
      # then dump csv data per file into each individual table
      with open(filename, 'r') as f:
           headerInfo = f.readline().strip()
      if headerInfo:
           dbExe = "CREATE TABLE " + tableName + " (" + headerInfo + ");"
           cur.execute(dbExe)

           with open(filename, 'r') as f:
                reader = csv.reader(f)
                for field in reader:
                    headerInfo = re.sub(r'c[0-9]*', '?', headerInfo)
                    dbExe = "INSERT INTO " + tableName + " VALUES (" + headerInfo + ");"
                    cur.execute(dbExe, field)

      con.commit()
      con.close()

def modify_file(filename):

      #Create temporary file read/write
      t = tempfile.NamedTemporaryFile(mode="r+")

      #Open input file read-only
      i = open(filename, 'r')

      startPrint = False

      #Copy input file to temporary file, modifying as we go
      for line in i:
           if chemicalNameStart in line:
                # Prepend generic header info in front of file
                tempString = ''
                # plus one to account for some csv file having a hidden column
                # because header column count > data count is okay, but not the other way around
                for count in range(1, len(line.split(','))+1):
                    tempString = tempString + "c"+str(count)+","
                # remove last not needed comma char, some if not all csv file have an extra useless column
                t.write(tempString[:-1]+"\n") 
                startPrint = True
           if chemicalNameEnd in line:
                t.write(line)
                startPrint = False
           if startPrint and line.strip():
                t.write(line)

      i.close() #Close input file

      t.seek(0) #Rewind temporary file to beginning

      o = open(filename, "w")  #Reopen input file writable

      #Overwriting original file with temporary file contents          
      for line in t:
           o.write(line)  

      t.close() #Close temporary file, will cause it to be deleted

if __name__ == "__main__":
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".csv"): 
            modify_file(filename)
            create_db(filename)
