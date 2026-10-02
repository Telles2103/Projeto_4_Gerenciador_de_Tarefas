import os
import json

with open("tarefas.json", "r", encoding="utf-8") as arquivo:
    tarefas = json.load(arquivo)

def mostrar_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    print("| TAREFAS ATUAIS")
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f"| Tarefa {i+1} - {tarefas['tarefas'][i]} ({tarefas['datas'][i]})")
    print(barra)
    input("| Aperte enter para continuar... ")

def adicionar_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    print("| ADICIONAR TAREFAS")
    print(barra)
    tarefa = input("| Digite o nome da tarefa: ")
    data = input("| Informe a data: ")
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    print(barra)
    print(f'Tarefa ({tarefa}) adicionado com sucesso!')
    input("| Aperte enter para continuar... ")

def remover_tarefas():
    barra = f'|{60*'-'}|'
    print(barra)
    print("| REMOVER TAREFAS")
    print(barra)
    input("| Aperte enter para continuar... ")

def mostrar_menu():
    while True:
        os.system('cls')
        barra = f'|{60*'-'}|'
        print(barra)
        print("| GERENCIADOR DE TAREFAS")
        print(barra)
        print("| 1 - Mostrar tarefas")
        print("| 2 - Adicionar tarefas")
        print("| 3 - Remover tarefas")
        print("| 4 - Sair")
        print(barra)
        opc = input("| Digite o número da opção: ")

        if opc == '1':
            os.system('cls')
            mostrar_tarefas()

        elif opc == '2':
            os.system('cls')
            adicionar_tarefas()

        elif opc == '3':
            os.system('cls')
            remover_tarefas()

        elif opc == '4':
            print("| Saindo...")

        else:
            print("Erro! Escolha uma opção válida!")
            input("| Aperte enter para continuar... ")

mostrar_menu()
