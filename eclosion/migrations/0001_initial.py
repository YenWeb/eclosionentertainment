# Generated by Django 4.1.7 on 2023-03-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre1', models.CharField(max_length=50)),
                ('Description1', models.TextField(max_length=100)),
                ('Image1', models.ImageField(upload_to='')),
                ('Titre2', models.CharField(max_length=50)),
                ('Description2', models.TextField(max_length=100)),
                ('Image2', models.ImageField(upload_to='')),
                ('Titre3', models.CharField(max_length=50)),
                ('Description3', models.TextField(max_length=100)),
                ('Image3', models.ImageField(upload_to='')),
            ],
        ),
    ]