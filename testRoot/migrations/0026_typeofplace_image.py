# Generated by Django 4.0.2 on 2022-02-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testRoot', '0025_typeofplace_good'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofplace',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]