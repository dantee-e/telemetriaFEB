# Generated by Django 5.0.4 on 2024-06-10 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_dados_mhps1_alter_dados_mhps2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='pot4',
            field=models.FloatField(null=True),
        ),
    ]
