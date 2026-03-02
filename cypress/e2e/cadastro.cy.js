describe('Teste de Cadastro', () => {
    before(() => {
        cy.visit('http://127.0.0.1:5500/index.html')
    })

    it('Deve rejeitar email sem @', () => {
        // Navegar
        cy.get('a[href="#cadastre-se"]').click()

        // Preencher COM EMAIL SEM @
        cy.get('input#nome-criar').type('João Silva')
        cy.get('input#email-cadastro').type('jheisongmail.com')  // ❌ Sem @!
        cy.get('input#password-criar').type('Senha123')
        cy.get('input#password-confirmar').type('Senha123')
        cy.get('input#whatsapp').type('61999999999')

        // Clicar em cadastrar
        cy.get('button#btn-cadastrar').click()

        // VERIFICAR se o erro apareceu
        cy.get('div#erro-cadastro').should('contain', 'Email')
        // ✅ Se erro apareceu, teste passa!
    })
})
