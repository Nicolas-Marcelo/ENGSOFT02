import PySimpleGUI as sg

layout = [
    [sg.Text("Pegar Cotação da Moeda")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotacao")],
]

janela = sg.Window("Uma nova janela", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar cotação":
        codigo_cotacao = valores["nome_contacao"]

janela.clode()
