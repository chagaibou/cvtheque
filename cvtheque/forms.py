from django.forms import ModelForm,modelformset_factory,DateInput
from . import models
from django import forms



class ExperiencesProfessionellesForm(ModelForm):
    class Meta:
        model = models.ExperiencesProfessionnelles
        fields = ['datedebut','datefin','organisation','type_experience','poste','attestation']

        widgets = {
            'datedebut': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'datefin': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }



class FormationForm(ModelForm):
    edit_formation =  forms.BooleanField(widget=forms.HiddenInput,initial=True)
    class Meta:
        model = models.Formation
        fields = ['datedebut','datefin','universite_institution','niveau_degre','formation','diplome_attestation']

        widgets = {
            'datedebut': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'datefin': DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

class CompetenceForm(ModelForm):
    class Meta:
        model = models.Competence
        fields = ['competence']
class LangueForm(ModelForm):
    class Meta:
        model = models.Langue
        fields = ['langue_parlee','niveau_maitrise']


class DeleteFormation(forms.Form):
    delete_formation = forms.BooleanField(widget=forms.HiddenInput,initial=True)

ExperiencesProfessionellesFormSet = modelformset_factory(models.ExperiencesProfessionnelles, ExperiencesProfessionellesForm, extra=1)
FormationFormSet = modelformset_factory(models.Formation, FormationForm, extra=1)
CompetenceFormSet = modelformset_factory(models.Competence, CompetenceForm, extra=1)
LangueFormSet = modelformset_factory(models.Langue, LangueForm, extra=1)