# Generated by Django 4.2.5 on 2023-10-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='Checking',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
