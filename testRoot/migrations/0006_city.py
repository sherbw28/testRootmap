# Generated by Django 4.0.2 on 2022-02-10 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testRoot', '0005_typeofplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('pref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testRoot.prefecode')),
            ],
        ),
    ]
