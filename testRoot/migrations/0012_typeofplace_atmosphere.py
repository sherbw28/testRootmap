# Generated by Django 4.0.2 on 2022-02-13 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testRoot', '0011_atmosphere'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofplace',
            name='atmosphere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='testRoot.atmosphere'),
        ),
    ]
