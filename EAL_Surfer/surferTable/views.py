# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from utility import *
from surferTable import listOfChemicalNames, listOfCASNames
from compiler import *

def index(request):
    if request.method == 'GET':
        landUse = request.GET.get('LandUse', '')
        groundWaterUtility = request.GET.get('GroundWaterUtility', '')
        distanceToNearest = request.GET.get('DistanceToNearest', '')
        contaminantType = request.GET.get('ContaminantType', '')
        contaminantName = request.GET.get('ContaminantName', '')

        #  only do lookup if values are from the available list
        if (contaminantType == contaminantTypeCas) or (contaminantType == contaminantTypeChemical):
            # convert CAS to chemical name
            if contaminantType == contaminantTypeCas:
                contaminantName = convertCASNameToChemicalName(contaminantName)

            # pass user inputs to compiler
            surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)

            # debug print
            #lookUpValue = dbLookUp("c3", "SummaryTableA", contaminantName)
            #print lookUpValue
            #print soilTier1EALTablesLookUp(groundWaterUtility, distanceToNearest)
            #print finalGroundWaterActionLevelsLookUp(groundWaterUtility, distanceToNearest)
            #print soilActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
            #print groundWaterActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
            #print indoorAirAndSoilGasActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)

    return render(request, 'index.html', {'listOfChemicalNames': listOfChemicalNames, 'listOfCASNames': listOfCASNames})
