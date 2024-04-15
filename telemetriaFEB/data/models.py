from django.db import models

class Dados(models.Model):
    temperatura_motor = models.FloatField(null=True)
    rpm = models.IntegerField(null=True)
    pressao_oleo = models.FloatField(null=True)
    tensao_bateria = models.FloatField(null=True)

    mpu1_gyro_X = models.IntegerField(null=True)
    mpu1_gyro_Y = models.IntegerField(null=True)
    mpu1_gyro_Z = models.IntegerField(null=True)

    mpu2_gyro_X = models.IntegerField(null=True)
    mpu2_gyro_Y = models.IntegerField(null=True)
    mpu2_gyro_Z = models.IntegerField(null=True)

    mpu1_acele_X = models.FloatField(null=True)
    mpu1_acele_Y = models.FloatField(null=True)
    mpu1_acele_Z = models.FloatField(null=True)

    mpu2_acele_X = models.FloatField(null=True)
    mpu2_acele_Y = models.FloatField(null=True)
    mpu2_acele_Z = models.FloatField(null=True)

    pot1 = models.IntegerField(null=True)
    pot2 = models.IntegerField(null=True)
    pot3 = models.IntegerField(null=True)

    GPSX = models.FloatField(null=True)
    GPSY = models.FloatField(null=True)
    GPSSpeed = models.FloatField(null=True)
    GPSAltitude = models.FloatField(null=True)

    MHPS1 = models.IntegerField(null=True)
    MHPS2 = models.IntegerField(null=True)

    MLX1 = models.FloatField(null=True)
    MLX2 = models.FloatField(null=True)
    MLX3 = models.FloatField(null=True)
    MLX4 = models.FloatField(null=True)

    data_hora = models.DateTimeField(auto_now_add=True)
