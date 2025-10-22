from datetime import datetime

def txt_to_list(filename):
    items = []
    with open(filename, 'r') as file:
        for x in file:
            items.append(x.replace('\n', '').split(';'))
    return items

def printt(table):
    atributes = [0 for _ in range(len(table[0]))]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > atributes[j]:
                atributes[j] = len(table[i][j])
    
    for i in range(len(table)):
        print(i + 1, end=' |')
        for j in range(len(table[i])):
            print(f" {table[i][j]}".ljust(atributes[j] + 2), end='|')
        print()

emprestados = txt_to_list('emprestados.txt')
devolvidos = txt_to_list('devolvidos.txt')

while True:
    
    print("últimos itens emprestados")
    printt(emprestados[::-1][0:5])

    print("\núltimos itens devolvidos")
    printt(devolvidos[::-1][0:5])

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

            emprestados.append([item, pessoa, data])

            with open('emprestados.txt', 'a') as emprestados_file:
                emprestados_file.write(f'"{item}";"{pessoa}";"{data}"\n')

            print("Empréstimo registrado com sucesso!")
        case 2:
            for i, item in enumerate(emprestados):
                print(f"{i + 1} - {item}")

            devolucao_index = int(input("Escolha o número do item devolvido: ")) 
            devolvido_item = emprestados.pop(devolucao_index - 1)
            devolvido_item.append(f'"{datetime.now().strftime("%d/%m/%Y %H:%M")}"')
            devolvidos.append(devolvido_item)

            with open('devolvidos.txt', 'a') as devolvidos_file:
                aux = ';'.join(devolvido_item)
                devolvidos_file.write(f"{aux}\n")

            with open('emprestados.txt', 'w') as emprestados_file:
                for item in emprestados:
                    aux = ';'.join(item)
                    emprestados_file.write(f"{aux}\n")

            print("Devolução registrada com sucesso!")