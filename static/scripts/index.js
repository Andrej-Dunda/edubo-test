let login_passw = document.getElementById("passw"),
    reg_passw = document.getElementById("reg_passw"),
    reg_passw_conf = document.getElementById("reg_passw_conf");

function handleLoginPasswordToggle() {
    if (login_passw.type === "password") {
        login_passw.type= "text"
        document.getElementById("login-pass-vis-toggle").src = "static/media/hidden.png"
    } else {
        login_passw.type = "password"
        document.getElementById("login-pass-vis-toggle").src = "static/media/view.png"
    }
}

function handleRegPasswordToggle() {
    if (reg_passw.type === "password") {
        reg_passw.type = "text"
        reg_passw_conf.type = "text"
        document.getElementById("reg-pass-vis-toggle").src = "static/media/hidden.png"
    } else {
        reg_passw.type = "password"
        reg_passw_conf.type = "password"
        document.getElementById("reg-pass-vis-toggle").src = "static/media/view.png"
    }
}

function checkPasswMatch(input) {
    if (input.value !== document.getElementById('reg_passw').value) {
        input.setCustomValidity('Hesla musí být stejná!');
    } else {
        input.setCustomValidity('');
    }
}








