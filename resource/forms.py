from django import forms
from surferTable import listOfChemicalNames, listOfCASNames

class NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    LandUser = forms.ChoiceField(label='Land Use:', choices=(('base','Please Select'),('unrestricted','Unrestricted'),('commercial','Commercia/Industrial Only')))
    GroundWaterUtility = forms.ChoiceField(label='Ground Water Utility:', choices=(('base','Please Select'),('drinking','Drinking Water'),('nondrinking','Nondrinking Water')))
    DistanceToNearest = forms.ChoiceField(label='Distance To Nearest Surface Water Body:', choices=(('base','Please Select'),('lessthan','< 150m'),('greaterthan','> 150m')))