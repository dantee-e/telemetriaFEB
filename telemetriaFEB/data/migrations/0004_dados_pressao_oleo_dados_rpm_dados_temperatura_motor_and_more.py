# Generated by Django 5.0.4 on 2024-04-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_remove_dados_pressao_oleo_remove_dados_rpm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='pressao_oleo',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='dados',
            name='rpm',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='dados',
            name='temperatura_motor',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='dados',
            name='tensao_bateria',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='dados',
            name='velocidade',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MHPS1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MHPS2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MLX1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MLX2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MLX3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='MLX4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_acele_X',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_acele_Y',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_acele_Z',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_X',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_Y',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu1_gyro_Z',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_acele_X',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_acele_Y',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_acele_Z',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_X',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_Y',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='mpu2_gyro_Z',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dados',
            name='pot3',
            field=models.IntegerField(null=True),
        ),
    ]