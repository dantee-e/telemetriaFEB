from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Dados
import json

@csrf_exempt
def receber_dados(request):
    if request.method == 'POST':
        dados_recebidos = json.loads(request.body)
        
        velocidade = dados_recebidos['velocidade']
        temperatura_motor = dados_recebidos['temperatura_motor']
        rpm = dados_recebidos['rpm']
        pressao_oleo = dados_recebidos['pressao_oleo']
        tensao_bateria = dados_recebidos['tensao_bateria']
        
        Dados.objects.create(
            velocidade=velocidade,
            temperatura_motor=temperatura_motor,
            rpm=rpm,
            pressao_oleo=pressao_oleo,
            tensao_bateria=tensao_bateria
        )
        
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)