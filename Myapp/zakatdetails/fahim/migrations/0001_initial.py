# Generated by Django 5.0.7 on 2024-07-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Madrasadetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madrasaname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                

            ],
        ),
    ]
