document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    let tokenKey = "etiketleJwtToken";
    let username = document.querySelector('input[name="username"]').value;
    let password = document.querySelector('input[name="password"]').value;

    let userLoginData = {
        username: username,
        password: password
    };

    fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userLoginData)
    }).then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(response => {
        console.log(response)
        localStorage.setItem(tokenKey, response.data.token);
        window.location.href = 'list.html';
    }).catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
});
