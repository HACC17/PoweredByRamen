"""
Translation of compiler logic from Surfer Table Compiler Excel sheet 
Quick implementation to get project going
See file 'surfer_table_compiler_logic_breakdown.docx' in the resource directory (top level) for more info
TODO rework code to make it cleaner and model driven
"""

from utility import *

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
                     optional_inputSoilConcentration=0, optional_inputGroundWaterConcentration=0, optional_inputSoilGasConcentration=0,
                     optional_site_name=0, optional_site_address1=0, optional_site_address2=0, 
                     optional_site_address3=0, optional_site_id=0, optional_date_of_search=0):
    _landUse = landUse
    _groundWaterUtility = groundWaterUtility
    _chemicalSelected = contaminantName
    _distanceToNearestSurfaceWaterBody = distanceToNearest
    #_inputSoilConcentration = optional_inputSoilConcentration
    #_inputGroundWaterConcentration = optional_inputGroundWaterConcentration
    #_inputSoilGasConcentration = optional_inputSoilGasConcentration
    #_site_name = optional_site_name
    #_site_address1 = optional_site_address1
    #_site_address2 = optional_site_address2
    #_site_address3 = optional_site_address3
    #_site_id = optional_site_id
    #_date_of_search = optional_date_of_search
    
    soilActionLevelsList = soilActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    groundWaterActionLevelsList = groundWaterActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    indoorAirAndSoilGasActionLevelsList = indoorAirAndSoilGasActionLevels(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    
    [contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert] = selectedSiteScenarioConvert(contaminantName, landUse, groundWaterUtility, distanceToNearest)
    surfReportTemplateList = findSurfReportTemplateReplaceList(contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert,
                                                                soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList)
    # replace all '' with '-' to format better
    surfReportTemplateList = [element or '-' for element in surfReportTemplateList]
    
    chemicalSummaryTemplateList = findChemicalSummaryTemplateReplaceList(contaminantNameConvert, landUseConvert,
                                                                soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList)
	# make sure all values are encoded utf-8, due to the way data are stored in sqlite															
    chemicalSummaryTemplateList = [element.encode('utf-8') for element in chemicalSummaryTemplateList]
    return chemicalSummaryTemplateList

    # return column 71, 88, 99
    # map to index soilActionLevelsList[24], groundWaterActionLevelsList[10], indoorAirAndSoilGasActionLevelsList[5] 
    #[soil, groundWater, soilVapor] = [soilActionLevelsList[24], groundWaterActionLevelsList[10], indoorAirAndSoilGasActionLevelsList[5]]
    #return [soil, groundWater, soilVapor]

# Return 'X' based on potential health effect category
def checkTargetOrgansAndHealthEffect(chemName, tableName, column):
    tempString = "X"
    result = dbLookUp(column, tableName, chemName)
    if (result == '0' or result == 'NA' or result == '' or result == 'D' or result == 'E'):
        tempString = ''
    return tempString
    
# Return table name based on landUse inputs
def humanToxicityTableLookUp(landUse):
    tempString = 'TableI2'
    if landUse == 'unrestricted':
        tempString = 'TableI1'
    return tempString
    
# these variable names are map to the chemicalSummaryTemplateList found in utility file
def findChemicalSummaryTemplateReplaceList(contaminantName, landUse,
                                      soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList):
    # Human Toxicity Factors
    tableNameHumanToxicityFactors = 'TableH'
    tableNameHumanToxicityFactorsLookUp = humanToxicityTableLookUp(landUse) # Table based on landUse, use for display only
    tableColumnCancerSlope = 'c14'
    tableColumnCancerIhalation = 'c15'
    tableColumnReferenceDoseOral = 'c16'
    tableColumnReferenceDoseInhalation = 'c17'
    tableColumnReferenceDoseInhalationOther = 'c18'
    
    tableColumnGastroIntestinal = 'c12'
    tableColumnSkinAbsorption = 'c13'
    tableColumnSkinAbsorptionOther = 'c14'
    
    tableColumnTargetExcess = 'c4'
    tableColumnTargetExcessOther = 'c5'
    tableColumnTargetHazard = 'c7'

    tempCancerSlop = dbLookUp(tableColumnCancerSlope, tableNameHumanToxicityFactors, contaminantName)
    cancer_slope = ''
    if tempCancerSlop != '0' or tempCancerSlop != '0.0':
        cancer_slope = dbLookUp(tableColumnCancerIhalation, tableNameHumanToxicityFactors, contaminantName)
        
    tempCancerInha = dbLookUp(tableColumnCancerIhalation, tableNameHumanToxicityFactors, contaminantName)
    cancer_inha = ''
    if tempCancerInha != '0' or tempCancerInha != '0.0':
        cancer_inha = dbLookUp(tableColumnReferenceDoseOral, tableNameHumanToxicityFactors, contaminantName)

    tempReferDoseOral = dbLookUp(tableColumnReferenceDoseOral, tableNameHumanToxicityFactors, contaminantName)
    refer_dose_oral = ''
    if tempReferDoseOral != '0' or tempReferDoseOral != '0.0':
        refer_dose_oral = dbLookUp(tableColumnReferenceDoseInhalation, tableNameHumanToxicityFactors, contaminantName)

    tempReferDoseInha = dbLookUp(tableColumnReferenceDoseInhalation, tableNameHumanToxicityFactors, contaminantName)
    refer_dose_inha = ''
    if tempReferDoseInha != '0' or tempReferDoseInha != '0.0':
        refer_dose_inha = dbLookUp(tableColumnReferenceDoseInhalationOther, tableNameHumanToxicityFactors, contaminantName)

    gastr_intest = dbLookUp(tableColumnGastroIntestinal, tableNameHumanToxicityFactors, contaminantName)
    if gastr_intest != '0' or gastr_intest != '0.0':
        gastr_intest = dbLookUp(tableColumnSkinAbsorption, tableNameHumanToxicityFactors, contaminantName)
        
    skin_absorb = dbLookUp(tableColumnSkinAbsorption, tableNameHumanToxicityFactors, contaminantName)
    if skin_absorb != '0' or skin_absorb != '0.0':
        skin_absorb = dbLookUp(tableColumnSkinAbsorptionOther, tableNameHumanToxicityFactors, contaminantName)

    target_excess = ''
    if (tempCancerSlop != '0' or tempCancerSlop != '0.0') and (tempCancerInha != '0' or tempCancerInha != '0.0'):
        if landUse == 'unrestricted':
            target_excess = configLookUp(tableColumnTargetExcess, contaminantName)
        else:
            target_excess = configLookUp(tableColumnTargetExcessOther, contaminantName)

    target_hazard = ''
    if (tempReferDoseOral != '0' or tempReferDoseOral != '0.0') and (tempReferDoseInha != '0' or tempReferDoseInha != '0.0'):
            target_hazard = configLookUp(tableColumnTargetHazard, contaminantName)

    # Aquatic Habitat Protection Goals
    tableNameAquaticHabitatProtection = 'TableD4a'
    tableNameBioaccumulation = 'TableD4f'
    tableColumnFCGoal = 'c4'
    tableColumnMCGoal = 'c6'
    tableColumnECGoal= 'c2'
    tableColumnFAGoal = 'c5'
    tableColumnMAGoal = 'c7'
    tableColumnEAGoal = 'c3'
    tableColumnBGoal = 'c2'

    fresh_chronic = dbLookUp(tableColumnFCGoal, tableNameAquaticHabitatProtection, contaminantName)
    marine_chronic = dbLookUp(tableColumnMCGoal, tableNameAquaticHabitatProtection, contaminantName)
    estuary_chronic = dbLookUp(tableColumnECGoal, tableNameAquaticHabitatProtection, contaminantName)
    fresh_acute = dbLookUp(tableColumnFAGoal, tableNameAquaticHabitatProtection, contaminantName)
    marine_acute = dbLookUp(tableColumnMAGoal, tableNameAquaticHabitatProtection, contaminantName)
    estruary_acute = dbLookUp(tableColumnEAGoal, tableNameAquaticHabitatProtection, contaminantName)
    bio_goal = dbLookUp(tableColumnBGoal, tableNameBioaccumulation, contaminantName)

    # Fate & Transport Information
    tableNameFateAndTransportInfo = 'TableH'
    tableColumnMolecularWeight = 'c4'
    tableColumnPSV = 'c2'
    tableColumnPSS = 'c3'
    tableColumnOCPC = 'c6'
    tableColumnDAir = 'c7'
    tableColumnDWater = 'c8'
    tableColumnSWater = 'c9'
    tableColumnHLCAtm = 'c10'
    tableColumnHLCUnit = 'c11'
    
    molecular_weight = dbLookUp(tableColumnMolecularWeight, tableNameFateAndTransportInfo, contaminantName)

    tempPSV = dbLookUp(tableColumnPSV, tableNameFateAndTransportInfo, contaminantName)  
    ps_v = 'nonvolatile'
    if tempPSV == 'V':
        ps_v = 'volatile'

    tempPSS = dbLookUp(tableColumnPSS, tableNameFateAndTransportInfo, contaminantName)
    ps_s = 'gas'
    if tempPSV == 'S':
        ps_s = 'solid'
    if tempPSV == 'G':
        ps_s = 'gas'
        
    organic_carbon = dbLookUp(tableColumnOCPC, tableNameFateAndTransportInfo, contaminantName)
    diff_in_air = dbLookUp(tableColumnDAir, tableNameFateAndTransportInfo, contaminantName)
    diff_in_water = dbLookUp(tableColumnDWater, tableNameFateAndTransportInfo, contaminantName)
    solu_water = dbLookUp(tableColumnSWater, tableNameFateAndTransportInfo, contaminantName)
    hlc_atm = dbLookUp(tableColumnHLCAtm, tableNameFateAndTransportInfo, contaminantName)
    hlc_unit = dbLookUp(tableColumnHLCUnit, tableNameFateAndTransportInfo, contaminantName)
        
    # Potential Health Effects
    tableNamePotentialHealth = 'TableJ'
    tableColumnCarc = 'c2'
    tableColumnMuta = 'c3'
    tableColumnAlim = 'c4'
    tableColumnCard = 'c5'
    tableColumnDeve = 'c6'
    tableColumnEndo = 'c7'
    tableColumnEye = 'c8'
    tableColumnHema = 'c9'
    tableColumnImmu = 'c10'
    tableColumnKidn = 'c11'
    tableColumnNerv = 'c12'
    tableColumnRepr = 'c13'
    tableColumnResp = 'c14'
    tableColumnSkin = 'c15'
    tableColumnOther = 'c16'
    '''
    health_carc = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnCarc)
    health_muta = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnMuta)
    health_alim = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnAlim)
    health_card = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnCard)
    health_deve = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnDeve)
    health_endo = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnEndo)
    health_eye = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnEye)
    health_hema = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnHema)
    health_immu = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnImmu)
    health_kidn = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnKidn)
    health_nerv = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnNerv)
    health_repr = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnRepr)
    health_resp = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnResp)
    health_skin = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnSkin)
    health_other = checkTargetOrgansAndHealthEffect(contaminantName, tableNamePotentialHealth, tableColumnOther)
    '''
    
    health_carc = 'X'
    health_muta = 'X'
    health_alim = 'X'
    health_card = 'X'
    health_deve = 'X'
    health_endo = 'X'
    health_eye = 'X'
    health_hema = 'X'
    health_immu = 'X'
    health_kidn = 'X'
    health_nerv = 'X'
    health_repr = 'X'
    health_resp = 'X'
    health_skin = 'X'
    health_other = 'X'
    
    return [contaminantName, cancer_slope, cancer_inha, refer_dose_oral, refer_dose_inha, gastr_intest, skin_absorb, 
            target_excess, target_hazard, fresh_chronic, marine_chronic, estuary_chronic, fresh_acute, marine_acute, 
            estruary_acute, bio_goal, molecular_weight, ps_v, ps_s, organic_carbon, diff_in_air, diff_in_water, 
            solu_water, hlc_atm, hlc_unit, health_carc, health_muta, health_alim, health_card, health_deve, 
            health_endo, health_eye, health_hema, health_immu, health_kidn, health_nerv, health_repr, health_resp, 
            health_skin, health_other]

#TODO this decoder ring is not maintainable in the long run, create dictionary instead
# Needed values, excel line number to list index number
# soilActionLevelsList
# 46, 50, 56, 60, 68, 70, 71, 72
# 3, 6, 11, 14, 21, 23, 24, 25
# groundWaterActionLevelsList
# 75, 79, 83, 87, 88, 89
# 0, 3, 6, 9, 10, 11
# indoorAirAndSoilGasActionLevelsList
# 95, 99
# 2, 5
# these variable names are map to the surferReoportrtTemplateList found in utility file
def findSurfReportTemplateReplaceList(contaminantName, landUse, groundWaterUtility, distanceToNearest,
                                      soilActionLevelsList, groundWaterActionLevelsList, indoorAirAndSoilGasActionLevelsList):
    # Soil Environmental Hazards
    direct_exposure = soilActionLevelsList[3]
    dehazard = '-'
    detable = 'Table I-1'
    vapor_emission = soilActionLevelsList[6]
    vehazard = '-'
    vetable = 'Table C-1b'
    terrestrial_ecotoxicity = soilActionLevelsList[14]
    tehazard = '-'
    tetable = 'Table L'
    gros_contamination = soilActionLevelsList[21]
    gchazard = '-'
    gctable = 'Table F-2'
    leach_threat = soilActionLevelsList[11]
    lthazard = '-'
    lttable  = 'Table E-1'
    background_tier1 = soilActionLevelsList[23]
    bthazard = ''
    final_soil_tier1 = soilActionLevelsList[24]
    final_soil_basis = soilActionLevelsList[25]
    # Groundwater Environmental Hazards     
    drink_water = groundWaterActionLevelsList[0]
    dwhazard = '-'
    dwtable = 'Table D-1a'
    v_emission_two = groundWaterActionLevelsList[3]
    ve2hazard = '-'
    ve2table = 'Table C-1a'
    aquatic_ecotoxicity = groundWaterActionLevelsList[6]
    aehazard = '-'
    aetable = 'Table D-4a'
    gross_contamination = groundWaterActionLevelsList[9]
    gc2hazard = '-'
    gc2table = 'Table G-1'
    final_ground_tier1 = findMinFromList([drink_water, v_emission_two, aquatic_ecotoxicity, gross_contamination])
    final_ground_basis = groundWaterActionLevelsList[11]
    # Other Tier 1 EALs     
    shallow_soil = indoorAirAndSoilGasActionLevelsList[5]
    shhazard = '-'
    shtable = 'Table C-2'
    indoor_air = indoorAirAndSoilGasActionLevelsList[2]
    iahazard = '-'
    iatable = 'Table C-3'
    
    return [_site_name, _site_address1, _site_address2, _site_address3, _site_id, _date_of_search, landUse, groundWaterUtility, distanceToNearest, contaminantName,
            _inputSoilConcentration, _inputGroundWaterConcentration, _inputSoilGasConcentration, direct_exposure, dehazard, detable, vapor_emission, vehazard, vetable, 
            terrestrial_ecotoxicity, tehazard, tetable, gros_contamination, gchazard, gctable, leach_threat, lthazard, lttable, background_tier1, bthazard, final_soil_tier1, 
            final_soil_basis, drink_water, dwhazard, dwtable, v_emission_two, ve2hazard, ve2table, aquatic_ecotoxicity, aehazard, aetable, gross_contamination, gc2hazard, 
            gc2table, final_ground_tier1, final_ground_basis, shallow_soil, shhazard, shtable, indoor_air, iahazard, iatable]

            
# Scrub and convert user input for selected site values
def selectedSiteScenarioConvert(contaminantName, landUse, groundWaterUtility, distanceToNearest):
    contaminantNameConvert = contaminantName.encode('utf-8')
    landUseConvert = 'Commercial/Industrial Only'
    groundWaterUtilityConvert = 'Nondrinking Water Resource'
    distanceToNearestConvert = '> 150m'
    if landUse == 'unrestricted':
        landUseConvert = 'Unrestricted'
    if groundWaterUtility == 'drinking':
        groundWaterUtilityConvert = 'Drinking Water Resource'
    if distanceToNearest == 'lessthan':
        distanceToNearestConvert = '< 150m'
    return [contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert]
                
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

# soil action levels logic
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

# ground waster action levels logic
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

# indoor air and soil gas action levels logic
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
