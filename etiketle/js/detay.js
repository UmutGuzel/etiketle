var data_id;
window.onload = () => {
    let data = JSON.parse(localStorage.getItem('selectedCardData'));
    const title = document.getElementById('title');
    const x_data = document.getElementById('data');
    title.innerText = "Veri Seti: " + data.title;
    fetchItem(data._id)
        .then(item => {
            x_data.innerText = item.data.X;
            data_id = item.data._id;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    console.log(data);
};


document.getElementById('button').addEventListener('submit', function (event) {
    event.preventDefault();

    let label = document.querySelector('input[name="label"]').value;

    fetch('http://127.0.0.1:8000/dataupdate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "id": data_id,
            "Y": label
        })
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        window.location.href = 'detay.html';
    }).catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
});

async function fetchItem(_id) {
    const response = await fetch('http://127.0.0.1:8000/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({id: _id})
    });
    const items = await response.json();
    return items;
}
