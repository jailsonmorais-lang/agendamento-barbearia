# 📐 Sistema de Espaçamento Profissional para Mobile-First

**Versão:** 1.0  
**Data:** Fevereiro 2026  
**Padrão:** Mobile-First Responsivo  

---

## 🎯 Introdução

Este documento define um **padrão profissional** de espaçamento para aplicações web responsivas. Use este padrão em **TODOS** os seus projetos para manter consistência e profissionalismo.

---

## 📋 Índice

1. [Passo 1: Entender a Escala de Telas](#passo-1-entender-a-escala-de-telas)
2. [Passo 2: A Escala de Espaçamento](#passo-2-a-escala-de-espaçamento)
3. [Passo 3: Padrão de Padding](#passo-3-padrão-de-padding-por-tipo-de-elemento)
4. [Passo 4: Padrão de Margin](#passo-4-padrão-de-margin)
5. [Passo 5: Padrão de Font-Size](#passo-5-padrão-de-font-size)
6. [Passo 6: Padrão de Border-Radius](#passo-6-padrão-de-border-radius)
7. [Passo 7: Padrão de Width](#passo-7-padrão-de-width-para-containers)
8. [Passo 8: Template Organizado](#passo-8-template-de-media-query-organizado)
9. [Tabela de Referência](#-tabela-rápida-de-referência)
10. [Checklist](#-checklist-quando-criar-um-novo-elemento)
11. [Exemplo Prático](#-exemplo-prático-seu-card-de-serviço)

---

## Passo 1: Entender a Escala de Telas

Existem **3 tamanhos de telas**. Cada uma tem seus próprios valores:

```
CELULAR:  até 480px
TABLET:   481px até 768px
DESKTOP:  769px em diante
```

Para cada tamanho, você vai usar **valores diferentes** de:
- Padding
- Margin
- Gap
- Font-size
- Border-radius

---

## Passo 2: A Escala de Espaçamento

Crie uma **tabela mental** com esses valores:

### **MOBILE (até 480px)**

```
Espaçamento Mínimo:     4px   (muito pequeno)
Espaçamento Pequeno:    8px   (ícones, gaps pequenos)
Espaçamento Médio:      12px  (entre elementos)
Espaçamento Grande:     16px  (padding de containers)
Espaçamento Muito Grande: 20px (padding de seções)
Espaçamento Enorme:     24px  (margin entre grandes blocos)
```

### **TABLET (481px até 768px)**

```
Espaçamento Pequeno:    8px
Espaçamento Médio:      12px
Espaçamento Grande:     20px  (aumenta um pouco)
Espaçamento Muito Grande: 24px
Espaçamento Enorme:     32px
```

### **DESKTOP (769px acima)**

```
Espaçamento Pequeno:    8px
Espaçamento Médio:      16px
Espaçamento Grande:     24px  (maior ainda)
Espaçamento Muito Grande: 32px
Espaçamento Enorme:     40px
Espaçamento Gigante:    50px
```

---

## Passo 3: Padrão de Padding por Tipo de Elemento

### **Buttons (Botões)**

```css
/* MOBILE */
@media (max-width: 480px) {
    button {
        padding: 10px 16px;  /* Vertical | Horizontal */
        height: 40px;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    button {
        padding: 12px 20px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    button {
        padding: 12px 24px;
    }
}
```

### **Containers/Sections**

```css
/* MOBILE */
@media (max-width: 480px) {
    .container,
    .div-section,
    .form-login {
        padding: 16px;  /* Só um valor = todos os lados */
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .container,
    .div-section,
    .form-login {
        padding: 24px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .container,
    .div-section,
    .form-login {
        padding: 32px;
    }
}
```

### **Inputs**

```css
/* MOBILE */
@media (max-width: 480px) {
    input {
        padding: 10px 12px;
        height: 40px;
        width: 100%;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    input {
        padding: 12px 16px;
        height: 44px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    input {
        padding: 12px 16px;
        height: 48px;
    }
}
```

### **Gaps (Espaço entre itens)**

```css
/* MOBILE */
@media (max-width: 480px) {
    .container {
        gap: 16px;  /* Menos espaço */
    }
    
    .div-informacoes-cortes {
        gap: 8px;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .container {
        gap: 24px;
    }
    
    .div-informacoes-cortes {
        gap: 12px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .container {
        gap: 32px;
    }
    
    .div-informacoes-cortes {
        gap: 16px;
    }
}
```

---

## Passo 4: Padrão de Margin

### **Entre Títulos e Conteúdo**

```css
/* MOBILE */
@media (max-width: 480px) {
    .titulo-principal {
        margin-bottom: 16px;  /* Espaço abaixo do título */
    }
    
    .titulo-secundario {
        margin-bottom: 12px;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .titulo-principal {
        margin-bottom: 24px;
    }
    
    .titulo-secundario {
        margin-bottom: 16px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .titulo-principal {
        margin-bottom: 32px;
    }
    
    .titulo-secundario {
        margin-bottom: 20px;
    }
}
```

### **Entre Seções**

```css
/* MOBILE */
@media (max-width: 480px) {
    section {
        margin-bottom: 24px;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    section {
        margin-bottom: 32px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    section {
        margin-bottom: 48px;
    }
}
```

---

## Passo 5: Padrão de Font-Size

### **Títulos Principais**

```css
/* MOBILE */
@media (max-width: 480px) {
    .titulo-principal {
        font-size: 1.75rem;  /* 28px */
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .titulo-principal {
        font-size: 2rem;  /* 32px */
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .titulo-principal {
        font-size: 2.5rem;  /* 40px */
    }
}
```

### **Títulos Secundários**

```css
/* MOBILE */
@media (max-width: 480px) {
    .titulo-secundario {
        font-size: 1.25rem;  /* 20px */
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .titulo-secundario {
        font-size: 1.5rem;  /* 24px */
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .titulo-secundario {
        font-size: 1.75rem;  /* 28px */
    }
}
```

### **Corpo (Parágrafos)**

```css
/* MOBILE */
@media (max-width: 480px) {
    p, span {
        font-size: 0.875rem;  /* 14px */
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    p, span {
        font-size: 1rem;  /* 16px */
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    p, span {
        font-size: 1rem;  /* 16px */
    }
}
```

---

## Passo 6: Padrão de Border-Radius

```css
/* MOBILE */
@media (max-width: 480px) {
    button,
    input,
    .card,
    .container {
        border-radius: 8px;  /* Menos arredondado */
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    button,
    input,
    .card,
    .container {
        border-radius: 10px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    button,
    input,
    .card,
    .container {
        border-radius: 12px;  /* Mais arredondado */
    }
}
```

---

## Passo 7: Padrão de Width para Containers

```css
/* MOBILE - Always Full Width */
@media (max-width: 480px) {
    .container,
    .div-section,
    .form-login {
        width: 100%;
        max-width: 100%;
    }
}

/* TABLET - Pequeno Margin */
@media (min-width: 481px) and (max-width: 768px) {
    .container,
    .div-section,
    .form-login {
        width: 90%;
        max-width: 600px;
    }
}

/* DESKTOP - Mais Controle */
@media (min-width: 769px) {
    .container,
    .div-section,
    .form-login {
        width: 100%;
        max-width: 600px;
    }
}
```

---

## Passo 8: Template de Media Query Organizado

**Sempre use essa estrutura** no seu CSS:

```css
/* ===== MOBILE (até 480px) ===== */
@media (max-width: 480px) {
    /* Padding dos containers */
    .container {
        padding: 16px;
    }
    
    /* Buttons */
    button {
        padding: 10px 16px;
        height: 40px;
    }
    
    /* Inputs */
    input {
        padding: 10px 12px;
        height: 40px;
    }
    
    /* Gaps */
    .container {
        gap: 16px;
    }
    
    /* Font sizes */
    .titulo-principal {
        font-size: 1.75rem;
    }
    
    /* Border radius */
    button, input, .container {
        border-radius: 8px;
    }
}

/* ===== TABLET (481px até 768px) ===== */
@media (min-width: 481px) and (max-width: 768px) {
    .container {
        padding: 24px;
    }
    
    button {
        padding: 12px 20px;
    }
    
    input {
        padding: 12px 16px;
        height: 44px;
    }
    
    .container {
        gap: 24px;
    }
    
    .titulo-principal {
        font-size: 2rem;
    }
    
    button, input, .container {
        border-radius: 10px;
    }
}

/* ===== DESKTOP (769px acima) ===== */
@media (min-width: 769px) {
    .container {
        padding: 32px;
    }
    
    button {
        padding: 12px 24px;
    }
    
    input {
        padding: 12px 16px;
        height: 48px;
    }
    
    .container {
        gap: 32px;
    }
    
    .titulo-principal {
        font-size: 2.5rem;
    }
    
    button, input, .container {
        border-radius: 12px;
    }
}
```

---

## 📊 Tabela Rápida de Referência

Imprima ou salve isso:

```
╔════════════════════════════════════════════════════════════════╗
║         PADRÃO DE ESPAÇAMENTO RESPONSIVO                       ║
╠════════════════════════════════════════════════════════════════╣
║                  MOBILE    │  TABLET   │  DESKTOP              ║
║ Padding Container  16px    │   24px    │   32px                ║
║ Button Padding     10x16px │  12x20px  │  12x24px              ║
║ Input Height       40px    │   44px    │   48px                ║
║ Gap Containers     16px    │   24px    │   32px                ║
║ Título Principal   1.75rem │   2rem    │  2.5rem               ║
║ Título Secundário  1.25rem │  1.5rem   │  1.75rem              ║
║ Border Radius      8px     │   10px    │   12px                ║
║ Container Width    100%    │   90%     │  100%                 ║
║ Container MaxW     100%    │  600px    │  600px                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 🎯 Checklist: Quando Criar um Novo Elemento

Sempre que você criar algo NOVO, pergunte:

### 1. **Qual o padding?**
   - Mobile: 16px?
   - Tablet: 24px?
   - Desktop: 32px?

### 2. **Qual a margin?**
   - Mobile: 12px abaixo?
   - Tablet: 16px?
   - Desktop: 20px?

### 3. **Qual o font-size?**
   - Mobile: 14px?
   - Tablet: 16px?
   - Desktop: 16px?

### 4. **Qual o gap?**
   - Mobile: 8px?
   - Tablet: 12px?
   - Desktop: 16px?

### 5. **Qual o width?**
   - Mobile: 100%?
   - Tablet: 90%?
   - Desktop: 600px max?

---

## 💡 Exemplo Prático: Seu Card de Serviço

Usando o padrão:

```css
/* CSS NORMAL (sem media query) */
.card-servico {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    background: var(--fundo-secundario);
}

/* MOBILE */
@media (max-width: 480px) {
    .card-servico {
        padding: 12px;
        margin-bottom: 16px;
        border-radius: 8px;
    }
    
    .card-servico__titulo {
        font-size: 1.1rem;
        margin-bottom: 8px;
    }
}

/* TABLET */
@media (min-width: 481px) and (max-width: 768px) {
    .card-servico {
        padding: 16px;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    
    .card-servico__titulo {
        font-size: 1.3rem;
        margin-bottom: 12px;
    }
}

/* DESKTOP */
@media (min-width: 769px) {
    .card-servico {
        padding: 20px;
        margin-bottom: 24px;
        border-radius: 12px;
    }
    
    .card-servico__titulo {
        font-size: 1.5rem;
        margin-bottom: 16px;
    }
}
```

---

## 🚀 Resumo: Use SEMPRE Esses Valores

**NUNCA invente novos números!** Use SEMPRE:

### Padding/Margin:
```
8px, 12px, 16px, 20px, 24px, 32px
```

### Font-size:
```
0.875rem (14px)
1rem (16px)
1.25rem (20px)
1.5rem (24px)
1.75rem (28px)
2rem (32px)
2.5rem (40px)
```

### Border-radius:
```
8px, 10px, 12px
```

### Gap:
```
8px, 12px, 16px, 20px, 24px, 32px
```

### Width:
```
100%, 90%, com max-width de 600px
```

---

## 📌 Dicas Finais

### ✅ Faça

- Use os valores da tabela sempre
- Teste em 3 tamanhos: 375px (mobile), 768px (tablet), 1920px (desktop)
- Use `max-width` junto com percentual de width
- Organize media queries do mobile para desktop
- Use `gap` em flex containers (melhor que margin)

### ❌ NÃO Faça

- Não invente valores de espaçamento
- Não use `padding: 17px` ou `margin: 23px`
- Não misture unidades (px com em)
- Não use `width: 400px` fixo em celular
- Não esqueça de testar responsivo

---

## 📞 Como Usar Este Documento

1. **Salve este arquivo** em seu projeto
2. **Sempre consulte** quando criar novo CSS
3. **Copie o template** de media query para cada novo elemento
4. **Use a tabela de referência** como atalho rápido

---

**Status:** ✅ Pronto para Usar  
**Versão:** 1.0  
**Última atualização:** Fevereiro 2026

---

**Bom código! 🚀**
