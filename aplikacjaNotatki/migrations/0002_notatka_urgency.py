# Generated by Django 5.0.4 on 2024-04-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacjaNotatki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notatka',
            name='urgency',
            field=models.IntegerField(choices=0, default=0),
        ),
    ]
