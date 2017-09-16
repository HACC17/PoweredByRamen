# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from compiler import surferTableInput
from utility import *
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
        contaminantNameList = request.GET.getlist('ContaminantName', '')

        # scrub input list to convert to UTF8 format
        contaminantNameList = convertDataToUTF8Format(contaminantNameList)

        # build response dictionary and return it back to page
        response = {'listOfChemicalNames': listOfChemicalNames,
                    'listOfCASNames': listOfCASNames,
                    'landUse': landUse,
                    'groundWaterUtility': groundWaterUtility,
                    'distanceToNearest': distanceToNearest,
                    'contaminantType': contaminantType,
                    'contaminantName': contaminantNameList }

        # make sure all values are filled out before computation
        if landUse and groundWaterUtility and distanceToNearest and contaminantNameList:
            #  only do lookup if values are from the available list
            if (contaminantType == contaminantTypeCas) or (contaminantType == contaminantTypeChemical):
                # convert CAS to chemical name
                if contaminantType == contaminantTypeCas:
                    temp = []
                    for contaminantName in contaminantNameList:
                        temp.append(convertCASNameToChemicalName(contaminantName))
                    contaminantNameList = temp
                    response['contaminantName'] = contaminantNameList
            iteration = 1
            soil = []
            groundWater = []
            soilVapor = []
            for contaminantName in contaminantNameList:
                # pass user inputs to compiler logic and get a dictionary of results back
                resultDict = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)
                soil.append(resultDict.get('soil'))
                groundWater.append(resultDict.get('groundWater'))
                soilVapor.append(resultDict.get('soilVapor'))
                # get template list from utility file
                replace_template('chem', chemicalSummaryTemplate, iteration, chemicalSummaryTemplateList, resultDict.get('chemicalSummaryResultList'))
                replace_template('surf', surferReportTemplate, iteration, surferReportTemplateList, resultDict.get('surfReportResultList'))
                numFile = str(iteration)
                convertHtmlToPDF('chem' + numFile + '.html', 'chem' + numFile + '.pdf')
                convertHtmlToPDF('surf' + numFile + '.html', 'surf' + numFile + '.pdf')
                iteration += 1

            response['soil'] = soil
            response['groundWater'] = groundWater
            response['soilVapor'] = soilVapor
            response['pdfFile'] = 'result.pdf'

    return render(request, 'index.html', response)