# Generated by Django 4.1.7 on 2023-03-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eclosion', '0002_alter_index_description1_alter_index_description2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cathegorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
