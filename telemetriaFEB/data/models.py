from django.db import models

class Dados(models.Model):
    velocidade = models.FloatField()
    temperatura_motor = models.FloatField()
    rpm = models.IntegerField()
    pressao_oleo = models.FloatField()
    tensao_bateria = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)