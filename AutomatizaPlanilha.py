# Pegar dado do site web scraping - Selenium
# Acessar o site
# extrair titulo(nome da pessoa que falou no chamado)
# extrair data e hora
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

numero = input('Digite o numero do chamado')
# iniciar o navegador, para acessar o site. ex "https://lista.mercadolivre.com.br/computador"

driver = webdriver.Chrome()
driver.get('https://lista.mercadolivre.com.br/computador')

# extrair titulo(nome da pessoa que falou no chamado)

# encontrar o elemento de o valor para extração via xpath   //tag[@atributo='valor']
titulos = driver.find_elements(
    By.XPATH, "//h2[@class='ui-search-item__title']")
precos = driver.find_elements(
    By.XPATH, "//span[@class='andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript']")


# Criar planilha

Workbook = openpyxl.Workbook()

# Criar pagina Produtos

Workbook.create_sheet('produtos')

# Selecionar a pagina Produtos

shet_produtos = Workbook['produtos']

# Passar dados para planilha - Openpyxl

shet_produtos['A1'].value = 'Produto'
shet_produtos['B1'].value = 'Preço'


# laço de repetição para encontra todos os textos validos para o projeto.

for titulo, preco in zip(titulos, precos):
    shet_produtos.append([titulo.text, preco.text])


# Salvar dados na planilha. *Importante lembrar de colocar a extenção xlsx
Workbook.save(f'Chamado {numero}.xlsx')
