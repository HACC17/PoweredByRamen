# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from compiler import surferTableInput
from utility import *
from surferTable.models import Allchemicals
import pdfkit
from django.templatetags.static import static
import os

def index(request):

    # get drop down list values from specific columns of config table
    listOfChemicalNames = [chemical.encode("utf8") for chemical in Allchemicals.objects.values_list('c3', flat=True)]
    listOfChemicalNames.pop(0) # pop off the column header
    listOfCASNames = [chemical.encode("utf8") for chemical in Allchemicals.objects.values_list('c2', flat=True)]
    listOfCASNames.pop(0) # pop off the column header

    if request.method == 'GET':
    
        landUse = request.GET.get('LandUse', '')
        groundWaterUtility = request.GET.get('GroundWaterUtility', '')
        distanceToNearest = request.GET.get('DistanceToNearest', '')
        contaminantType = request.GET.get('ContaminantType', '')
        contaminantName = request.GET.getlist('ContaminantName')
		##############################################################
        #TODO temp code, please remove once multi chem names are working
        if contaminantName:
            contaminantName = contaminantName[0]
		##############################################################
        print contaminantName
        response = {'listOfChemicalNames': listOfChemicalNames,
                    'listOfCASNames': listOfCASNames,
                    'landUse': landUse,
                    'groundWaterUtility': groundWaterUtility,
                    'distanceToNearest': distanceToNearest,
                    'contaminantType': contaminantType,
                    'contaminantName': contaminantName }

        # Windows and *nix machines behave differently
        if os.name != 'nt':
            # package would not install correctly, installed manually and set explicit path
            config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
            options = {
                'quiet': '',
                'page-size': 'B7',
                'margin-top': '0.35in',
                'margin-right': '0.25in',
                'margin-bottom': '0.25in',
                'margin-left': '0.30in',
                'disable-smart-shrinking': ''
            }
            pdfkit.from_file('surfertable/templates/chemical_summary_template.html', 'surfertable/static/test.pdf', configuration = config, options = options)
        else:
            options = {
                'quiet': '',
                'page-size': 'B4',
                'margin-top': '0.45in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '1.00in',
                'disable-smart-shrinking': ''
            }
            pdfkit.from_file('surfertable/templates/surfer_report_template.html', 'surfertable/static/test.pdf', options = options)

        response['pdfFile'] = 'test.pdf'
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="test.pdf"'

        # make sure all values are filled out before computation
        if landUse and groundWaterUtility and distanceToNearest and contaminantName:
            #  only do lookup if values are from the available list
            if (contaminantType == contaminantTypeCas) or (contaminantType == contaminantTypeChemical):
                # convert CAS to chemical name
                if contaminantType == contaminantTypeCas:
                    contaminantName = convertCASNameToChemicalName(contaminantName)

            # pass user inputs to compiler logic
            [soil, groundWater, soilVapor] = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)
            response['soil'] = soil
            response['groundWater'] = groundWater
            response['soilVapor'] = soilVapor
            print "it reached here"
            return render(request, 'index.html', response)

    return render(request, 'index.html', response)