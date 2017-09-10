# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
# -*- coding: utf-8 -*-

# Create your views here.
#from django.http import HttpResponse
#from django.template import Context, loader
import sqlite3 as db
from django.shortcuts import render


conn = db.connect('EAL_SURFER_TABLES_DB.sqlite3')
conn.row_factory = lambda cursor, row: row[0]
conn.text_factory = str
c = conn.cursor()
listOfchemicalNames = c.execute('SELECT c3 FROM allchemicals').fetchall()
listOfchemicalNames.pop(0)
listOfCASNames = c.execute('SELECT c2 FROM allchemicals').fetchall()
listOfCASNames.pop(0)

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #template = loader.get_template("index.html")
    #return HttpResponse(template.render())

    #if request.POST.get("base", "") == 'chemical':
    #    dropDownlistValue = listOfchemicalNames
    #

    return render(request, 'index.html', {'listOfchemicalNames': listOfchemicalNames, 'listOfCASNames' : listOfCASNames })
