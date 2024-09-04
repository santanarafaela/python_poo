import pickle
import traceback
<<<<<<< HEAD
import gerenciar_urna
=======

>>>>>>> origin/main
from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

<<<<<<< HEAD
def menu():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Inserir Candidato")
    print("4-Listar Candidatos")
    print("5-Iniciar Urna")
    print("6-Testar Urna")
    print("7-Emitir zeresima")
    print("8- Finalizar")
    print("9-Sair")
    op = int(input("Digite a opcao [1 a 9]? "))
    while op not in range(1, 10):
        op = int(input("Digite a opcao [1 a 9]? "))
    return op

=======
def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def menu_candidato():
    print("1-Novo Candidato")
    print("2-Listar candidatos")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_candidatos(candidatos):
    numero = int(input('Digite o número: '))

    if numero in candidatos:
        raise Exception('Candidato já existe!')

    nome = input('Digite o nome: ')
    RG = input('Digite o RG: ')
    CPF = input('Digite o CPF: ')

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[numero] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Arquivo gravado com sucesso!')

def lista_candidatos(candidato):
    for c in candidatos.values():
        print(f'Candidato número: {str(c.get_numero())}')
        print("-------------------------------------------")
        print(c)

>>>>>>> origin/main
def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
<<<<<<< HEAD
    secao = int(input("Digite a secao: "))
    zona = int(input("Digite a zona: "))
=======
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")
>>>>>>> origin/main

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
<<<<<<< HEAD
        secao = int(input("Digite a nova secao: "))
        zona = int(input("Digite a nova zona: "))
=======
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
>>>>>>> origin/main
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

<<<<<<< HEAD
def inserir_candidato(candidatos):
    numero = int(input("Digite o número do candidato: "))

    if numero in candidatos:
        raise Exception("Candidato já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def listar_candidatos(candidatos):
    for candidato in candidatos.values():
        print(candidato)

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
=======
if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    candidatos = {} #dicionario a chave será o número

>>>>>>> origin/main
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
<<<<<<< HEAD
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    candidatos = {}  # dicionário a chave será o titulo
    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    opcao = 1
    while opcao in range(1,8):
        try:
            opcao = menu()

            if opcao == 1:
                inserir_eleitor(eleitores)
            elif opcao == 2:
                atualizar_eleitor(eleitores)
            elif opcao == 3:
                inserir_candidato(candidatos)
            elif opcao == 4:
                listar_candidatos(candidatos)
            elif opcao == 5:
                urna = gerenciar_urna.iniciar_urna(eleitores.values(),
                                                   candidatos.values())
            elif opcao == 6:
                gerenciar_urna.votar(urna)
            elif opcao == 7:
                gerenciar_urna.emitir_zeresima(urna)
            elif opcao == 8:
                gerenciar_urna.finalizar(urna)
            elif opcao == 9:
                print("Saindo!")
                break
        except Exception as e:
            #traceback.print_exc()
            print(e)
=======

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)

    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado!")

    op_usr = 1
    while op_usr in (1, 2):
        op_usr = int(input('Gerenciar\n1 - Candidatos\n2 - Eleitores[1,2]:\n '))

    if op_usr == 1:
        opcao = 1
        while opcao in (1, 2, 3):
            try:
                opcao = menu_candidato()

                if opcao == 1:
                    inserir_candidatos(candidatos)
                elif opcao == 2:
                    lista_candidatos(candidatos)
                elif opcao == 3:
                    print("Saindo!")
                    break
            except Exception as e:
                # traceback.print_exc()
                print('Erro')

>>>>>>> origin/main
