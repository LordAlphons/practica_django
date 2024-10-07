# Generated by Django 4.2.16 on 2024-10-04 20:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("libro", "0005_alter_boardsmodel_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="boardsmodel",
            name="creado",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="boardsmodel",
            name="valor",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="boardsmodel",
            name="modificado",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
