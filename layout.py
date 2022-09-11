import PySimpleGUI as sg
from Criar_usuario import registrar_usuario, verificando_se_usario_ja_existe
from deletar_user import deletar_usuario



sg.theme('Black')

layout = [
    [sg.Text("Nome: "), sg.Input("", key="nome")],
    [sg.Text("E-mail: "), sg.Input("",key="email")],
    [sg.Text("Departament: "), sg.Input("",key="departamento")],
    [sg.Text("Salary: "), sg.Input("", key="salario")],
    [sg.Text("Birth date: "), sg.Input("",size=(4,4),key="dia"), sg.Input("",size=(4,4),key="mes"), sg.Input("",size=(4,4),key="ano")], 
    [sg.Button("Enviar"), sg.Button("Sair")],
    [sg.Text("Deletar um usuário: "),sg.Button("Deletar")]
]


window = sg.Window("Crud trabalhadores", layout)


while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED or event == "Sair":
        break

    if event ==  "Enviar":
        nome = value["nome"]
        email = value["email"]
        departamento = value["departamento"]
        salario = value["salario"]
        aniversario = str(value["dia"] + "-" + value["mes"] + "-" + value["ano"])
       
        #verificando_se_usario_ja_existe(nome, email)
        registrar_usuario(nome, email, departamento,  salario, aniversario)
        sg.popup(f"Prontinho o usuário {nome} foi registrado com sucesso :) ")

    elif event == "Deletar":
        deletar_usuario()


