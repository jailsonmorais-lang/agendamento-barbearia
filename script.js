/* ====== VARIÁVEIS GLOBAIS ====== */
// Login
const email = document.querySelector('input#email-login')                 /* Email de login */
const senha = document.querySelector('input#password-login')              /* Senha de login */
const retorno = document.querySelector('div#erro-login')                  /* div para mostrar erro no momento do login */
const erro = '0 10px 20px rgba(237, 58, 58, 0.9)'                  /* estilização da mensagem de erro */

// Cadastro
const regexNome = /^[A-Za-zÀ-ÿ\s]{3,70}$/                                 /* Receita para validar nomes */
const nomeCadastro = document.querySelector('input#nome-criar')           /* Nome para criar nova conta */
const emailCadastro = document.querySelector('input#email-cadastro')      /* Email para cadastro */
const senhaCadastro = document.querySelector('input#password-criar')      /* Senha para cadastro */
const senhaConfirmar = document.querySelector('input#password-confirmar') /* Confirmar a senha de cadastro */
const whatsapp = document.querySelector('input#whatsapp')                 /* Whatsapp para cadastro */
const erroCadastro = document.querySelector('div#erro-cadastro')          /* div para mostrar erro no momento do cadastro */

// Gerar código para criar nova senha
let codigoGerado = ''
const erroRecuperaSenha = document.querySelector('div#erro-recupera-senha')
let codigo = document.querySelector('input#codigo')
let whatsRecupera = document.querySelector('input#whatsapp-recuperar')
const whatsappsRegistrados = ['61999999999']
let novaSenha = document.querySelector('input#nova-senha')
let confirmarNovaSenha = document.querySelector('input#confirmar-nova-senha')
let erroCriarNovaSenha = document.querySelector('div#erro-criar-nova-senha')

/* BOTÃO PARA VIZUALIZAR SENHAS */

function configurarBotaoMostrarSenha(botaoSeletor, inputSeletor, imgSeletor) {
    const botao = document.querySelector(botaoSeletor)
    const input = document.querySelector(inputSeletor)
    const imagem = document.querySelector(imgSeletor)

    botao.addEventListener('click', () => {
        if (input.type === 'password') {
            input.type = 'text'
            imagem.src = 'icones/olho-aberto.svg'
        } else {
            input.type = 'password'
            imagem.src = 'icones/olho-fechado.svg'
        }
    })
}
configurarBotaoMostrarSenha('#btn-mostrar-senha-login', '#password-login', '#icone-olho-login')
configurarBotaoMostrarSenha('#btn-mostrar-senha-cadastro', '#password-criar', '#icone-olho-criar')
configurarBotaoMostrarSenha('#btn-mostrar-senha-confirmar', '#password-confirmar', '#icone-olho-confirmar')
configurarBotaoMostrarSenha('#btn-mostrar-nova-senha', '#nova-senha', '#icone-olho-nova-senha')
configurarBotaoMostrarSenha('#btn-mostrar-nova-senha-confirmar', '#confirmar-nova-senha', '#icone-olho-confirmar-nova-senha')

/* ====== VALIDAÇÃO DE LOGIN ====== */
// Responsáveis por validar dados do formulário de login
//Retornam mensagens de erro ou executam ação de sucesso

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

/* ====== EVENT LISTENERS - TELA LOGIN ====== */
// Escutam ações do usuário na tela de login
// Enter no input valida o formulário
// Clique no botão valida o formulário
// Clique em "Cadastre-se" navega para tela de cadastro

function validarEntrada(seletor) {
    document.querySelector(seletor).addEventListener('keydown', (evento) => {
        if (evento.key === 'Enter') {
            validarLogin()
        }
    })
}
validarEntrada('input#email-login')
validarEntrada('input#password-login')

document.querySelector('button#btn-login').addEventListener('click', (evento) => {
    evento.preventDefault()
    validarLogin()
})

document.querySelector('#tela-login a[href="#cadastre-se"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    mudarTela('tela-criar-conta')
    limparCadastro()
})

/* ====== VALIDAÇÃO DE CADASTRO ====== */
// Função para limpar campo de cadastro

function limparCadastro() {
    nomeCadastro.value = ''
    emailCadastro.value = ''
    senhaCadastro.value = ''
    senhaConfirmar.value = ''
    whatsapp.value = ''
    erroCadastro.innerHTML = ''
    erroCadastro.style.textShadow = ''
    erroCriarNovaSenha.innerHTML = ''
    erroCriarNovaSenha.style.textShadow = ''
    email.value = ''
    senha.value = ''
    retorno.innerHTML = ''
    retorno.style.textShadow = ''
    erroRecuperaSenha.innerHTML = ''
    erroRecuperaSenha.style.textShadow = ''
    codigo.value = ''
    whatsRecupera.value = ''
    novaSenha.value = ''
    confirmarNovaSenha.value = ''
    codigoGerado = ''
}

