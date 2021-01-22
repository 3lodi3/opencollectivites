# Generated by Django 3.1.5 on 2021-01-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('francesubdivisions', '0008_remove_epci_insee'),
        ('core', '0020_auto_20210122_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='communes',
            field=models.ManyToManyField(blank=True, to='francesubdivisions.Commune', verbose_name='commune'),
        ),
        migrations.AddField(
            model_name='source',
            name='departements',
            field=models.ManyToManyField(blank=True, to='francesubdivisions.Departement', verbose_name='département'),
        ),
        migrations.AddField(
            model_name='source',
            name='epcis',
            field=models.ManyToManyField(blank=True, to='francesubdivisions.Epci', verbose_name='EPCI'),
        ),
        migrations.AddField(
            model_name='source',
            name='regions',
            field=models.ManyToManyField(blank=True, to='francesubdivisions.Region', verbose_name='région'),
        ),
        migrations.AlterField(
            model_name='source',
            name='scope',
            field=models.ManyToManyField(blank=True, to='core.Scope', verbose_name='portée'),
        ),
        migrations.AlterField(
            model_name='source',
            name='topics',
            field=models.ManyToManyField(blank=True, to='core.Topic', verbose_name='sujet'),
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='source',
            name='years',
            field=models.ManyToManyField(blank=True, to='core.DataYear', verbose_name='année'),
        ),
    ]
