from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

# Solicita o email do usuário
nome_usuario = input("Digite o seu email de usuário: ") 
# Solicita a senha do usuário
senha_usuario = input("Digite sua senha de usuário: ") 
# Solicita a quantidade de convites que deseja enviar
quantidade_convites = int(input('Digite a quantidade de convites que deseja ser enviado: '))

# Configura o serviço do ChromeDriver
servico = Service(ChromeDriverManager().install())
# Inicializa o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessa a página de login do LinkedIn
navegador.get("https://www.linkedin.com/login/")

# Maximiza a janela do navegador
navegador.maximize_window() 

# Define o tempo máximo de espera para elementos ficarem disponíveis
wait = WebDriverWait(navegador, 15) 

# Espera até o campo de usuário estar clicável e preenche com o email
preencher_usuario = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
preencher_usuario.click()
preencher_usuario.send_keys(nome_usuario)

# Preenche o campo de senha
navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha_usuario)

# Clica no botão de login
navegador.find_element('xpath', '//*[@id="organic-div"]/form/div[4]/button').click()

# Acessa a área de conexões
area_conexao = navegador.find_element('xpath', '//*[@id="global-nav"]/div/nav/ul/li[2]/a')
area_conexao.click()

# Espera até que pelo menos um botão "Conectar" esteja clicável
conectar_usuario = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//button[.//span[contains(text(), "Conectar")]]')
    )
)

# Define o tempo de pausa após rolagem para carregar mais perfis
SCROLL_PAUSE_TIME = 2

# Inicializa o contador de convites enviados
contador_convites = 0

# Loop principal que continua enquanto não atingir a quantidade desejada de convites
while contador_convites < quantidade_convites:
    # Busca todos os botões "Conectar" visíveis na página
    botoes_conectar = navegador.find_elements(By.XPATH, '//button[.//span[contains(text(), "Conectar")]]')

    if botoes_conectar:
        # Itera sobre cada botão encontrado
        for botao in botoes_conectar:
            # Verifica se ainda pode enviar convites
            if contador_convites < quantidade_convites:
                contador_convites += 1
                try:
                    # Rola a página até o botão para garantir que esteja visível
                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
                    time.sleep(0.5)  # Pequena pausa para estabilidade
                    # Clica no botão "Conectar"
                    botao.click()
                    print("Convite numero " + str(contador_convites) + " enviado!")
                    time.sleep(1)  # Pausa para evitar bloqueios por ações muito rápidas
                except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                    # Caso não consiga clicar, exibe o erro e continua para o próximo botão
                    print(f"Erro ao clicar no botão: {e}, pulando.")
                    continue
            else:
                # Sai do loop se já enviou a quantidade desejada de convites
                break

    # Rola a página para baixo para tentar carregar mais perfis
    navegador.execute_script("window.scrollBy(0, window.innerHeight);")
    print("Rolando a página para carregar perfis...")
    time.sleep(SCROLL_PAUSE_TIME)  # Pausa para o carregamento dos novos perfis

# Aguarda o usuário pressionar Enter antes de fechar o navegador
input("Pressione Enter para fechar o navegador...")
