describe('Teste de Login - Barbearia Morais', () => {
    
    // Antes de cada teste, abra o site
    beforeEach(() => {
        cy.visit('http://127.0.0.1:5500/index.html')
    })

    // TESTE 1: Login com sucesso
    it('Deve fazer login com dados corretos', () => {
        // Verificar se a página carregou
        cy.contains('Barbearia Morais').should('be.visible')
        
        // Digitar email
        cy.get('input#email-login').type('usuario@email.com')
        
        // Digitar senha
        cy.get('input#password-login').type('Senha123')
        
        // Clicar em Login
        cy.get('button#btn-login').click()
        
        // Verificar se foi para dashboard
        cy.get('#tela-dashboard').should('have.class', 'ativa')
    })

    // TESTE 2: Email sem @
    it('Deve mostrar erro com email inválido', () => {
        // Digitar email SEM @
        cy.get('input#email-login').type('usuarioemail.com')
        
        // Digitar senha
        cy.get('input#password-login').type('Senha123')
        
        // Clicar em Login
        cy.get('button#btn-login').click()
        
        // Verificar se mostra erro
        cy.get('div#erro-login').should('contain', 'Email')
    })

    // TESTE 3: Senha muito curta
    it('Deve mostrar erro com senha curta', () => {
        // Digitar email
        cy.get('input#email-login').type('usuario@email.com')
        
        // Digitar senha COM POUCOS CARACTERES
        cy.get('input#password-login').type('Abc')
        
        // Clicar em Login
        cy.get('button#btn-login').click()
        
        // Verificar se mostra erro
        cy.get('div#erro-login').should('contain', 'caracteres')
    })
});

it('cadastro.cy.js', function() {});