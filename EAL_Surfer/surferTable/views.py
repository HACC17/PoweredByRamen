# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from surferTable import listOfChemicalNames, listOfCASNames
from compiler import surferTableInput
from utility import *


def index(request):
    soil = ''
    groundWater = ''
    soilVapor = ''

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
            [soil, groundWater, soilVapor] = surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName)

            #print soil
            #print groundWater
            #print soilVapor

    return render(request, 'index.html', {'listOfChemicalNames': listOfChemicalNames,
                                          'listOfCASNames': listOfCASNames,
                                          'soil': soil,
                                          'groundWater': groundWater,
                                          'soilVapor': soilVapor})
