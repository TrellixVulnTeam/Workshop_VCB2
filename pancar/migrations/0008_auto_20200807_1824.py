# Generated by Django 3.1 on 2020-08-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0007_orderedcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
