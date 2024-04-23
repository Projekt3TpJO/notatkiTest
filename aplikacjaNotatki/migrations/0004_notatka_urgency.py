# Generated by Django 5.0.4 on 2024-04-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacjaNotatki', '0003_remove_notatka_urgency'),
    ]

    operations = [
        migrations.AddField(
            model_name='notatka',
            name='urgency',
            field=models.TextField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default='Low'),
        ),
    ]
