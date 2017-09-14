import sys
import os
import subprocess
import re

if __name__ == "__main__":
	csvToTableExeLoc = 'C:\\Python27\\Scripts\\' #path of cvsToTable (open source project; installed via pip) 
	inputOutputLoc = 'C:\\temp\\'	#out put dir
	for filename in os.listdir(sys.argv[1]):
			if filename.endswith(".csv"): 
				htmlName = re.sub(r'csv', 'html', filename)
				args = [csvToTableExeLoc + 'csvtotable', inputOutputLoc + filename, inputOutputLoc + htmlName]
				subprocess.call( args )
            
