# Generated by Django 4.1.7 on 2023-03-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eclosion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='Description1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='index',
            name='Description2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='index',
            name='Description3',
            field=models.TextField(),
        ),
    ]
