# Generated by Django 5.1.6 on 2025-03-21 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Competence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("competence", models.CharField(max_length=100)),
                (
                    "candidat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExperiencesProfessionnelles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datedebut", models.DateField()),
                ("datefin", models.DateField()),
                ("organisation", models.CharField(max_length=255)),
                (
                    "type_experience",
                    models.CharField(
                        choices=[
                            ("enquete", "enquete"),
                            ("recensement", "recensement"),
                            ("sondage", "sondage"),
                            ("autres", "autres"),
                        ],
                        max_length=255,
                    ),
                ),
                ("poste", models.CharField(max_length=255)),
                ("attestation", models.FileField(upload_to="media/")),
                (
                    "candidat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Formation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datedebut", models.DateField()),
                ("datefin", models.DateField()),
                ("universite_institution", models.CharField(max_length=100)),
                ("formation", models.CharField(max_length=100)),
                (
                    "niveau_degre",
                    models.CharField(
                        choices=[
                            ("Bt", "Bt"),
                            ("Licence", "Licence"),
                            ("Master", "Master"),
                            ("Doctorat", "Doctorat"),
                            ("Autres", "Autres"),
                        ],
                        max_length=100,
                    ),
                ),
                ("diplome_attestation", models.FileField(upload_to="media/")),
                (
                    "candidat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Langue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("langue_parlee", models.CharField(max_length=100)),
                (
                    "niveau_maitrise",
                    models.CharField(
                        choices=[
                            ("Débutant", "Débutant"),
                            ("Intermediaire", "Intermediaire"),
                            ("avancé", "avancé"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "candidat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
