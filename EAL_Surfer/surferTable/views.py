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

        siteName = request.GET.get('site_name', '')
        siteId = request.GET.get('site_id', '')
        siteaddress1 = request.GET.get('site_address1', '')
        siteaddress2 = request.GET.get('site_address2', '')
        siteaddress3 = request.GET.get('site_address3', '')
        dateofsearch = request.GET.get('date_of_search', '')

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

        # build response dictionary and return it back to page
        response = {'siteName': siteName,
                    'siteId': siteId,
                    'siteaddress1': siteaddress1,
                    'siteaddress2': siteaddress2,
                    'siteaddress3': siteaddress3,
                    'dateofsearch': dateofsearch,
                    'listOfChemicalNames': listOfChemicalNames,
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
        
            # pass user inputs to compiler logic and get a dictionary of results back
            resultDict = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName, '', '', '', siteName, siteId,
                                          siteaddress1, siteaddress2, siteaddress3, dateofsearch )
            response['soil'] = resultDict.get('soil')
            response['groundWater'] = resultDict.get('groundWater')
            response['soilVapor'] = resultDict.get('soilVapor')
            iteration = 1
            # get template list from utility file
            replace_template('chem', chemicalSummaryTemplate, iteration, chemicalSummaryTemplateList, resultDict.get('chemicalSummaryResultList'))
            replace_template('surf', surferReportTemplate, iteration, surferReoportrtTemplateList, resultDict.get('surfReportResultList'))
            convertHtmlToPDF('chem1.html', 'chem.pdf') 
            convertHtmlToPDF('surf1.html', 'surf.pdf') 

            response['pdfFile'] = 'test.pdf'
                        
    return render(request, 'index.html', response)