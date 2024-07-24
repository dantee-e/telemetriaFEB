function atualizarImagens(){
    fetch(window.location.href+'1/', {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(json => {
        for (var item in json){
            var img = document.getElementById(item)
            img.src = '/static/'+json[item]+ '?'+new Date().getTime();
        }
        console.log('imagens atualizadas acho')
    })
}
document.addEventListener('DOMContentLoaded', () => {
    setInterval(atualizarImagens, 500);
}) 