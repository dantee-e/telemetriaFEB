from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dados
import json
import matplotlib.pyplot as plt
from django.shortcuts import render
from .models import Dados
import os
from django.conf import settings
from django.templatetags.static import static
from datetime import datetime, timedelta
import json  

@csrf_exempt
def receber_dados(request):
    if request.method == 'POST':
        dados_recebidos = json.loads(request.body)
        
        print('Dados recebidos: ', dados_recebidos)
        
        try:
            dados = Dados.objects.create(
                temperatura_motor=float(dados_recebidos.get('temperatura_motor')),
                rpm=int(dados_recebidos.get('rpm')),
                pressao_oleo=float(dados_recebidos.get('pressao_oleo')),
                tensao_bateria=float(dados_recebidos.get('tensao_bateria')),
                mpu1_gyro_Y=float(dados_recebidos['mpu1_gyro'].get('Y')),
                mpu1_gyro_X=float(dados_recebidos['mpu1_gyro'].get('X')),
                mpu1_gyro_Z=float(dados_recebidos['mpu1_gyro'].get('Z')),
                mpu2_gyro_X=float(dados_recebidos['mpu2_gyro'].get('X')),
                mpu2_gyro_Y=float(dados_recebidos['mpu2_gyro'].get('Y')),
                mpu2_gyro_Z=float(dados_recebidos['mpu2_gyro'].get('Z')),
                mpu1_acele_X=float(dados_recebidos['mpu1_acele'].get('X')),
                mpu1_acele_Y=float(dados_recebidos['mpu1_acele'].get('Y')),
                mpu1_acele_Z=float(dados_recebidos['mpu1_acele'].get('Z')),
                mpu2_acele_X=float(dados_recebidos['mpu2_acele'].get('X')),
                mpu2_acele_Y=float(dados_recebidos['mpu2_acele'].get('Y')),
                mpu2_acele_Z=float(dados_recebidos['mpu2_acele'].get('Z')),
                pot1=float(dados_recebidos['potenciometros'].get('pot1')),
                pot2=float(dados_recebidos['potenciometros'].get('pot2')),
                pot3=float(dados_recebidos['potenciometros'].get('pot3')),
                pot4=float(dados_recebidos['potenciometros'].get('pot4')),
                GPSX=float(dados_recebidos['GPS'].get('X')),
                GPSY=float(dados_recebidos['GPS'].get('Y')),
                GPSSpeed=float(dados_recebidos['GPS'].get('Speed')),
                GPSAltitude=float(dados_recebidos['GPS'].get('Altitude')),
                MHPS1=float(dados_recebidos['MHPS'].get('MHPS1')),
                MHPS2=float(dados_recebidos['MHPS'].get('MHPS2')),
                MLX1=float(dados_recebidos['MLX'].get('MLX1')),
                MLX2=float(dados_recebidos['MLX'].get('MLX2')),
                MLX3=float(dados_recebidos['MLX'].get('MLX3')),
                MLX4=float(dados_recebidos['MLX'].get('MLX4'))
            )
            
            return JsonResponse({"status": "success"}, status=201)
        except Exception as e:
            # Log de erro detalhado
            print("Erro ao processar os dados recebidos:", e)
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Método não permitido"}, status=405)

