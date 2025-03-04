from django.db import models
from authentification.models import User



class ExperiencesProfessionnelles(models.Model):
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec le modèle Candidat
    datedebut = models.DateField()
    datefin = models.DateField()
    organisation = models.CharField(max_length=255)
    responsabilité = models.CharField(max_length=255)
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





