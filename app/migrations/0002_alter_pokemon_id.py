# Generated by Django 3.2.15 on 2022-08-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]