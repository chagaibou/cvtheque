from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser with additional required fields'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = input("Email: ")
        password = input("Password: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        date_de_naissance = input("Date de Naissance (YYYY-MM-DD): ")
        genre = input("Genre (HOMME/FEMME): ")
        situation_matrimoniale = input("Situation Matrimoniale (celibataire/marie/veuf): ")
        nationalite = input("Nationalité (Malien/Autres): ")
        residence_legale = input("Résidence Légale: ")
        disponibilite = input("Disponibilité (disponible/non_disponible): ")
        telephone = input("Téléphone: ")
        region = input("Région: ")
        cercle = input("cercle: ")
        commune  = input("commune: ")

        User.objects.create_superuser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_de_naissance=date_de_naissance,
            genre=genre,
            situation_matrimoniale=situation_matrimoniale,
            nationalite=nationalite,
            residence_legale=residence_legale,
            disponibilite=disponibilite,
            telephone=telephone,
            region=region,
            cercle=cercle,
            commune=commune,
        )

        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
