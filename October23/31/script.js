const flashlight = document.getElementById('flashlight');
const toggleButton = document.getElementById('toggleButton');

let isOn = false;

toggleButton.addEventListener('click', () => {
    if (isOn) {
        flashlight.style.backgroundColor = '#fff';
    } else {
        flashlight.style.backgroundColor = '#000';
    }
    isOn = !isOn;
});

