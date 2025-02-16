const inputColorFront = document.querySelector('.color-qr');
const inputColorBg = document.querySelector('.color-bg');
const pColorFront = document.querySelector('.qr-color');
const pColorBg = document.querySelector('.bg-color');

inputColorFront.addEventListener('input', () => {
    pColorFront.textContent = inputColorFront.value;
    inputColorFront.style.backgroundColor = inputColorFront.value;
});

inputColorBg.addEventListener('input', () => {
    pColorBg.textContent = inputColorBg.value;
    inputColorBg.style.backgroundColor = inputColorBg.value;
});
