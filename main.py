
from datetime import datetime


emprestados = []
with open('emprestados.txt', 'r') as emprestados_file:
    for x in emprestados_file:
        emprestados.append(x.replace('\n', ''))

devolvidos = []
with open('devolvidos.txt', 'r') as devolvidos_file:
    for x in devolvidos_file:
        devolvidos.append(x.replace('\n', ''))


while True:
    
    print("últimos itens emprestados")
    for i, item in enumerate(emprestados[::-1]):
        if i >= 5:
            break
        print(f"{i + 1} - {item}")

    print("\núltimos itens devolvidos")
    for i, item in enumerate(devolvidos[::-1]):
        if i >= 5:
            break
        print(f"{i + 1} - {item}")

    print("\n0 - SAIR | 1 - Novo Empréstimo | 2 - Nova Devolução")
    opcoes = int(input("Escolha uma opção: "))
    match opcoes:
        case 0:
            print("Saindo...")
            break
        case 1:
            item = input("Nome do item: ")
            pessoa = input("Nome da pessoa: ")
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            emprestados.append(f'"{item}";"{pessoa}";"{data}"')
            with open('emprestados.txt', 'a') as emprestados_file:
                emprestados_file.write(f'"{item}";"{pessoa}";"{data}"\n')
            print("Empréstimo registrado com sucesso!")
        case 2:
            for i, item in enumerate(emprestados):
                print(f"{i + 1} - {item}")
            devolucao_index = int(input("Escolha o número do item devolvido: ")) 
            devolvido_item = emprestados.pop(devolucao_index - 1)
            devolvido_item += f';"{datetime.now().strftime("%d/%m/%Y %H:%M")}"'
            devolvidos.append(devolvido_item)
            with open('devolvidos.txt', 'a') as devolvidos_file:
                devolvidos_file.write(f"{devolvido_item}\n")
            with open('emprestados.txt', 'w') as emprestados_file:
                for item in emprestados:
                    emprestados_file.write(f"{item}\n")
            print("Devolução registrada com sucesso!")