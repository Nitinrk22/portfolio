# Generated by Django 3.0.5 on 2020-05-10 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200510_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]
