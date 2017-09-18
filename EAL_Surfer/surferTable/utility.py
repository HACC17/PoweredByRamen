import sqlite3 as db
import math
from django.apps import apps
import tempfile
import os
import pdfkit
from PyPDF2 import PdfFileMerger

# utility vars
dbName = 'EAL_SURFER_TABLES_DB.sqlite3'
appName = 'surferTable'
configTableName = 'allchemicals'
# use in view file
contaminantTypeCas = 'CAS'
contaminantTypeChemical = 'Chemical'
# template file names
chemicalSummaryTemplate = 'chemical_summary_template.html'
surferReportTemplate = 'surfer_report_template.html'
# list of strings to replace in template
chemicalSummaryTemplateList = ['chemical_input', 
            'cancer_slope', 'cancer_inha', 'refer_dose_oral', 'refer_dose_inha', 'gastr_intest', 'skin_absorb', 'target_excess', 'tecru_table', 'target_hazard', 'thqu_table',
            'fresh_chronic', 'marine_chronic', 'estuary_chronic', 'fresh_acute', 'marine_acute', 'estruary_acute', 'bio_goal',
            'molecular_weight', 'ps_v', 'ps_s', 'organic_carbon', 'diff_in_air', 'diff_in_water', 'solu_water', 'hlc_atm', 'hlc_unit',
            'health_carc', 'health_muta', 'health_alim', 'health_card', 'health_deve', 'health_endo', 'health_eye', 'health_hema', 
            'health_immu', 'health_kidn', 'health_nerv', 'health_repr', 'health_resp', 'health_skin', 'health_other']
surferReportTemplateList = ['site_name', 'site_address1', 'site_address2', 'site_address3', 'site_id', 'date_of_search', 'land_use', 'ground_water_utility', 'distance_to_nearest', 'chemical_input', 'soil_site',
                            'gw_site', 'sv_site', 'direct_exposure', 'dehazard', 'detable', 'vapor_emission', 'vehazard', 'vetable', 'terrestrial_ecotoxicity', 'tehazard', 'tetable',
                            'gros_contamination', 'gchazard', 'gctable', 'leach_threat', 'lthazard', 'lttable', 'background_tier1', 'bthazard', 'final_soil_tier1',
                            'final_soil_basis', 'drink_water', 'dwhazard', 'dwtable', 'v_emission_two', 've2hazard', 've2table', 'aquatic_ecotoxicity', 'aehazard', 'aetable',
                            'gross_contamination', 'gc2hazard', 'gc2table', 'final_ground_tier1', 'final_ground_basis', 'shallow_soil', 'shhazard', 'shtable', 'indoor-air', 'iahazard', 'iatable']
# wkhtmltopdf parameters to format PDF's on Windows machines
windowsPDFKitOptions = {}
   # 'quiet': '',
   # 'page-size': 'B7',
   # 'margin-top': '0.35in',
   # 'margin-right': '0.25in',
   # 'margin-bottom': '0.25in',
   # 'margin-left': '0.30in',
   # 'disable-smart-shrinking': ''}
# wkhtmltopdf parameters to format PDF's on *NIX machines
nixPDFKitOptions = {
    'quiet': '',
    'page-size': 'B4',
    'margin-top': '0.45in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '1.00in',
    'disable-smart-shrinking': ''}


# Return table name based on permutation of groundwater utility and distance to nearest surface waster body inputs
def soilTier1EALTablesLookUp(groundWaterUtilityInput, distanceToNearestInput):
    tempString = ''
    if groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'Table A-1'
    elif groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'lessthan':
        tempString = 'Table A-2'
    elif groundWaterUtilityInput == 'nondrinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'Table B-1'
    else:
        tempString = 'Table B-2'
    return tempString


# Return table name based on permutation of groundwater utility and distance to nearest surface waster body inputs
def finalGroundWaterActionLevelsLookUp(groundWaterUtilityInput, distanceToNearestInput):
    tempString = ''
    if groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'lessthan':
        tempString = 'Table D-1a'
    elif groundWaterUtilityInput == 'drinking' and distanceToNearestInput == 'greaterthan':
        tempString = 'Table D-1b'
    elif groundWaterUtilityInput == 'nondrinking' and distanceToNearestInput == 'lessthan':
        tempString = 'Table D-1c'
    else:
        tempString = 'Table D-1d'
    return tempString


# Helper function to merge a list of PDF files into one
def mergePDFFiles(pdflist):
    filename = 'result.pdf'
    oFile = 'static/'+filename
    merger = PdfFileMerger()

    for pdf in pdflist:
        merger.append(open(pdf, 'rb'))
        os.remove(pdf)

    with open(oFile, 'wb') as fout:
        merger.write(fout)

    return filename

