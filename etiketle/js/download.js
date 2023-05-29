document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    let titleInput = document.getElementById('title')
    let formData = new FormData();
    formData.append("title", titleInput.value);

    fetch('http://127.0.0.1:8000/download', {
        method: 'POST',
        body: formData
    })
    .then(response => {
         if (response.ok) {
            const contentDisposition = response.headers.get('Content-Disposition');
            let filename = 'dataset_' + titleInput.value + '.csv';
            if (contentDisposition) {
                filename = contentDisposition.split('filename=')[1];
            }

            return response.blob().then(blob => {
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = filename;

                a.click();

                URL.revokeObjectURL(url);
            });
        } else {
            throw new Error('Failed to download file');
        }
    })
    .then(data => console.log(data))
    .catch(error => console.error(error));
});