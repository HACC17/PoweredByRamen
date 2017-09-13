# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from compiler import surferTableInput
from utility import *
from surferTable.models import Allchemicals
import pdfkit

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
        contaminantName = request.GET.get('ContaminantName', '')
        response = {'listOfChemicalNames': listOfChemicalNames,
                    'listOfCASNames': listOfCASNames,
                    'landUse': landUse,
                    'groundWaterUtility': groundWaterUtility,
                    'distanceToNearest': distanceToNearest,
                    'contaminantType': contaminantType,
                    'contaminantName': contaminantName }
                    
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

            return render(request, 'index.html', response)

    return render(request, 'index.html', response)