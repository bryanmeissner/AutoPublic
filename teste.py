import pyautogui as pag
import time as tm


# Variaveis
imagem = False
email = 'staffxcraft@gmail.com'
password = 'dongls123'
imgEmail = 'resources\email.png'
pag.PAUSE = 1


def moveClick(x, y):
    pag.moveTo(x, y)
    pag.click(x, y)



# Abrir o navegado e entrar no site
pag.press('win')
pag.write('chrome')
pag.press('enter')
pag.write('https://conta.olx.com.br/acesso/')
pag.press('enter')

# Fazer login
while imagem == False:

    # Pega a posição da palavra e-mail
    if pag.locateCenterOnScreen(imgEmail, confidence=0.7) != None:
        imagem = True
        x, y = pag.locateCenterOnScreen(imgEmail, confidence=0.7)


# Inseri email e senha
moveClick(x, y)
pag.press('tab')
pag.write(email)
pag.press('tab')
pag.write(password)
pag.press('enter')


# Vai até a parte de anuncios
#pag.write('https://www2.olx.com.br/ai/form/0/')