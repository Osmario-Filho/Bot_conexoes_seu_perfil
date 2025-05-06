# Bot de Envio de Convites no LinkedIn

Este projeto é um script em Python que automatiza o envio de convites de conexão no LinkedIn utilizando a biblioteca Selenium para controlar o navegador Chrome. Ele permite que você envie uma quantidade personalizada de convites de forma automática, poupando tempo e esforço.

---

## Funcionalidades

- Login automático no LinkedIn com credenciais fornecidas pelo usuário.
- Navegação até a área de conexões do LinkedIn.
- Envio automático de convites para os usuários recomendados na sua rede.
- Controle da quantidade de convites enviados, conforme definido pelo usuário.
- Tratamento de exceções comuns durante a interação com elementos da página.
- Rolagem automática da página para carregar mais perfis quando necessário.
- Mensagens de progresso exibidas no console para acompanhamento.

---

## Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- WebDriver Manager para gerenciamento automático do ChromeDriver
- Google Chrome (navegador)

---

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado:

- Python 3.x ([Download](https://www.python.org/downloads/))
- Google Chrome instalado no seu sistema.
- Bibliotecas Python necessárias:
pip install selenium webdriver-manager

---

## Como usar

1. Clone este repositório ou baixe os arquivos.

2. Abra o terminal na pasta do projeto.

3. Execute o script com o comando:

python nome_do_seu_script.py


4. Insira as informações solicitadas pelo script:

- Seu e-mail de usuário do LinkedIn.
- Sua senha do LinkedIn.
- A quantidade de convites que deseja enviar.

5. O script abrirá o navegador, fará login e começará a enviar os convites automaticamente para os usuários recomendados na sua rede.

6. Acompanhe as mensagens no console para ver o progresso.

7. Ao final, pressione Enter para fechar o navegador.

---

## Atenção e Responsabilidade

- Para que o script funcione corretamente, **é necessário desabilitar a verificação em duas etapas (autenticação de dois fatores)** na sua conta do LinkedIn.  
  Isso porque o script automatiza o login e não consegue lidar com a etapa extra de verificação, o que impediria o acesso automatizado.

- Use este script com responsabilidade e respeite as políticas do LinkedIn para evitar bloqueios ou restrições na sua conta.

- O LinkedIn pode limitar ou bloquear ações automatizadas que violem seus termos de uso.

- Este script é fornecido para fins educacionais e de automação pessoal.

---

## Estrutura do Código

O script realiza as seguintes etapas principais:

- Solicita as credenciais e quantidade de convites.
- Inicializa o ChromeDriver automaticamente.
- Realiza login no LinkedIn.
- Navega até a seção de conexões.
- Envia convites clicando nos botões "Conectar" dos usuários recomendados na sua rede.
- Rola a página para carregar mais perfis conforme necessário.
- Trata exceções comuns para evitar falhas durante a execução.

---

## Possíveis melhorias

- Implementar autenticação via OAuth para maior segurança.
- Adicionar suporte a múltiplas contas.
- Melhorar o tratamento de erros e logs.
- Automatizar o login com autenticação em duas etapas.
- Criar interface gráfica para facilitar o uso.

---


## Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- Email: osmarioslfilho@gmail.com  
- GitHub: https://github.com/Osmario-Filho

---

Obrigado por usar este projeto! 🚀
