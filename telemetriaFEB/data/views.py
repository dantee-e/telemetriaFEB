from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Dados
import json
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Dados
import os
from django.conf import settings
from django.templatetags.static import static

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

def mostrar_grafico(request):
    dados = Dados.objects.all()
    velocidade = [d.velocidade for d in dados]
    temperatura_motor = [d.temperatura_motor for d in dados]
    rpm = [d.rpm for d in dados]
    pressao_oleo = [d.pressao_oleo for d in dados]
    tensao_bateria = [d.tensao_bateria for d in dados]
    tempos = [d.data_hora for d in dados]
    
    variaveis = [
        [velocidade, 'velocidade'], 
        [temperatura_motor, 'temperatura_motor'], 
        [rpm, 'rpm'], 
        [pressao_oleo, 'pressao_oleo'], 
        [tensao_bateria, 'tensao_bateria']
    ]
    context = {}
    
    for variavel in variaveis:
        plt.plot(tempos, variavel[0])
        plt.xlabel('Data e Hora')
        plt.ylabel(variavel[1])
        plt.title('Variação de '+ variavel[1])
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        image_path = settings.STATICFILES_DIRS[0] + variavel[1] +'.png'
        imagem_src = 'image/'+variavel[1]+'.png'
        plt.savefig(image_path)
        plt.clf()
        context[variavel[1]] = imagem_src
        
    """plt.plot(tempos, velocidades)
    plt.xlabel('Data e Hora')
    plt.ylabel('Velocidade')
    plt.title('Variação da Velocidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    image_path = settings.STATICFILES_DIRS[0] + 'velocidade.png'
    velocidade_src = 'image/velocidade.png'

    plt.savefig(image_path)  # Salva o gráfico como uma imagem
    context = {'velocidade': velocidade_src}"""
    
    return render(request, 'grafico.html', context)

