import sqlite3 as db
import math

# utility vars
dbName = 'EAL_SURFER_TABLES_DB.sqlite3'
configTableName = 'allchemicals'
contaminantTypeCas = 'CAS'
contaminantTypeChemical = 'Chemical'


# Helper function to look up mapping of CAS to chemical name
def convertCASNameToChemicalName(contaminantName):
    conn = db.connect(dbName)
    c = conn.cursor()
    conn.text_factory = str
    c.execute('SELECT c3 FROM ' + configTableName + ' WHERE c2="{cn}"'. \
              format(cn=contaminantName))
    result = c.fetchall()
    return result[0][0]


# Helper function to look up db (translate of vlookup functionality)
def dbLookUp(column, table_name, contaminantName):
    conn = db.connect(dbName)
    c = conn.cursor()
    c.execute('SELECT {col} FROM {tn} WHERE c1="{cn}"'. \
              format(col=column, tn=table_name, cn=contaminantName))
    result = c.fetchall()
    return to_precision(float(result[0][0]), 2)


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