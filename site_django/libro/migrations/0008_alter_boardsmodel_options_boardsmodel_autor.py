# Generated by Django 4.2.16 on 2024-10-04 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libro", "0007_alter_boardsmodel_creado"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="boardsmodel",
            options={
                "permissions": (
                    ("es_miembro_1", "Es miembro con prioridad 1"),
                    ("development", "Permiso como Desarrollador"),
                    ("scrum_master", "Permiso como Scrum Master"),
                    ("product_owner", "Permiso como Product Owner"),
                ),
                "verbose_name": "libro",
                "verbose_name_plural": "libros",
            },
        ),
        migrations.AddField(
            model_name="boardsmodel",
            name="autor",
            field=models.CharField(default="Anonimo", max_length=200),
        ),
    ]
