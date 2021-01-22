# Generated by Django 3.1.5 on 2021-01-21 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210121_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datayear',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='documenttype',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='pagetype',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='pagetype',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='datayear',
            name='created',
        ),
        migrations.RemoveField(
            model_name='document',
            name='created',
        ),
        migrations.RemoveField(
            model_name='documenttype',
            name='created',
        ),
        migrations.RemoveField(
            model_name='editor',
            name='created',
        ),
        migrations.RemoveField(
            model_name='scope',
            name='created',
        ),
        migrations.RemoveField(
            model_name='source',
            name='created',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='created',
        ),
        migrations.AddField(
            model_name='datayear',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datayear',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='documenttype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documenttype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='editor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='editor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='pagetype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='scope',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scope',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='source',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
        migrations.AddField(
            model_name='topic',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date de création'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de modification'),
        ),
    ]
