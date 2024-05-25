document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const ra = document.getElementById('ra').value;
    const password = document.getElementById('password').value;

    // Registra os dados no console
    console.log('RA:', ra);
    console.log('Password:', password);

    // Espera 1 segundo antes de redirecionar para garantir que os dados sejam registrados no console
    setTimeout(function() {
        // Exemplo de redirecionamento para uma página de dashboard após login
        if (ra.startsWith('00')) {
            window.location.href = 'admin-dashboard.html';
        } else if (ra.startsWith('01')) {
            window.location.href = 'professor-dashboard.html';
        } else {
            window.location.href = 'student-dashboard.html';
        }
    }, 1000); // 1 segundo de atraso
});
