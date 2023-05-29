document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    var fileInput = document.getElementById('file');
    var file = fileInput.files[0];
    var textInput = document.getElementById('adress')
    var titleInput = document.getElementById('title')
    var formData = new FormData();
    formData.append('file', file);
    formData.append("text", textInput.value);
    formData.append("title", titleInput.value);

    fetch('http://127.0.0.1:8000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
});
