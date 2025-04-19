ENQUETE = 'enquete'
RECENSEMENT = 'recensement'
SONDAGE = 'sondage'
AUTRES = 'autres'

EXPERIENCES_CHOICES = (
    (ENQUETE, 'enquete'),
    (RECENSEMENT, 'recensement'),
    (SONDAGE, 'sondage'),
    (AUTRES, 'autres')
)


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


DEBUTANT = 'Débutant'
INTERMEDIAIRE = 'Intermediaire'
AVANCE = 'avancé'

NIVEAU_MAITRISE_CHOICES = (
        (DEBUTANT, 'Débutant'),
        (INTERMEDIAIRE, 'Intermediaire'),
        (AVANCE, 'avancé')
)