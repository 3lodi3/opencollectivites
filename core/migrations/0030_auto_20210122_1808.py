# Generated by Django 3.1.5 on 2021-01-22 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20210122_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['title'], 'verbose_name': 'source', 'verbose_name_plural': 'sources'},
        ),
    ]
