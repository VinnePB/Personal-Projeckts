alunos = []
disciplinas = {}

def cadastrar_disciplina():
    nome = input("Digite o nome da disciplina: ").strip()

    if nome == "":
        print("Nome inválido.\n")
        return

    if nome in disciplinas:
        print("Essa disciplina já existe.\n")
    else:
        disciplinas[nome] = []
        print("Disciplina cadastrada com sucesso!\n")


def cadastrar_aluno():

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        print("Cadastre uma disciplina primeiro.\n")
        return

    nome = input("Digite o nome do aluno: ").strip()

    if nome == "":
        print("Nome inválido.\n")
        return

    print("\nDisciplinas disponíveis:")

    lista = list(disciplinas.keys())

    for i, d in enumerate(lista, 1):
        print(f"{i} - {d}")

    try:
        escolha = int(input("Escolha o número da disciplina: "))
        disciplina = lista[escolha - 1]
    except:
        print("Escolha inválida.\n")
        return

    alunos.append({"nome": nome, "disciplina": disciplina})
    disciplinas[disciplina].append(nome)

    print("Aluno cadastrado com sucesso!\n")


def listar_alunos():

    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("\nLista de alunos:")

    for aluno in alunos:
        print(f"{aluno['nome']} - {aluno['disciplina']}")

    print()


def listar_por_disciplina():

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.\n")
        return

    print("\nDisciplinas:")

    lista = list(disciplinas.keys())

    for i, d in enumerate(lista, 1):
        print(f"{i} - {d}")

    try:
        escolha = int(input("Escolha a disciplina: "))
        disciplina = lista[escolha - 1]
    except:
        print("Opção inválida.\n")
        return

    print(f"\nAlunos da disciplina {disciplina}:")

    if not disciplinas[disciplina]:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in disciplinas[disciplina]:
            print("-", aluno)

    print()


def menu():

    while True:

        print("===== SISTEMA ESCOLAR =====")
        print("1 - Cadastrar disciplina")
        print("2 - Cadastrar aluno")
        print("3 - Listar alunos")
        print("4 - Listar alunos por disciplina")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_disciplina()

        elif opcao == "2":
            cadastrar_aluno()

        elif opcao == "3":
            listar_alunos()

        elif opcao == "4":
            listar_por_disciplina()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.\n")


menu()
