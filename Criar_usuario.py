import requests
import json

link_registro_usuario = "ainda em construção"
link_usuario_ja_registrador = "URL do firebase"




def verificando_se_usario_ja_existe(name,email):
    requisicao = requests.get(f"{link_registro_usuario}/.json")
    dic_requisicao = requisicao.json()

    for usuarios in dic_requisicao:
        nome_cliente = dic_requisicao[usuarios]["Name"]
        email_cliente = dic_requisicao[usuarios]["E-mail"]

        if name in nome_cliente:
            print(f"Esse nome {name} já existe")
        elif email in email_cliente:
            print(f"O email {email} já existe")
    

    
   
         
    

def registrar_usuario(name,email,departamento,salario,aniversario):
    

    #verificacao_de_usuario = verificando_se_usario_ja_existe(name,email,departamento,salario)


    dados_usuario = {
        "Name": f"{name}",
        "E-mail": f"{email}",
        "department": f"{departamento}",
        "salary": f"{salario}",
        "birth_date": f"{aniversario}"
    }
    


    requisicao = requests.post(f"{link_registro_usuario}/.json", data=json.dumps(dados_usuario))


