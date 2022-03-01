# Generated by Django 4.0.2 on 2022-02-27 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testRoot', '0038_goodcheck'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokyoCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('eat', 'ご飯'), ('cafe', 'カフェ'), ('play', '観光')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('ido', models.FloatField(null=True)),
                ('keido', models.FloatField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('good', models.IntegerField(default=0, null=True)),
                ('comment', models.CharField(max_length=500, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]