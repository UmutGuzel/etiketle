function checkAuthentication() {
    var token = localStorage.getItem("etiketleJwtToken");

    if (!token) {
        window.location.href = 'giris.html';
        return;
    }

    var myHeaders = new Headers();
    myHeaders.append("Authorization", "Bearer " + token);

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/protected", requestOptions)
        .then(response => response.text())
        .then(result => {
            console.log(myHeaders)
            console.log(result);
        })
        .catch(error => {
            console.log('error', error);
            window.location.href = 'giris.html';
        });
}

checkAuthentication();