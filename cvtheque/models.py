from django.db import models
from authentification.models import User
from . import choices


class ExperiencesProfessionnelles(models.Model):

    #
    # RGPH = 'RGPH'
    # RGUE = 'RGUE'
    # EHCVM = 'EHCVM'
    # SMART = 'SMART'
    #
    #
    #
    # ENQUETES_CHOICES = (
    #     (RGPH,'RGPH'),
    #     (RGUE,'RGUE'),
    #     (EHCVM,'EHCVM'),
    #     (SMART,'SMART'),
    #     (AUTRES,'autres')
    #
    # )
    # EMOP = 'EMOP'
    # SMART = 'SMART'
    # SMIC = 'SMIC'
    # ROUGEOLE = 'ROUGEOLE'
    # EHCVM = 'EHCVM'
    # SMART_RAPIDE = 'SMART_RAPIDE'
    # OIM = 'OIM'
    # PALU = 'PALU'
    # NAFAMA = 'NAFAMA'
    #
    # RGPH = 'RGPH'
    # RGUE = 'RGUE'
    # PROJET_CHOICES = (
    #
    #         (EMOP, "emop"),
    #         (SMART, "smart"),
    #         (SMIC,'smic'),
    #         (ROUGEOLE,'rougeole'),
    #         (EHCVM,'ehcvm'),
    #         (SMART_RAPIDE,'smart_rapide'),
    #         (OIM,'oim'),
    #         (PALU,'palu'),
    #         (NAFAMA,'nafama'),
    #         (RGPH, "rgph"),
    #         (RGUE, "rgue"),
    #         (AUTRES,'autres')
    #     )




    candidat = models.ForeignKey(User, on_delete=models.CASCADE,related_name='experiences')  # Lien avec le modèle Candidat
    datedebut = models.DateField()
    datefin = models.DateField()
    organisation = models.CharField(max_length=255)
    type_experience = models.CharField(max_length=255,choices=choices.EXPERIENCES_CHOICES)
    poste = models.CharField(max_length=255)

    attestation = models.FileField(upload_to='media/')

    def __str__(self):
        return f'{self.candidat} au poste de {self.poste}'
class Formation(models.Model):

    BAC1='BAC+1'
    BAC2='BAC+2'
    BAC3='BAC+3'
    BAC4='BAC+4'
    BAC5='BAC+5'
    BAC6='BAC+6'
    BAC7='BAC+7'
    BAC8='BAC+8'
    DEGRE_CHOICES = (
        (BAC1,'BAC+1'),
        (BAC2,'BAC+2'),
        (BAC3,'BAC+3'),
        (BAC4,'BAC+4'),
        (BAC5,'BAC+5'),
        (BAC6,'BAC+6'),
        (BAC7,'BAC+7'),
        (BAC8,'BAC+8'),
    )
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    datedebut = models.DateField()
    datefin = models.DateField()
    universite_institution = models.CharField(max_length=100)
    niveau_degre = models.CharField(max_length=100,choices=choices.DEGRE_CHOICES)
    formation = models.CharField(max_length=100)
    diplome_attestation = models.FileField(upload_to='media/')

    def __str__(self):
        return self.formation

class Competence(models.Model):
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    competence = models.CharField(max_length=100)

    def __str__(self):
        return self.competence


class Langue(models.Model):
    DEBUTANT = 'Débutant'
    INTERMEDIAIRE = 'Intermediaire'
    AVANCE = 'avancé'

    NIVEAU_MAITRISE_CHOICES = (
        (DEBUTANT, 'Débutant'),
        (INTERMEDIAIRE, 'Intermediaire'),
        (AVANCE, 'avancé')
    )
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    langue_parlee = models.CharField(max_length=100)
    niveau_maitrise = models.CharField(max_length=50,choices=choices.NIVEAU_MAITRISE_CHOICES)

    def __str__(self):
        return self.langue_parlee





