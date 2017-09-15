# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from compiler import surferTableInput
from utility import *
from utility import surferReoportrtTemplateList
from surferTable.models import Allchemicals
from django.templatetags.static import static

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

        # make sure all values are filled out before computation
        if landUse and groundWaterUtility and distanceToNearest and contaminantName:
            #  only do lookup if values are from the available list
            if (contaminantType == contaminantTypeCas) or (contaminantType == contaminantTypeChemical):
                # convert CAS to chemical name
                if contaminantType == contaminantTypeCas:
                    contaminantName = convertCASNameToChemicalName(contaminantName)
        
            # pass user inputs to compiler logic
            #[soil, groundWater, soilVapor] = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)
            #response['soil'] = soil
            #response['groundWater'] = groundWater
            #response['soilVapor'] = soilVapor
            surfReportTemplateList = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)
            response['soil'] = 1
            response['groundWater'] = 2
            response['soilVapor'] = 3

            replace_template('tempfile', 'surfer_report_template.html', 1, surferReoportrtTemplateList, surfReportTemplateList)
            convertHtmlToPDF('tempfile1.html', 'test.pdf') 
            response['pdfFile'] = 'test.pdf'
                        
    return render(request, 'index.html', response)