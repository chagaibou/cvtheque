# your_app/management/commands/load_geographic_data.py

import csv
import os
from django.core.management.base import BaseCommand
from authentification.models import Region, Cercle, Commune

class Command(BaseCommand):
    help = 'Load geographic data from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Chemin vers les fichiers CSV dans le même répertoire
        base_dir = os.path.dirname(os.path.abspath(__file__))
        regions_csv = os.path.join(base_dir, 't_region.csv')
        cercles_csv = os.path.join(base_dir, 't_cercle.csv')
        communes_csv = os.path.join(base_dir, 't_commune.csv')

        # Supprimer les données existantes pour éviter les doublons
        Region.objects.all().delete()
        Cercle.objects.all().delete()
        Commune.objects.all().delete()

        # Insérer les régions
        with open(regions_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                region = Region.objects.create(nom=row['nom'])
                self.stdout.write(self.style.SUCCESS(f'Successfully added region "{region.nom}"'))

        # Insérer les cercles
        with open(cercles_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                region = Region.objects.get(id=row['region_id'])
                cercle = Cercle.objects.create(nom=row['nom'], region=region)
                self.stdout.write(self.style.SUCCESS(f'Successfully added cercle "{cercle.nom}" in region "{region.nom}"'))

        # Insérer les communes
        with open(communes_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cercle = Cercle.objects.get(id=row['cercle_id'])
                commune = Commune.objects.create(nom=row['nom'], cercle=cercle)
                self.stdout.write(self.style.SUCCESS(f'Successfully added commune "{commune.nom}" in cercle "{cercle.nom}"'))
