# Generated by Django 4.2.4 on 2024-02-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("e_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="gender",
            field=models.CharField(max_length=20),
        ),
    ]
