# Generated by Django 2.2.3 on 2019-07-12 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20190712_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateField(),
        ),
    ]
