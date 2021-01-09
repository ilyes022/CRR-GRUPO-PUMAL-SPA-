# Generated by Django 3.0.8 on 2020-11-29 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('wilaya', models.CharField(max_length=255)),
                ('localité', models.CharField(max_length=255)),
                ('nom_gérant', models.CharField(max_length=255)),
                ('adresse', models.CharField(max_length=255)),
                ('téléphone', models.CharField(max_length=255)),
                ('potentiel', models.CharField(max_length=255)),
                ('distributeur', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('région', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Pumal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('disponibilité', models.CharField(max_length=255)),
                ('quantité_disponible', models.IntegerField()),
                ('commande', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('disponibilité_concurrent', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=100)),
                ('client', models.ForeignKey(default='true', on_delete=django.db.models.deletion.CASCADE, to='pro.Clients')),
                ('créer_par', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('designation', models.ForeignKey(default='true', on_delete=django.db.models.deletion.CASCADE, to='pro.Produit')),
                ('région', models.ForeignKey(default='true', on_delete=django.db.models.deletion.CASCADE, to='pro.Location')),
                ('wilaya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pro.Wilaya')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='clients',
            name='région',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pro.Location'),
        ),
    ]