# Scrub and convert user input for selected site values
def selectedSiteScenarioConvert(contaminantName, landUse, groundWaterUtility, distanceToNearest):
    contaminantNameConvert = contaminantName.encode('utf-8')
    landUseConvert = 'Comm/Indst Only'
    groundWaterUtilityConvert = 'Nondrinking Water Resource'
    distanceToNearestConvert = '> 150m'
    if landUse == 'unrestricted':
        landUseConvert = 'Unrestricted'
    if groundWaterUtility == 'drinking':
        groundWaterUtilityConvert = 'Drinking Water Resource'
    if distanceToNearest == 'lessthan':
        distanceToNearestConvert = '< 150m'
        
    return [contaminantNameConvert, landUseConvert, groundWaterUtilityConvert, distanceToNearestConvert]
    
# Helper function convert each element in a list into UTF-8 format                                                          
def convertDataToUTF8Format(inputList):
    return [element.encode('utf-8') for element in inputList]   
    
    
# Helper function replace '' with '-' to format better
def replaceSpaceWithDash(inputList):
    return [element or '-' for element in inputList]    

# Helper function convert html format to PDF format           
def convertHtmlToPDF(fileName):
    iFile = 'static/'+fileName+'.html'
    oFile = 'static/'+fileName+'.pdf'
    # Windows and *nix machines behave differently
    if os.name != 'nt':
        # package would not install correctly, installed manually and set explicit path
        config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
        pdfkit.from_file(iFile, oFile, configuration = config, options = windowsPDFKitOptions)
    else:
        pdfkit.from_file(iFile, oFile, options = nixPDFKitOptions)

    # clean up input file
    os.remove(iFile)
    return oFile

        
# Helper function replace a list of string variables with a string of values 
# from template file and write it to a new file     
def replace_template(newFileName, templateFile, iteration, findList, replaceList):
    newfile = 'static/' + newFileName + str(iteration) +'.html'
    ifile = open('static/'+templateFile, 'rb')
    ofile = open(newfile, 'wb')

    s = ifile.read()
    for item, replacement in zip(findList, replaceList):
        s = s.replace(item, replacement)
    ofile.write(s)

    ifile.close()
    ofile.close()

    
# Helper function to look up mapping of CAS to chemical name
def convertCASNameToChemicalName(contaminantName):

    model = apps.get_model(appName, configTableName)
    chemicalName = model.objects.values_list('c3', flat=True).filter(c2__exact=contaminantName)
    return chemicalName[0]

    
# Helper function to look up db (translate of vlookup functionality)
def configLookUp(column, contaminantName):
    model = apps.get_model(appName, configTableName)
    # SELECT {column} FROM {configTableName} WHERE c1 = {contaminantName}
    result = model.objects.values_list(column, flat=True).filter(c3__exact=contaminantName)
    result = result[0]
    if RepresentsFloat(result):
        return to_precision(float(result), 2)
    return result   
    
    
# Helper function to look up db (translate of vlookup functionality)
def dbLookUp(column, table_name, contaminantName):

    model = apps.get_model(appName, table_name)
    # SELECT {column} FROM {table_name} WHERE c1 = {contaminantName}
    result = model.objects.values_list(column, flat=True).filter(c1__exact=contaminantName)
    result = result[0] # return as list of one
    if RepresentsFloat(result):
        return to_precision(float(result), 2)
    return result


# Helper function to look up db (translate of vlookup functionality)
def dbLookUpWithChemicalColumnSpecified(column, table_name, contaminantName_column, contaminantName):

    columnToFilter = contaminantName_column+'__exact'
    model = apps.get_model(appName, table_name)
    # SELECT {column} FROM {table_name} WHERE {contaminantName_colun} = {contaminantName}
    # using parameter '**{ columnToFilter: contaminantName } to dynamically filter out results
    result = model.objects.values_list(column, flat=True).filter(**{ columnToFilter: contaminantName })
    result = result[0] # return as list of one
    if RepresentsFloat(result):
        return to_precision(float(result), 2)
    return result

    
# Helper function to check if string is represents a float/convertible to float
def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Helper function to return the minimum value of a list (in sig fig notations)
def findMinFromList(inputList):
    tempList = []
    for val in inputList:
        # check to make sure the val is float convertible
        if RepresentsFloat(val):
            tempList.append(float(val))
    return to_precision(min(tempList), 2)

# Helper function
def to_precision(x, p):
    """
    returns a string representation of x formatted with a precision of p

    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """
    x = float(x)

    if x == 0.:
        return "0." + "0" * (p - 1)

    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x / tens)

    if n < math.pow(10, p - 1):
        e = e - 1
        tens = math.pow(10, e - p + 1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens - x):
        n = n + 1

    if n >= math.pow(10, p):
        n = n / 10.
        e = e + 1

    m = "%.*g" % (p, n)

    if e < -2 or e >= p:
        out.append(m[0])
        if p > 1:
            out.append(".")
            out.extend(m[1:p])
        out.append('e')
        if e > 0:
            out.append("+")
        out.append(str(e))
    elif e == (p - 1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e + 1])
        if e + 1 < len(m):
            out.append(".")
            out.extend(m[e + 1:])
    else:
        out.append("0.")
        out.extend(["0"] * -(e + 1))
        out.append(m)

    return "".join(out)