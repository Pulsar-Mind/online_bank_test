# Generated by Django 2.0 on 2018-12-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181231_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transactionmodel',
            name='amount',
            field=models.FloatField(),
        ),
    ]
