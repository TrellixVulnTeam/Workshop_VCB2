# Generated by Django 2.2.6 on 2020-05-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pancar', '0006_auto_20200526_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]