function validarCadastro() {
    if (nomeCadastro.value.length == 0) {
        erroCadastro.innerHTML = 'Campo "Nome" não pode ficar em branco.'
        erroCadastro.style.textShadow = erro
    } else if (/[0-9]/.test(nomeCadastro.value)) {
        erroCadastro.innerHTML = 'Nome não pode ter números.'
        erroCadastro.style.textShadow = erro
    } else if (!regexNome.test(nomeCadastro.value)) {
        erroCadastro.innerHTML = 'Nome tem caracteres invalidos.'
        erroCadastro.style.textShadow = erro
    } else if (nomeCadastro.value.length < 3 || nomeCadastro.value.length > 50) {
        erroCadastro.innerHTML = 'Nome muito curto ou muito longo'
        erroCadastro.style.textShadow = erro
    } else if (emailCadastro.value.length == 0) {
        erroCadastro.innerHTML = 'Campo "Email" não pode ficar em branco.'
        erroCadastro.style.textShadow = erro
    } else if (!emailCadastro.value.includes('@')) {
        erroCadastro.innerHTML = 'Email invalido.'
        erroCadastro.style.textShadow = erro
    } else if (senhaCadastro.value.length < 8) {
        erroCadastro.innerHTML = 'Senha deve conter no minimo 8 caracteres'
        erroCadastro.style.textShadow = erro
    } else if (!/[A-Z]/.test(senhaCadastro.value)) {
        erroCadastro.innerHTML = 'Senha deve conter pelo menos uma letra maiúscula'
        erroCadastro.style.textShadow = erro
    } else if (senhaConfirmar.value !== senhaCadastro.value) {
        erroCadastro.innerHTML = 'As senhas não coincidem!'
        erroCadastro.style.textShadow = erro
    } else if (whatsapp.value.length < 11) {
        erroCadastro.innerHTML = 'Número de WhatsApp invalido'
        erroCadastro.style.textShadow = erro
    } else if (!/^[0-9]{11}$/.test(whatsapp.value.replace(" ", ''))) {
        erroCadastro.innerHTML = 'Número de WhatsApp invalido'
        erroCadastro.style.textShadow = erro
    } else {
        mudarTela('tela-login')
    }
}

document.querySelector('button#btn-cadastrar').addEventListener('click', (evento) => {
    evento.preventDefault()
    validarCadastro()
})

/* ====== FUNÇÕES DE NAVEGAÇÃO ====== */
//Responsáveis por mddar entre telas
// Removem a classe "ativa" de todas as telas
// Adiciona "ativa" apenas na tela desejada

function mudarTela(idTela) {
    const todasTelas = document.querySelectorAll('.tela')
    todasTelas.forEach((tela) => {
        tela.classList.remove('ativa')
    })

    const telaSelecionada = document.getElementById(idTela)
    telaSelecionada.classList.add('ativa')
}

document.querySelector('#tela-criar-conta a[href="#login"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    mudarTela('tela-login')
})

document.querySelector('#tela-login a[href="#esqueci-a-senha"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    limparCadastro()
    mudarTela("tela-recuperar-senha")
})

document.querySelector('button#btn-verificar-codigo').addEventListener('click', (evento) => {
    evento.preventDefault()
    recuperarSenha()
})

document.querySelector('#tela-recuperar-senha a[href="#enviarcodigo"]').addEventListener('click', (evento) => {
    evento.preventDefault()
    enviarCodigo()

})

document.querySelector('button#redefinir-senha').addEventListener('click', (evento) => {
    evento.preventDefault()
    criarNovaSenha()
})

/* ====== RECUPERAÇÃO DE SENHA ====== */

function enviarCodigo() {
    if (whatsRecupera.value.length < 11) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp invalido'
        erroRecuperaSenha.style.textShadow = erro
    } else if (!/^[0-9]{11}$/.test(whatsRecupera.value.replace(" ", ''))) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp invalido'
        erroRecuperaSenha.style.textShadow = erro
    } else if (!whatsappsRegistrados.includes(whatsRecupera.value)) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp não encontrado!'
        erroRecuperaSenha.style.textShadow = erro
    } else {
        codigoGerado = String(Math.floor(Math.random() * 1000000)).padStart(6, '0')
        console.log('Codigo gerado:', codigoGerado)
        erroRecuperaSenha.innerHTML = 'Código enviado! Verifique seu WhatsApp'
        erroRecuperaSenha.style.textShadow = ''
    }
}

function recuperarSenha() {
    if (whatsRecupera.value.length < 11) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp invalido'
        erroRecuperaSenha.style.textShadow = erro
    } else if (!/^[0-9]{11}$/.test(whatsRecupera.value.replace(" ", ''))) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp invalido'
        erroRecuperaSenha.style.textShadow = erro
    } else if (!whatsappsRegistrados.includes(whatsRecupera.value)) {
        erroRecuperaSenha.innerHTML = 'Número de WhatsApp não encontrado!'
        erroRecuperaSenha.style.textShadow = erro
    } else if (codigo.value.length > 6 || codigo.value.length < 6) {
        erroRecuperaSenha.innerHTML = 'Código deve conter 6 digitos'
        erroRecuperaSenha.style.textShadow = erro
    } else if (codigo.value !== codigoGerado) {
        erroRecuperaSenha.innerHTML = 'Código INCORRETO'
        erroRecuperaSenha.style.textShadow = erro
    } else {
        mudarTela('tela-criar-nova-senha')
    }
}

function criarNovaSenha() {
    if (novaSenha.value.length < 8) {
        erroCriarNovaSenha.innerHTML = 'Senha deve conter no minimo 8 caracteres'
        erroCriarNovaSenha.style.textShadow = erro
    } else if (!/[A-Z]/.test(novaSenha.value)) {
        erroCriarNovaSenha.innerHTML = 'Senha deve conter uma letra maiúscula'
        erroCriarNovaSenha.style.textShadow = erro
    } else if (confirmarNovaSenha.value !== novaSenha.value) {
        erroCriarNovaSenha.innerHTML = 'As senhas não coincidem!'
        erroCriarNovaSenha.style.textShadow = erro
    } else {
        mudarTela('tela-login')
    }
}