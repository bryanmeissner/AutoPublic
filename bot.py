from playwright.sync_api import sync_playwright
from time import sleep


def programa():

    item_pesquisa = ""
    ordenacao = True
    valor_min_max = True
    
    mercado_livre = "iphone-13"
    amazon = "s?k=iphone+13"

    if valor_min_max == True:
        mercado_livre += '_PriceRange_1000-0_NoIndex_True'
        amazon += '&rh=p_36%3A500000-'

    if ordenacao == True:
        mercado_livre += '_OrderId_PRICE_NoIndex_True'
        amazon += '&s=price-asc-rank'
        


    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Vai até o Mercado Livre com o preço minimo e a ordenação
        page.goto(f'https://lista.mercadolivre.com.br/{mercado_livre}')


        # Pega o nome do produto
        nome_produtoM = page.locator('li.ui-search-layout__item:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > a > h2').all_text_contents()
        
        # Pega o valor do produto
        valor_produtoM = page.locator('li.ui-search-layout__item:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div > div > div > span:nth-child(1) > span:nth-child(2) > span:nth-child(2)').all_text_contents()
        print(f'Mercado Livre: {nome_produtoM} - {valor_produtoM}')
        

        # Vai até a Amazon com o preço minimo e a ordenação
        page.goto(f'https://www.amazon.com.br/{amazon}')

        # Pega o nome do produto
        nome_produtoA = page.locator('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[2]/div[1]/h2/a/span').all_text_contents()

        # Pega o valor do produto
        valor_produtoA = page.locator('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[2]/div[3]/div/div[1]/a/span/span[2]/span[2]').all_text_contents()
        valor_produtoA += page.locator('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[2]/div[3]/div/div[1]/a/span/span[2]/span[3]').all_text_contents()






        
        print(f'Amazon: {nome_produtoA} - {valor_produtoA}')
        browser.close()


programa()