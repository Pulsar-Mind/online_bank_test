# Generated by Django 2.0 on 2018-08-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200)),
                ('iban', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('failed_attempts', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-iban'],
            },
        ),
    ]
