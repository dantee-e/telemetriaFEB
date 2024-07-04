// script.js

function atualizarPonteiros(json_dados){
    const ponteiro1 = document.querySelector('#ponteiro-velocimetro');
    const ponteiro2 = document.querySelector('#ponteiro-tacometro');

    // Ajuste dos graus para os ponteiros de velocidade e tacômetro
    let grauVelocidade = (json_dados.velocidade / 180) * 270 - 135; // Converte o valor para um ângulo entre -135 e 135
    ponteiro1.style.transform = `rotate(${grauVelocidade}deg)`;

    let grauRPM = (json_dados.RPM / 14000) * 215 - 135; // Converte o valor para um ângulo entre -135 e 135
    ponteiro2.style.transform = `rotate(${grauRPM}deg)`;

    console.log('velocidade = '+ json_dados.velocidade);
    console.log('RPM = '+ json_dados.RPM);
}


document.addEventListener('DOMContentLoaded', () => {
    const numerosVelocimetro = document.querySelector('.velocimetro .numeros');
    const numerosTacometro = document.querySelector('.tacometro .numeros');
    const numeroInicial = 0; // Valor inicial dos números
    const intervalo = 20; // Intervalo entre os números
    const numeroMaximo = 200; // Valor máximo dos números do velocímetro
    const rpmMaximo = 8000; // Valor máximo dos números do tacômetro
    const raioMostrador = 130; // Raio do mostrador

    // Função para converter graus em radianos
    function degToRad(deg) {
        return deg * Math.PI / 180;
    }

    // Adiciona números ao mostrador de velocidade
    for (let i = 0; i <= 9; i++) {
        const numero = document.createElement('span');
        numero.classList.add('numero');
        const valor = numeroInicial + i * intervalo;
        const angulo = 135 + (i * 30); // Inicia em -135 graus e adiciona 30 graus para cada número
        const x = 150 + raioMostrador * Math.cos(degToRad(angulo));
        const y = 150 + raioMostrador * Math.sin(degToRad(angulo));
        numero.textContent = valor;
        numero.style.left = `${x}px`;
        numero.style.top = `${y}px`;
        numerosVelocimetro.appendChild(numero);
    }

    // Adiciona números ao mostrador de RPM
    for (let i = 0; i <= 7; i++) {
        const numero = document.createElement('span');
        numero.classList.add('numero');
        const valor = numeroInicial + i * intervalo * 100;
        const angulo = 135 + (i * 30); // Inicia em -135 graus e adiciona 30 graus para cada número
        const x = 150 + raioMostrador * Math.cos(degToRad(angulo));
        const y = 150 + raioMostrador * Math.sin(degToRad(angulo));
        numero.textContent = valor;
        numero.style.left = `${x}px`;
        numero.style.top = `${y}px`;
        numerosTacometro.appendChild(numero);
    }




/*
    let i=1;
    while (1){
        if(i>5){
            break;
        }
        i++;
        setTimeout(()=>{
            fetch('/velocidade-RPM/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
            },
            })
            .then(response => response.json())
            .then(response => atualizarPonteiros(response));
            i+=1;
        },100);

    };
*/
   atualizarPonteiros({velocidade: 180, RPM:14000})
});

