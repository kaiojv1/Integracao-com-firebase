import PySimpleGUI as sg
import requests
import json

sg.theme('Black')
link_usuario_apagar= "URL da seção que deseja apagar o usuário"



def deletar_usuario():

    layout_deletar = [ [sg.Text("Nome: "), sg.Input("", key="nome")], [sg.Button("Deletar")] ]


    window = sg.Window("Deletar Usuário", layout_deletar)


    while True:
        event, value = window.read()
        

        if event == sg.WIN_CLOSED:
            break

        if event == "Deletar":    
            requisicao = requests.get(f"{link_usuario_apagar}/.json")
            dic_requisicao = requisicao.json()

            try:
                for usuarios in dic_requisicao:
                    registrados = dic_requisicao[usuarios]["Name"]
                    
                    if value["nome"] in registrados:
                        requisicao_deletar = requests.delete(f"{link_usuario_apagar}/{usuarios}.json")
                        sg.Popup(f"O usuário {registrados} Foi deletado com sucesso")

            except KeyError:
                pass
