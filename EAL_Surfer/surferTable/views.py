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
        contaminantNameList = request.GET.getlist('ContaminantName', '')

        # scrub input list to convert to UTF8 format
        contaminantNameList = convertDataToUTF8Format(contaminantNameList)

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
                    'contaminantType': contaminantType }

        # make sure all values are filled out before computation
        if landUse != 'base' and groundWaterUtility != 'base' and distanceToNearest != 'base' and contaminantNameList:
            print landUse
            #  only do lookup if values are from the available list
            if (contaminantType == contaminantTypeCas) or (contaminantType == contaminantTypeChemical):
                # convert CAS to chemical name
                if contaminantType == contaminantTypeCas:
                    temp = []
                    # convert each CAS value into their mapped contaminant name
                    for contaminantName in contaminantNameList:
                        temp.append(convertCASNameToChemicalName(contaminantName))
                    contaminantNameList = temp

            # return contaminant list for template (view side) processing
            response['contaminantNameList'] = contaminantNameList
            # three separate lists to store final EALs per each contaminant selected
            soil = []
            groundWater = []
            soilVapor = []
            iteration = 1

            # process each contaminant individually and store result in list
            for contaminantName in contaminantNameList:
                # pass user inputs to compiler logic and get a dictionary of results back
                resultDict = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)
                soil.append(resultDict.get('soil'))
                groundWater.append(resultDict.get('groundWater'))
                soilVapor.append(resultDict.get('soilVapor'))

                # get chemicalSummaryTemplateList and surferReportTemplateList from utility file
                # each contaminant needs two template files (PDFs) to be outputed
                # continuous generate all the PDFs and combine them into one at the end
                # called 'result.pdf' so user could download it
                replace_template('chem', chemicalSummaryTemplate, iteration, chemicalSummaryTemplateList, resultDict.get('chemicalSummaryResultList'))
                replace_template('surf', surferReportTemplate, iteration, surferReportTemplateList, resultDict.get('surfReportResultList'))
                numFile = str(iteration)
                # convert HTMLs into PDFs
                convertHtmlToPDF('chem' + numFile + '.html', 'chem' + numFile + '.pdf')
                convertHtmlToPDF('surf' + numFile + '.html', 'surf' + numFile + '.pdf')
                iteration += 1

            # store all data back into list and pass it back to template side (view side)
            response['soilList'] = soil
            response['groundWaterList'] = groundWater
            response['soilVaporList'] = soilVapor
            # zip everything up for easy access/process in the template side (view side)
            response['contaminantResults'] = zip(contaminantNameList, soil, groundWater, soilVapor)
            response['pdfFile'] = 'result.pdf'

    return render(request, 'index.html', response)