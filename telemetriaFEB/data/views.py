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
from datetime import datetime, timedelta

@csrf_exempt
def receber_dados(request):
    if request.method == 'POST':
        dados_recebidos = json.loads(request.body)
        
        temperatura_motor = dados_recebidos['temperatura_motor']
        rpm = dados_recebidos['rpm']
        pressao_oleo = dados_recebidos['pressao_oleo']
        tensao_bateria = dados_recebidos['tensao_bateria']

        mpu1_gyro_Y = dados_recebidos['mpu1_gyro_Y']
        mpu1_gyro_X = dados_recebidos['mpu1_gyro_X']
        mpu1_gyro_Z = dados_recebidos['mpu1_gyro_Z']
        mpu2_gyro_X = dados_recebidos['mpu2_gyro_X']
        mpu2_gyro_Y = dados_recebidos['mpu2_gyro_Y']
        mpu2_gyro_Z = dados_recebidos['mpu2_gyro_Z']

        mpu1_acele_X = dados_recebidos['mpu1_acele_X']
        mpu1_acele_Y = dados_recebidos['mpu1_acele_Y']
        mpu1_acele_Z = dados_recebidos['mpu1_acele_Z']
        mpu2_acele_X = dados_recebidos['mpu2_acele_X']
        mpu2_acele_Y = dados_recebidos['mpu2_acele_Y']
        mpu2_acele_Z = dados_recebidos['mpu2_acele_Z']

        pot1 = dados_recebidos['pot1']
        pot2 = dados_recebidos['pot2']
        pot3 = dados_recebidos['pot3']
        pot4 = dados_recebidos['pot4']

        GPSX = dados_recebidos['GPSX']
        GPSY = dados_recebidos['GPSY']
        GPSSpeed = dados_recebidos['GPSSpeed']
        GPSAltitude = dados_recebidos['GPSAltitude']

        MHPS1 = dados_recebidos['MHPS1']
        MHPS2 = dados_recebidos['MHPS2']
        
        MLX1 = dados_recebidos['MLX1']
        MLX2 = dados_recebidos['MLX2']
        MLX3 = dados_recebidos['MLX3']
        MLX4 = dados_recebidos['MLX4']
        
            


        Dados.objects.create(
            temperatura_motor=temperatura_motor,
            rpm=rpm,
            pressao_oleo=pressao_oleo,
            tensao_bateria=tensao_bateria,
            mpu1_gyro_Y = mpu1_gyro_Y,
            mpu1_gyro_X = mpu1_gyro_X,
            mpu1_gyro_Z = mpu1_gyro_Z,
            mpu2_gyro_X = mpu2_gyro_X,
            mpu2_gyro_Y = mpu2_gyro_Y,
            mpu2_gyro_Z = mpu2_gyro_Z,
            mpu1_acele_X = mpu1_acele_X,
            mpu1_acele_Y = mpu1_acele_Y,
            mpu1_acele_Z = mpu1_acele_Z,
            mpu2_acele_X = mpu2_acele_X,
            mpu2_acele_Y = mpu2_acele_Y,
            mpu2_acele_Z = mpu2_acele_Z,
            pot1 = pot1,
            pot2 = pot2,
            pot3 = pot3,
            pot4 = pot4,
            GPSX = GPSX,
            GPSY = GPSY,
            GPSSpeed = GPSSpeed,
            GPSAltitude = GPSAltitude,
            MHPS1 = MHPS1,
            MHPS2 = MHPS2,
            MLX1 = MLX1,
            MLX2 = MLX2,
            MLX3 = MLX3,
            MLX4 = MLX4
        )
        
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

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