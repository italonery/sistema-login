"""
Sistema de login utilizando a biblioteca PySimpleGUI
"""
import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'login':
        USUARIO_CORRETO = 'italonery'
        SENHA_CORRETA = '123456'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            window['mensagem'].update('Login realizado com sucesso!')
        else:
            window['mensagem'].update('Usuário ou senha incorreto!')
