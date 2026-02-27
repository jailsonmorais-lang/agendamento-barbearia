/* ===== VARIÁVEIS (CSS CUSTOM PROPERTIES) ===== */
:root {
    --roxo-principal: #7C3AED;
    /* mais variáveis */
}

/* ===== RESET/NORMALIZAÇÕES ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* ===== WEBKIT (COMPATIBILIDADE) ===== */
* {
    -webkit-tap-highlight-color: transparent;
    -webkit-font-smoothing: antialiased;
}

button {
    -webkit-appearance: none;
}

/* ===== ESTILOS GERAIS (BODY, HTML, GLOBALS) ===== */
body {
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    color: var(--texto-principal);
    background: var(--fundo-principal);
}

html {
    scroll-behavior: smooth;
}

/* ===== ANIMAÇÕES ===== */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

/* ===== COMPONENTES (BUTTONS, INPUTS, ETC) ===== */
button {
    /* estilos */
}

input {
    /* estilos */
}

a {
    /* estilos */
}

/* ===== LAYOUT/CONTAINERS ===== */
.container {
    /* estilos */
}

.secao {
    /* estilos */
}

/* ===== TIPOGRAFIA ===== */
.titulo-principal {
    /* estilos */
}

.titulo-secundario {
    /* estilos */
}

.destaque {
    /* estilos */
}

/* ===== SEÇÃO 1: [NOME DA SEÇÃO] ===== */
#qualificacoes {
    /* estilos */
}

.experiencia {
    /* estilos */
}

/* ===== SEÇÃO 2: [NOME DA SEÇÃO] ===== */
#btns-navegacao {
    /* estilos */
}

#btn-ver-servicos {
    /* estilos */
}

/* ===== MEDIA QUERIES (RESPONSIVO) ===== */
@media (hover: hover) {
    button:hover {
        /* estilos */
    }
    
    a:hover {
        /* estilos */
    }
    
    .card:hover {
        /* estilos */
    }
}

@media (max-width: 768px) {
    .container {
        /* estilos mobile */
    }
    
    #qualificacoes {
        /* estilos mobile */
    }
}

@media (max-width: 480px) {
    /* Ultra mobile */
}