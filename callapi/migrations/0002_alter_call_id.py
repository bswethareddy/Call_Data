# Generated by Django 4.2.4 on 2023-08-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
