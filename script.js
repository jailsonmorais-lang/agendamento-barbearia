const email = document.querySelector('input#email')
const senha = document.querySelector('input#password')
const retorno = document.querySelector('div#retorno')

function validarLogin() {
    if (email.value.length == 0 || !email.value.includes('@')) {
        retorno.innerHTML = 'Email inválido'
        retorno.style.textShadow += '0 10px 20px rgba(237, 58, 58, 0.9)'
    } else if (senha.value.length < 8) {
        retorno.innerHTML = 'A senha deve conter pelo menos 8 caracteres'
        retorno.style.textShadow = '0 10px 20px rgba(237, 58, 58, 0.9)'
    } else if (!/[A-Z]/.test(senha.value)) {
        retorno.innerHTML = 'Deve conter pelo menos uma letra maiúscula'
        retorno.style.textShadow += '0 10px 20px rgba(237, 58, 58, 0.9)'
    }
}

document.querySelector('input#login').addEventListener('click', () => {
    validarLogin()
})
document.querySelector('input#password').addEventListener('keydown', (evento) => {
    if (evento.key === 'Enter') {
        validarLogin()
    }
})