def graficos_basicos(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]

    temperatura_motor = [d.temperatura_motor for d in dados]
    rpm = [d.rpm for d in dados]
    pressao_oleo = [d.pressao_oleo for d in dados]
    tensao_bateria = [d.tensao_bateria for d in dados]
    
    
    variaveis = [
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
        
    return render(request, 'tela_principal.html', {'context':context})

def graficos_MPU(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]

    mpu1_gyro_X = [d.mpu1_gyro_X for d in dados]
    mpu1_gyro_Y = [d.mpu1_gyro_Y for d in dados]
    mpu1_gyro_Z = [d.mpu1_gyro_Z for d in dados]
    mpu2_gyro_X = [d.mpu2_gyro_X for d in dados]
    mpu2_gyro_Y = [d.mpu2_gyro_Y for d in dados]
    mpu2_gyro_Z = [d.mpu2_gyro_Z for d in dados]

    mpu1_acele_X = [d.mpu1_acele_X for d in dados]
    mpu1_acele_Y = [d.mpu1_acele_Y for d in dados]
    mpu1_acele_Z = [d.mpu1_acele_Z for d in dados]
    mpu2_acele_X = [d.mpu2_acele_X for d in dados]
    mpu2_acele_Y = [d.mpu2_acele_Y for d in dados]
    mpu2_acele_Z = [d.mpu2_acele_Z for d in dados]

    variaveis =[
        [mpu1_gyro_X, 'mpu1_gyro_X'],
        [mpu1_gyro_Y, 'mpu1_gyro_Y'],
        [mpu1_gyro_Z, 'mpu1_gyro_Z'],
        [mpu2_gyro_X, 'mpu2_gyro_X'],
        [mpu2_gyro_Y, 'mpu2_gyro_Y'],
        [mpu2_gyro_Z, 'mpu2_gyro_Z'],
        [mpu1_acele_X, 'mpu1_acele_X'],
        [mpu1_acele_Y, 'mpu1_acele_Y'],
        [mpu1_acele_Z, 'mpu1_acele_Z'],
        [mpu2_acele_X, 'mpu2_acele_X'],
        [mpu2_acele_Y, 'mpu2_acele_Y'],
        [mpu2_acele_Z, 'mpu2_acele_Z']
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
    
    return render(request, 'grafico.html', {'context':context})

def graficos_analogicos(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]

    pot1 = [d.pot1 for d in dados]
    pot2 = [d.pot2 for d in dados]
    pot3 = [d.pot3 for d in dados]
    pot4 = [d.pot4 for d in dados]
    MHPS1 = [d.MHPS1 for d in dados]
    MHPS2 = [d.MHPS2 for d in dados]

    variaveis = [
        [pot1, 'pot1'],
        [pot2, 'pot2'],
        [pot3, 'pot3'],
        [pot4, 'pot4'],
        [MHPS1, 'MHPS1'],
        [MHPS2, 'MHPS2']
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
    
    return render(request, 'grafico.html', {'context':context})

def graficos_GPS(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]


    GPSX = [d.GPSX for d in dados]
    GPSY = [d.GPSY for d in dados]
    GPSSpeed = [d.GPSSpeed for d in dados]
    GPSAltitude = [d.GPSAltitude for d in dados]
    variaveis = [
        [GPSX, 'GPSX'],
        [GPSY, 'GPSY'],
        [GPSSpeed, 'GPSSpeed'],
        [GPSAltitude, 'GPSAltitude']]


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
    
    return render(request, 'grafico.html', {'context':context})

def graficos_MLX(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]


    MLX1 = [d.MLX1 for d in dados]
    MLX2 = [d.MLX2 for d in dados]
    MLX3 = [d.MLX3 for d in dados]
    MLX4 = [d.MLX4 for d in dados]
    variaveis = [
        [MLX1, 'MLX1'],
        [MLX2, 'MLX2'],
        [MLX3, 'MLX3'],
        [MLX4, 'MLX4']]


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
    
    return render(request, 'grafico.html', {'context':context})

def index(request):
    return render(request, 'index.html')

def velocimetro_RPM(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    latest = Dados.objects.latest('data_hora')
    
    return JsonResponse({'velocidade': latest.GPSSpeed, 'RPM': latest.rpm})
    


"""
def graficos_novos(request):
    tempo_anterior = datetime.now() - timedelta(minutes=5)
    dados = Dados.objects.filter(data_hora__gte=tempo_anterior)
    tempos = [d.data_hora for d in dados]

    var_nova1 = [d.var_nova1 for d in dados]
    var_nova2 = [d.var_nova2 for d in dados]
    var_nova3 = [d.var_nova3 for d in dados]

    variaveis =[
        [var_nova1, 'var_nova1'],
        [var_nova2, 'var_nova2'],
        [var_nova3, 'var_nova3']
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
    
    return render(request, 'grafico.html', {'context':context})
"""