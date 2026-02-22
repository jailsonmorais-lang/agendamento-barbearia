/* ====== VALIDAÇÃO DE LOGIN ====== */

const email = document.querySelector('input#email-login')
const senha = document.querySelector('input#password-login')
const nome = document.querySelector('input#nome')
const retorno = document.querySelector('div#retorno')
const erro = '0 10px 20px rgba(237, 58, 58, 0.9)'

function validarLogin() {
    if (email.value.length == 0) {
        alert('Campo de Email obrigatório')
    } else if (!email.value.includes('@')) {
        retorno.innerHTML = 'Email invalido!'
        retorno.style.textShadow = erro
    } else if (senha.value.length < 8) {
        retorno.innerHTML = 'A senha deve conter pelo menos 8 caracteres'
        retorno.style.textShadow = erro
    } else if (!/[A-Z]/.test(senha.value)) {
        retorno.innerHTML = 'Senha deve conter pelo menos uma letra maiúscula'
        retorno.style.textShadow = erro
    } else {
        mudarTela('tela-home')
    }
}
function validarEntrada(seletor) {
    document.querySelector(seletor).addEventListener('keydown', (evento) => {
        if (evento.key === 'Enter') {
            validarLogin()
        }
    })
}
validarEntrada('input#email-login')
validarEntrada('input#password-login')

document.querySelector('input#login').addEventListener('click', () => {
    validarLogin()
})

/* ====== CRIAR CONTA ====== */

function mudarTela(idTela) {
    const todasTelas = document.querySelectorAll('.tela')
    todasTelas.forEach((tela) => {
        tela.classList.remove('ativa')
    })

    const telaSelecionada = document.getElementById(idTela)
    telaSelecionada.classList.add('ativa')
}

document.querySelector('#tela-login a[href="#cadastre-se"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    mudarTela('tela-criar-conta')
})

document.querySelector('#tela-criar-conta a[href="#entrar"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    mudarTela('tela-login')
})

