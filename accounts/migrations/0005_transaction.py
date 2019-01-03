# Generated by Django 2.0 on 2018-12-30 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180815_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('rec_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiving_account', to='accounts.BankAccount')),
                ('sen_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sending_account', to='accounts.BankAccount')),
            ],
        ),
    ]