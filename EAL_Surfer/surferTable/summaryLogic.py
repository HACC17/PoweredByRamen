'''
Logic to return a list of values to replace in the template files in html
format and then converted to PDF's
'''
from utility import *

# Return 'X' based on potential health effect category
def checkTargetOrgansAndHealthEffect(chemName, tableName, column):
    tempString = "X"
    result = dbLookUp(column, tableName, chemName)
    if (result == '0' or result == 'NA' or result == '' or result == 'D' or result == 'E'):
        tempString = ''
    return tempString
    
# Return table name based on land use input
def humanToxicityTableLookUp(landUse):
    print landUse
    tempString = 'Table I-2'
    if landUse == 'unrestricted':
        tempString = 'Table I-1'
    print tempString
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
    tableColumnHLCAtm = 'c11'
    tableColumnHLCUnit = 'c12'
    
    molecular_weight = dbLookUp(tableColumnMolecularWeight, tableNameFateAndTransportInfo, contaminantName)

    tempPSV = dbLookUp(tableColumnPSV, tableNameFateAndTransportInfo, contaminantName)  
    ps_v = 'nonvolatile'
    if tempPSV == 'V':
        ps_v = 'volatile'

    tempPSS = dbLookUp(tableColumnPSS, tableNameFateAndTransportInfo, contaminantName)
    ps_s = 'gas'
    if tempPSS == 'S':
        ps_s = 'solid'
    elif tempPSS == 'L':
        ps_s = 'liquid'
        
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

    result = [contaminantName, cancer_slope, cancer_inha, refer_dose_oral, refer_dose_inha, gastr_intest, skin_absorb, 
              target_excess, tableNameHumanToxicityFactorsLookUp, target_hazard, tableNameHumanToxicityFactorsLookUp,
              fresh_chronic, marine_chronic, estuary_chronic, fresh_acute, marine_acute,
              estruary_acute, bio_goal, molecular_weight, ps_v, ps_s, organic_carbon, diff_in_air, diff_in_water, 
              solu_water, hlc_atm, hlc_unit, health_carc, health_muta, health_alim, health_card, health_deve, health_endo, 
              health_eye, health_hema, health_immu, health_kidn, health_nerv, health_repr, health_resp, health_skin, health_other]
    
    # make sure all values are encoded utf-8, due to the way data are stored in sqlite                                                          
    result = convertDataToUTF8Format(result)
    
    return result

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
def findSurfReportTemplateReplaceList(site_name, site_address1, site_address2, site_address3, site_id, date_of_search,
                                      contaminantName, landUse, groundWaterUtility, distanceToNearest,
                                      inputSoilConcentration, inputGroundWaterConcentration, inputSoilGasConcentration,
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
    
    list1 = [site_name, site_address1, site_address2, site_address3, site_id, date_of_search]

    list2 = [landUse, groundWaterUtility, distanceToNearest, contaminantName,
             inputSoilConcentration, inputGroundWaterConcentration, inputSoilGasConcentration, direct_exposure, dehazard, detable, vapor_emission, vehazard, vetable, 
             terrestrial_ecotoxicity, tehazard, tetable, gros_contamination, gchazard, gctable, leach_threat, lthazard, lttable, background_tier1, bthazard, final_soil_tier1, 
             final_soil_basis, drink_water, dwhazard, dwtable, v_emission_two, ve2hazard, ve2table, aquatic_ecotoxicity, aehazard, aetable, gross_contamination, gc2hazard, 
             gc2table, final_ground_tier1, final_ground_basis, shallow_soil, shhazard, shtable, indoor_air, iahazard, iatable]
             
    # seperating into two list because we don't want to replace blank addresses with '-'
    result = list1 + replaceSpaceWithDash(list2)
    result = convertDataToUTF8Format(result)

    return result
