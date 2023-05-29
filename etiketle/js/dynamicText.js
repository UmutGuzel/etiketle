const messages = ["Veri seti etiketle", "Veri seti yükle"];
let index = 0;
const dynamicText = document.getElementById('dynamicText');

setInterval(() => {
    dynamicText.classList.add('fade');

    setTimeout(() => {
        dynamicText.innerText = messages[index];
        dynamicText.classList.remove('fade');
        index = (index + 1) % messages.length;
    }, 1000);
}, 4000);