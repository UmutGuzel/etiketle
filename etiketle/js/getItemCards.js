function createCard(item) {
    let itemString = encodeURIComponent(JSON.stringify(item));
    return `
        <div class="col">
            <div class="card h-100" onclick="goToPageWithData('detay.html', '${itemString}')">
                <div style="background-color: ${getRandomColor()}; height: 200px;"></div>
                <div class="card-body">
                    <h5 class="card-title text-center">${item.title}</h5>
                    <p class="card-text text-center">${item.description}</p>
                </div>
            </div>
        </div>`;
}

async function fetchItems() {
    const response = await fetch('http://127.0.0.1:8000/datasets');
    const items = await response.json();
    return items;
}

async function displayItems() {
    const items = await fetchItems();
    console.log(items);
    const cards = items.map(item => createCard(item));
    document.getElementById('cards-container').innerHTML = cards;
}

function goToPageWithData(page, data) {
    let item = decodeURIComponent(data);
    localStorage.setItem('selectedCardData', item);
    window.location.href = page
}

function getRandomColor() {
    const red = Math.floor(Math.random() * 256);
    const green = Math.floor(Math.random() * 256);
    const blue = Math.floor(Math.random() * 256);
    return `rgb(${red}, ${green}, ${blue})`;
}

displayItems();