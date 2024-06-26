# Generated by Django 5.0.4 on 2024-06-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_remove_dados_velocidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='MHPS1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MHPS2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_X',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_Y',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_Z',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_X',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_Y',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_Z',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='rpm',
            field=models.FloatField(null=True),
        ),
    ]
