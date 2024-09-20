'''
Quais passos manuais preciso fazer
para enviar uma mensagem para várias pessoas?
'''
import pyautogui
import webbrowser
from time import sleep
# 1- lista de números
telefones = ['Números dos contatos a serem enviadas mensagens separadas por vírgula']
#ou caso tenha uma lista em txt dos números:
'''
telefones = []
with open('nomeDaLista.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)  
'''
# 2- enviar individualmente uma mensagem para cada pessoa
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(-669,272, duration=1)
    sleep(10)
    pyautogui.typewrite('teste de envio automatizado.')
    sleep(5)
    pyautogui.press('enter')
    sleep(60)
# 3- Pausar entre cada envio
