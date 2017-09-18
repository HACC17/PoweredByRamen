"""
Translation of compiler logic from Surfer Table Compiler Excel sheet 
Quick implementation to get project going
See file 'surfer_table_compiler_logic_breakdown.docx' in the resource directory (top level) for more info

return a dictionary back in the form of:

{'soil': string, 
 'groundWater' : string, 
 'soilVapor' : string,
 'surfReportResultList': list of strings, 
 'chemicalSummaryResultList': list of strings }  
                  
TODO rework code to make it cleaner and model driven
"""

from utility import *
from summaryLogic import *

_landUse = ''
_groundWaterUtility = ''
_chemicalSelected = ''
_distanceToNearestSurfaceWaterBody = ''
_inputSoilConcentration = '-'
_inputGroundWaterConcentration = '-'
_inputSoilGasConcentration = '-'
_site_name = '' 
_site_address1 = ''
_site_address2 = ''
_site_address3 = ''
_site_id = ''
_date_of_search = ''

def surferTableInput(landUse, groundWaterUtility, distanceToNearest, contaminantName,
                     optional_inputSoilConcentration='', optional_inputGroundWaterConcentration='', optional_inputSoilGasConcentration='',
                     optional_site_name='', optional_site_address1='', optional_site_address2='',
                     optional_site_address3='', optional_site_id='', optional_date_of_search=''):
    _landUse = landUse
    _groundWaterUtility = groundWaterUtility
    _chemicalSelected = contaminantName
    _distanceToNearestSurfaceWaterBody = distanceToNearest
    #_inputSoilConcentration = optional_inputSoilConcentration
    #_inputGroundWaterConcentration = optional_inputGroundWaterConcentration
    #_inputSoilGasConcentration = optional_inputSoilGasConcentration
    _site_name = optional_site_name
    _site_address1 = optional_site_address1
    _site_address2 = optional_site_address2
    _site_address3 = optional_site_address3
    _site_id = optional_site_id
    _date_of_search = optional_date_of_search
    
    # compute the needed values
    soilActionLevelsList = soilActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    groundWaterActionLevelsList = groundWaterActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    indoorAirAndSoilGasActionLevelsList = indoorAirAndSoilGasActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)

    #print soilActionLevelsList
    #print '********'
    #print groundWaterActionLevelsList
    #print '********'
    #print indoorAirAndSoilGasActionLevelsList

    # clean up the for string sub in the templates
    [contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert] = selectedSiteScenarioConvert(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    
    # retrieve surfer report data and put it into a list
    surfReportTemplateList = findSurfReportTemplateReplaceList(_site_name, _site_address1, _site_address2, _site_address3, _site_id, _date_of_search,
                                                               contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert,
                                                               _inputSoilConcentration, _inputGroundWaterConcentration, _inputSoilGasConcentration,
                                                               soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList)
    # retrieve chemical summary data and put it into a list
    chemicalSummaryTemplateList = findChemicalSummaryTemplateReplaceList(contaminantNameConvert, landUseConvert,
                                                                soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList)
                                   
    # column 71, 88, 99 for soil, groundWater, and soilVapor
    # map to index -- ActionLevelsList[24], groundWaterActionLevelsList[10], indoorAirAndSoilGasActionLevelsList[5] 
    resultDict = {'soil': soilActionLevelsList[24], 
                  'groundWater': groundWaterActionLevelsList[10], 
                  'soilVapor': indoorAirAndSoilGasActionLevelsList[5],
                  'surfReportResultList': surfReportTemplateList, 
                  'chemicalSummaryResultList': chemicalSummaryTemplateList }  

    return resultDict
                
# Return table name based on permutation of groundwater utility and distance to nearest surface waster body inputs
def soilTier1EALTablesLookUp(groundWaterUtilityInput, distanceToNearestInput):
    tempString = ''
    if groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'TableA1'
    elif groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'lessthan':
        tempString = 'TableA2'
    elif groundWaterUtilityInput == 'nondrinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'TableB1'
    else:
        tempString = 'TableB2'
    return tempString

# Return table name based on permutation of groundwater utility and distance to nearest surface waster body inputs
def finalGroundWaterActionLevelsLookUp(groundWaterUtilityInput, distanceToNearestInput):
    tempString = ''
    if groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'lessthan':
        tempString = 'TableD1a'
    elif groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'TableD1b'
    elif groundWaterUtilityInput == 'nondrinking' and distanceToNearestInput == 'lessthan':
        tempString = 'TableD1c'
    else:
        tempString = 'TableD1d'
    return tempString

# Soil action levels logic
def soilActionLevels(contaminantNameInput, landUse, groundWaterUtilityInput, distanceToNearestInput):
    result = []

    ###################
    # Direct Exposure #
    ###################
    tableNameDirectExposureResidential = 'TableI1'
    tableNameDirectExposureCommercial = 'TableI2'
    tableNameDirectExposureConstruction = 'TableI3'
    tableColumnDirectExposure = 'c2'
    de_residential = dbLookUp(tableColumnDirectExposure, tableNameDirectExposureResidential, contaminantNameInput)
    de_commercial = dbLookUp(tableColumnDirectExposure, tableNameDirectExposureCommercial, contaminantNameInput)
    de_construction = dbLookUp(tableColumnDirectExposure, tableNameDirectExposureConstruction, contaminantNameInput)
    result.append(de_residential)
    result.append(de_commercial)
    result.append(de_construction)

    de_final = ''
    if landUse == 'unrestricted':
        de_final = de_residential
    else:
        de_final = de_commercial
    result.append(de_final)

    ###################
    # Vapor Intrusion #
    ###################
    tableNameVaporIntrusion = 'TableC1b'
    tableColumnResidentialVaporIntrusion = 'c5'
    tableColumnCommercialVaporIntrusion = 'c6'
    vi_residential = dbLookUp(tableColumnResidentialVaporIntrusion, tableNameVaporIntrusion, contaminantNameInput)
    vi_commercial = dbLookUp(tableColumnCommercialVaporIntrusion, tableNameVaporIntrusion, contaminantNameInput)
    result.append(vi_residential)
    result.append(vi_commercial)

    vi_final = ''
    if landUse == 'unrestricted':
        vi_final = vi_residential
    else:
        vi_final = vi_commercial
    result.append(vi_final)

    ############
    # Leaching #
    ############
    # TODO fix TableE either through csv file or parsing logic to not have an excess column 1
    tableNameLeaching = 'TableE' # it's called TableE instead of TableE1 in the csv file, and every column is shifted over 1
    tableColumnDWLessThanLeaching = 'c13' # csv is c12
    tableColumnDWGreaterThanLeaching = 'c14' # csv is c13
    tableColumnNDWLessThanLeaching = 'c15' # csv is c14
    tableColumnNDWGreaterThanLeaching = 'c16' # csv is c15
    l_dw_lessthan = dbLookUpWithChemicalColumnSpecified(tableColumnDWLessThanLeaching, tableNameLeaching, "c2", contaminantNameInput)
    l_dw_greatherthan = dbLookUpWithChemicalColumnSpecified(tableColumnDWGreaterThanLeaching, tableNameLeaching, "c2", contaminantNameInput)
    l_ndw_lessthan = dbLookUpWithChemicalColumnSpecified(tableColumnNDWLessThanLeaching, tableNameLeaching, "c2", contaminantNameInput)
    l_ndw_greatherthan = dbLookUpWithChemicalColumnSpecified(tableColumnNDWGreaterThanLeaching, tableNameLeaching, "c2", contaminantNameInput)
    result.append(l_dw_lessthan)
    result.append(l_dw_greatherthan)
    result.append(l_ndw_lessthan)
    result.append(l_ndw_greatherthan)

    l_final = ''
    if groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'lessthan':
        l_final = l_dw_lessthan
    elif groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'greaterthan':
        l_final = l_dw_greatherthan
    elif groundWaterUtilityInput == 'nondrinking' and distanceToNearestInput == 'lessthan':
        l_final = l_ndw_lessthan
    else:
        l_final = l_ndw_greatherthan
    result.append(l_final)

    ###########################
    # Terrestrial Ecotoxicity #
    ###########################
    tableNameTerrestrialEcotoxicity = 'TableL'
    tableColumnResidentialTerrestrialEcotoxicity = 'c2'
    tableColumnCommercialTerrestrialEcotoxicity = 'c3'
    te_residential = dbLookUp(tableColumnResidentialTerrestrialEcotoxicity, tableNameTerrestrialEcotoxicity, contaminantNameInput)
    te_commercial = dbLookUp(tableColumnCommercialTerrestrialEcotoxicity, tableNameTerrestrialEcotoxicity, contaminantNameInput)
    result.append(te_residential)
    result.append(te_commercial)

    te_final = ''
    if landUse == 'unrestricted':
        te_final = te_residential
    else:
        te_final = te_commercial
    result.append(te_final)

    #######################
    # Gross Contamination #
    #######################
    tableNameExposedSoilGrossContamination = 'TableF2'
    tableNameIsolatedSoilGrossContamination = 'TableF3'
    tableColumnResidentialGrossContamination = 'c2'
    tableColumnCommercialGrossContamination = 'c3'
    gc_residentialExposed = dbLookUp(tableColumnResidentialGrossContamination, tableNameExposedSoilGrossContamination, contaminantNameInput)
    gc_residentialIsolated = dbLookUp(tableColumnResidentialGrossContamination, tableNameIsolatedSoilGrossContamination, contaminantNameInput)
    gc_commercialExposed = dbLookUp(tableColumnCommercialGrossContamination, tableNameExposedSoilGrossContamination, contaminantNameInput)
    gc_commercialIsolated = dbLookUp(tableColumnCommercialGrossContamination, tableNameIsolatedSoilGrossContamination, contaminantNameInput)
    final_gc_residential = gc_residentialExposed
    final_gc_commercial = gc_commercialExposed

    result.append(gc_residentialExposed)
    result.append(gc_residentialIsolated)
    result.append(final_gc_residential)
    result.append(gc_commercialExposed)
    result.append(gc_commercialIsolated)
    result.append(final_gc_commercial)

    gc_final = ''
    if landUse == 'unrestricted':
        gc_final = final_gc_residential
    else:
        gc_final = final_gc_commercial
    result.append(gc_final)

    ###################
    # Lowest Soil EAL #
    ###################
    lowestSoilEAL = findMinFromList([de_final, vi_final, l_final, te_final, gc_final])
    result.append(lowestSoilEAL)

    ##############
    # Background #
    ##############
    tableNameBackGround = 'allchemicals'
    tableNameNestedBackGround = 'TableK'
    tableColumnBackground = 'c12' # Column number to look for the chemical code in the allchemicals config table
    chemicalColumnInBackGroundTable = 'c3' #This is the column for chemical names in the allchemicals config table
    tableColumnNestedBackground = 'c5'
    chemicalCode = dbLookUpWithChemicalColumnSpecified(tableColumnBackground, tableNameBackGround, chemicalColumnInBackGroundTable, contaminantNameInput)
    background = ''
    if chemicalCode == '2.0':
        backgroundValue = dbLookUp(tableColumnNestedBackground, tableNameNestedBackGround, contaminantNameInput)
        if backgroundValue == '':
            background = '?'
        else:
            background = backgroundValue
    else:
        background = '-'
    result.append(background)

    #########################
    # Final Tier 1 Soil EAL #
    #########################
    finalTier1SoilEAL = lowestSoilEAL
    if background == '-' or background == '?':
        finalTier1SoilEAL = lowestSoilEAL
    elif RepresentsFloat(background) and RepresentsFloat(lowestSoilEAL):
        if float(background) > float(lowestSoilEAL):
            finalTier1SoilEAL = background
    result.append(finalTier1SoilEAL)

    #########
    # Basis #
    #########
    basis = 'Gross Contamination'
    if finalTier1SoilEAL == background:
        basis = 'Background'
    elif finalTier1SoilEAL == de_final:
        basis = 'Direct Exposure'
    elif finalTier1SoilEAL == vi_final:
        basis = 'Vapor Intrusion'
    elif finalTier1SoilEAL == l_final:
        basis = 'Leaching'
    elif finalTier1SoilEAL == te_final:
        basis = 'Terrestrial Ecotoxicity'
    result.append(basis)

    return result

# Ground waster action levels logic
def groundWaterActionLevels(contaminantNameInput, landUse, groundWaterUtilityInput, distanceToNearestInput):
    result = []

    ###########################
    # Drinking Water Toxicity #
    ###########################
    tableNameDrinkingWaterToxicity = 'TableD3a'
    tableColumnDrinkingWaterToxicity = 'c2'
    drinkingWaterToxicity = dbLookUp(tableColumnDrinkingWaterToxicity, tableNameDrinkingWaterToxicity, contaminantNameInput)
    result.append(drinkingWaterToxicity)

    ###################
    # Vapor Intrusion #
    ###################
    tableNameVaporIntrusion = 'TableC1a'
    tableColumnResidentialVaporIntrusion = 'c5'
    tableColumnCommercialVaporIntrusion = 'c6'
    vi_residential = dbLookUp(tableColumnResidentialVaporIntrusion, tableNameVaporIntrusion, contaminantNameInput)
    vi_commercial = dbLookUp(tableColumnCommercialVaporIntrusion, tableNameVaporIntrusion, contaminantNameInput)
    result.append(vi_residential)
    result.append(vi_commercial)

    vi_final = ''
    if landUse == 'unrestricted':
        vi_final = vi_residential
    else:
        vi_final = vi_commercial
    result.append(vi_final)

    #######################
    # Aquatic Ecotoxicity #
    #######################
    tableNameAquaticEcotoxicity = 'TableD4a'
    tableColumnResidentialAquaticEcotoxicity = 'c2'
    tableColumnCommercialAquaticEcotoxicity = 'c3'
    ae_chronic = dbLookUp(tableColumnResidentialAquaticEcotoxicity, tableNameAquaticEcotoxicity, contaminantNameInput)
    ae_acute = dbLookUp(tableColumnCommercialAquaticEcotoxicity, tableNameAquaticEcotoxicity, contaminantNameInput)
    result.append(ae_chronic)
    result.append(ae_acute)

    ae_final = ''
    if distanceToNearestInput == 'lessthan':
        ae_final = ae_chronic
    else:
        ae_final = ae_acute
    result.append(ae_final)

    #######################
    # Gross Contamination #
    #######################
    tableNameDWGrossContamination = 'TableG1'
    tableNameNDWGrossContamination = 'TableG2'
    tableColumnGrossContamination = 'c2'
    gc_drinkingWater = dbLookUp(tableColumnGrossContamination, tableNameDWGrossContamination, contaminantNameInput)
    gc_nonDrinkingWater = dbLookUp(tableColumnGrossContamination, tableNameNDWGrossContamination, contaminantNameInput)
    result.append(gc_drinkingWater)
    result.append(gc_nonDrinkingWater)

    gc_final = ''
    if groundWaterUtilityInput == 'drinking':
        gc_final = gc_drinkingWater
    else:
        gc_final = gc_nonDrinkingWater
    result.append(gc_final)

    #######################
    # Final Tier 1 GW EAL #
    #######################
    finalTier1GWEAL = findMinFromList([drinkingWaterToxicity, vi_final, ae_final, gc_final])
    result.append(finalTier1GWEAL)

    #########
    # Basis #
    #########
    basis = 'Gross Contamination'
    if finalTier1GWEAL == drinkingWaterToxicity:
        basis = 'Drinking Waster Toxicity'
    elif finalTier1GWEAL == vi_final:
        basis = 'Final Vapor Intrusion'
    elif finalTier1GWEAL == ae_final:
        basis = 'Aquatic Ecotoxicity'
    result.append(basis)

    return result

# Indoor air and soil gas action levels logic
def indoorAirAndSoilGasActionLevels(contaminantNameInput, landUse, groundWaterUtilityInput, distanceToNearestInput):
    result = []

    ##############
    # Indoor Air #
    ##############
    tableNameIndoorAir = 'TableC3'
    tableColumnResidentialIndoorAir = 'c6'
    tableColumnCommercialIndoorAir = 'c9'
    ia_residential = dbLookUp(tableColumnResidentialIndoorAir, tableNameIndoorAir, contaminantNameInput)
    ia_commercial = dbLookUp(tableColumnCommercialIndoorAir, tableNameIndoorAir, contaminantNameInput)
    result.append(ia_residential)
    result.append(ia_commercial)

    ia_final = ''
    if landUse == 'unrestricted':
        ia_final = ia_residential
    else:
        ia_final = ia_commercial
    result.append(ia_final)

    ############
    # Soil Gas #
    ############
    tableNameSoilGas = 'TableC2'
    tableColumnResidentialSoilGas = 'c4'
    tableColumnCommercialSoilGas = 'c7'
    sg_residential = dbLookUp(tableColumnResidentialSoilGas, tableNameSoilGas, contaminantNameInput)
    sg_commercial = dbLookUp(tableColumnCommercialSoilGas, tableNameSoilGas, contaminantNameInput)
    result.append(sg_residential)
    result.append(sg_commercial)

    sg_final = ''
    if landUse == 'unrestricted':
        sg_final = sg_residential
    else:
        sg_final = sg_commercial
    result.append(sg_final)

    return result
