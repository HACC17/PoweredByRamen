import sqlite3
from math import log10, floor
import math

# helper function (not being used)
def round_sig(x, sig=2):
	return round(x, sig-int(floor(log10(abs(x))))-1)

# helper function to convert percision to sig fig
def to_precision(x,p):
    """
    returns a string representation of x formatted with a precision of p

    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """

    x = float(x)

    if x == 0.:
        return "0." + "0"*(p-1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x/tens)

    if n < math.pow(10, p - 1):
        e = e -1
        tens = math.pow(10, e - p+1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens -x):
        n = n + 1

    if n >= math.pow(10,p):
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
    elif e == (p -1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e+1])
        if e+1 < len(m):
            out.append(".")
            out.extend(m[e+1:])
    else:
        out.append("0.")
        out.extend(["0"]*-(e+1))
        out.append(m)

    return "".join(out)
	
	
sqlite_file = 'EAL_SURFER_TABLES_DB.sqlite3'    # name of the sqlite database file
table_name = 'SummaryTableA'   # name of the table to be queried
id_column = 'c1'
column_2 = 'c2'
column_3 = 'c3'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT {coi1} FROM {tn} WHERE {cn}="TETRACHLOROETHANE, 1,1,2,2-"'.\
        format(coi1=column_2, tn=table_name, cn=id_column))
all_rows = c.fetchall()
print(float(all_rows[0][0]))
print to_precision(float(all_rows[0][0]), 2)
