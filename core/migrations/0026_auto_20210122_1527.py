# Generated by Django 3.1.5 on 2021-01-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20210122_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenttype',
            name='icon_url',
            field=models.URLField(blank=True, null=True, verbose_name='URL de l’icône'),
        ),
    ]
