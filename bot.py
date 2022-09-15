from playwright.sync_api import sync_playwright
import pyautogui as pag
import time as tm

# Variaveis
email = 'staffxcraft@gmail.com'
password = 'dongls123'


with sync_playwright() as p:
    # Configurações
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()


    # Faz login
    page.goto('https://conta.olx.com.br/acesso/')
    page.fill('input[type="email"]', email)
    page.fill('input[type="password"]', password)
    page.click('button[class="sc-kGXeez kgGtxX"]')

    
    # Vai para a parte de anuncios
    page.locator('a[class="sc-jDwBTQ fiHbAO"]').wait_for()
    page.goto('https://www2.olx.com.br/ai/form/0/')


    # Preenche os campos

    # Titulo
    page.locator('//*[@id="subject"]').wait_for()
    page.fill('//*[@id="subject"]','teste') # Titulo

    # Descricao
    page.locator('//*[@id="body"]').wait_for()
    page.fill('//*[@id="body"]', 'teste') # Descricao

    # Categoria
    page.locator('//*[@id="category_item-3000"]').wait_for()
    page.click('//*[@id="category_item-3000"]')
    page.locator('//*[@id="category_item-3020"]').wait_for()
    page.click('//*[@id="category_item-3020"]')


    # Tipo
    page.locator('//*[@id="videogame_type"]').wait_for()
    page.click('//*[@id="videogame_type"]')
    page.keyboard.type('Console', delay= 100)
    page.keyboard.press('Enter')


    # Modelo
    page.locator('//*[@id="videogame_model"]').wait_for()
    page.click('//*[@id="videogame_model"]')
    page.keyboard.type('Playstation 4', delay=100)
    page.keyboard.press('Enter')


    # Preco
    page.locator('//*[@id="price_text"]').wait_for()
    page.fill('//*[@id="price_text"]', '5000')


    # Envia imagens
    page.locator('input[class="ai-input ai-input--file box__field"]').wait_for()
    page.click('input[class="ai-input ai-input--file box__field"]')
    print('Passou')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("resources\email.png"))



    
    
    tm.sleep(9000)