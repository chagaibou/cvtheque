from django.db import models
from authentification.models import User



class ExperiencesProfessionnelles(models.Model):
    ENQUETE = 'enquete'
    RECENSEMENT = 'recensement'
    SONDAGE = 'sondage'
    AUTRES = 'autres'

    EXPERIENCES_CHOICES = (
        (ENQUETE, 'enquete'),
        (RECENSEMENT,'recensement'),
        (SONDAGE,'sondage'),
        (AUTRES, 'autres')
    )
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




    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    datedebut = models.DateField()
    datefin = models.DateField()
    organisation = models.CharField(max_length=255)
    type_experience = models.CharField(max_length=255,choices=EXPERIENCES_CHOICES)
    poste = models.CharField(max_length=255)

    attestation = models.FileField(upload_to='media/')

    def __str__(self):
        return self.responsabilité
class Formation(models.Model):
    LICENCE = 'Licence'
    MASTER = 'Master'
    DOCTORAT = 'Doctorat',
    AUTRES = 'Autres'

    DEGRE_CHOICES = (
        (LICENCE,'Licence'),
        (MASTER,'Master'),
        (DOCTORAT,'Doctorat'),
        (AUTRES,'Autres'),
    )
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    datedebut = models.DateField()
    datefin = models.DateField()
    universite_institution = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    niveau_degre = models.CharField(max_length=100)
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
    niveau_maitrise = models.CharField(max_length=50,choices=NIVEAU_MAITRISE_CHOICES)

    def __str__(self):
        return self.langue_parlee





