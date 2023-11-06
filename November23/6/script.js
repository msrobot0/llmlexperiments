const flame = document.querySelector('.flame');
const toggleButton = document.getElementById('toggleButton');

let isFlameOn = true;

toggleButton.addEventListener('click', () => {
    if (isFlameOn) {
        flame.style.animationPlayState = 'paused';
        isFlameOn = false;
    } else {
        flame.style.animationPlayState = 'running';
        isFlameOn = true;
    }
});

