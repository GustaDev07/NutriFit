document.getElementById('dietaForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const peso = document.getElementById('peso').value;
    const altura = document.getElementById('altura').value;
    const genero = document.getElementById('genero').value;
    const objetivo = document.getElementById('objetivo').value;

    const response = await fetch('http://localhost:5000/plano_dieta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ peso, altura, genero, objetivo }),
    });

    const data = await response.json();
    const resultado = document.getElementById('resultado');
    resultado.style.display = 'block';
    resultado.innerHTML = data.dieta;
});
// script.js

document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');

    menuToggle.addEventListener('click', function () {
        nav.classList.toggle('active');
        menuToggle.classList.toggle('open');
    });
});
