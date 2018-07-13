# Generated by Django 2.0.5 on 2018-07-13 09:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import garage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=15, verbose_name='Nom Client')),
                ('prenom_client', models.CharField(max_length=15, verbose_name='Prenom Client')),
                ('numero_afpa_client', models.CharField(max_length=10, verbose_name='Numéro carte AFPA Client')),
            ],
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_devis', models.DateField(verbose_name='Date du devis')),
                ('devis_signe_img', models.ImageField(blank=True, null=True, upload_to='img/devis', verbose_name='Scan du devis signé')),
                ('numero_devis', models.IntegerField(default=garage.models.Devis.NumeroDevis, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Devis',
            },
        ),
        migrations.CreateModel(
            name='DonneesPersonnelles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_client', models.EmailField(max_length=35, verbose_name='Email Client')),
                ('telephone_client', models.CharField(max_length=10, verbose_name='Téléphone Client')),
                ('carte_AFPA_img', models.ImageField(blank=True, null=True, upload_to='img/carte_AFPA_client', verbose_name='Carte AFPA')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_fournisseur', models.CharField(max_length=35, verbose_name='Nom Fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_saisie_intervention', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name="date d'intervention")),
                ('date_restitution_prevu', models.DateField(null=True, verbose_name='Date de restitution prévisionnelle')),
                ('diagnostic', models.TextField(max_length=300, null=True)),
                ('intervention_a_realiser', models.TextField(max_length=300, null=True, verbose_name='interventions prévus')),
                ('intervention_realisee', models.BooleanField(default=False, verbose_name='intervention réalisée')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_piece', models.CharField(max_length=20, verbose_name='référence pièce')),
                ('libelle_piece', models.CharField(max_length=50, verbose_name='libellé de la pièce')),
            ],
        ),
        migrations.CreateModel(
            name='Piece_Fournisseur_Devis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Statut', models.CharField(choices=[('VF', 'ValidationFormateur'), ('AF', 'AttenteFormateur'), ('RF', 'RefusFormateur'), ('AD', 'AttenteDevis'), ('VC', 'ValidationClient'), ('AC', 'AttenteClient'), ('RC', 'RefusClient')], default='AF', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TypeVehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_vehicule', models.CharField(choices=[('voiture', 'Voiture'), ('moto', 'Moto'), ('velo', 'Velo')], default='voiture', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entree_stage', models.DateField(blank=True, null=True)),
                ('date_sortie_stage', models.DateField(blank=True, null=True)),
                ('carte_afpa', models.CharField(max_length=10, verbose_name='Numéro carte AFPA')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_modele', models.CharField(max_length=50, verbose_name='libellé modèle')),
            ],
        ),
        migrations.CreateModel(
            name='Motorise',
            fields=[
                ('vehicule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garage.Vehicule')),
                ('libelle_marque', models.CharField(max_length=100, null=True, verbose_name='libellé marque')),
                ('vin', models.CharField(max_length=100, null=True)),
                ('immatriculation', models.CharField(max_length=15, null=True)),
                ('kilometrage', models.IntegerField(null=True)),
                ('date_mec', models.DateField(default=datetime.datetime.now, null=True, verbose_name='date de première m.e.c.')),
                ('carte_grise_img', models.ImageField(blank=True, null=True, upload_to='img/carte_grise', verbose_name='carte grise')),
                ('carte_assurance_img', models.ImageField(blank=True, null=True, upload_to='img/carte_assurance', verbose_name='carte assurance')),
            ],
            bases=('garage.vehicule',),
        ),
        migrations.CreateModel(
            name='Velo',
            fields=[
                ('vehicule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garage.Vehicule')),
            ],
            bases=('garage.vehicule',),
        ),
        migrations.AddField(
            model_name='vehicule',
            name='type_vehicule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.TypeVehicule'),
        ),
        migrations.AddField(
            model_name='client',
            name='donnees_personnelles_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.DonneesPersonnelles'),
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('motorise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garage.Motorise')),
            ],
            bases=('garage.motorise',),
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('motorise_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garage.Motorise')),
            ],
            bases=('garage.motorise',),
        ),
    ]