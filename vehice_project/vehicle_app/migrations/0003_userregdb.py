# Generated by Django 3.2.10 on 2023-08-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0002_auto_20230812_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=15, null=True)),
                ('Password', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]