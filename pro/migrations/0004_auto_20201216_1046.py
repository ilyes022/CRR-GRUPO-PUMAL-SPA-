# Generated by Django 3.0.8 on 2020-12-16 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0003_auto_20201129_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pumal',
            name='commande',
            field=models.IntegerField(default=0),
        ),
    ]