import sqlite3 as db
import math
from django.apps import apps

# utility vars
dbName = 'EAL_SURFER_TABLES_DB.sqlite3'
appName = 'surferTable'
configTableName = 'allchemicals'
# use in view file
contaminantTypeCas = 'CAS'
contaminantTypeChemical = 'Chemical'


# Helper function to look up mapping of CAS to chemical name
def convertCASNameToChemicalName(contaminantName):

    model = apps.get_model(appName, configTableName)
    chemicalName = model.objects.values_list('c3', flat=True).filter(c2__exact=contaminantName)
    return chemicalName[0]

	
# Helper function to look up db (translate of vlookup functionality)
def dbLookUp(column, table_name, contaminantName):

    model = apps.get_model(appName, table_name)
	# SELECT {column} FROM {table_name} WHERE c1 = {contaminantName}
    result = model.objects.values_list(column, flat=True).filter(c1__exact=contaminantName)
    result = result[0] # return as list of one
    if RepresentsFloat(result):
        return to_precision(float(result), 2)
    return result


# Helper function to look up db (translate of vlookup functionality)
def dbLookUpWithChemicalColumnSpecified(column, table_name, contaminantName_column, contaminantName):

    columnToFilter = contaminantName_column+'__exact'
    model = apps.get_model(appName, table_name)
	# SELECT {column} FROM {table_name} WHERE {contaminantName_colun} = {contaminantName}
	# using parameter '**{ columnToFilter: contaminantName } to dynamically filter out results
    result = model.objects.values_list(column, flat=True).filter(**{ columnToFilter: contaminantName })
    result = result[0] # return as list of one
    if RepresentsFloat(result):
        return to_precision(float(result), 2)
    return result

	
# Helper function to check if string is represents a float/convertible to float
def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Helper function to return the minimum value of a list (in sig fig notations)
def findMinFromList(inputList):
    tempList = []
    for val in inputList:
        # check to make sure the val is float convertible
        if RepresentsFloat(val):
            tempList.append(float(val))
    return to_precision(min(tempList), 2)

# Helper function
def to_precision(x, p):
    """
    returns a string representation of x formatted with a precision of p

    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """
    x = float(x)

    if x == 0.:
        return "0." + "0" * (p - 1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x / tens)

    if n < math.pow(10, p - 1):
        e = e - 1
        tens = math.pow(10, e - p + 1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens - x):
        n = n + 1

    if n >= math.pow(10, p):
        n = n / 10.
        e = e + 1

    m = "%.*g" % (p, n)

    if e < -2 or e >= p:
        out.append(m[0])
        if p > 1:
            out.append(".")
            out.extend(m[1:p])
        out.append('e')
        if e > 0:
            out.append("+")
        out.append(str(e))
    elif e == (p - 1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e + 1])
        if e + 1 < len(m):
            out.append(".")
            out.extend(m[e + 1:])
    else:
        out.append("0.")
        out.extend(["0"] * -(e + 1))
        out.append(m)

    return "".join(out)