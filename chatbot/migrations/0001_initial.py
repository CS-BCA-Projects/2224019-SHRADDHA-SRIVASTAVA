# Generated by Django 3.1.12 on 2025-03-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=255, unique=True)),
                ('precautions', models.TextField()),
                ('ayurvedic_medicine', models.TextField()),
                ('symptoms_effects', models.TextField()),
            ],
        ),
    ]
