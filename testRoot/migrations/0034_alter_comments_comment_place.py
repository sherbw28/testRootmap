# Generated by Django 4.0.2 on 2022-02-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testRoot', '0033_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_place',
            field=models.CharField(max_length=255),
        ),
    ]
