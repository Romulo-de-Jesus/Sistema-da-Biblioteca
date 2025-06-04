import time
import os

try:
    import keyboard
except:
    print("O módulo keyboard não foi instalado \n")


os.system("color 70")
os.system("title Sistema da Biblioteca")
class Livro:
    def __init__(self,id,titulo,autor,disponibilidade,pertence):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade
        self.pertence = pertence

class Usuario:
    def __init__(self,id,nome,livros):
        self.id = id
        self.nome = nome
        self.livros = livros

class Biblioteca:
    def __init__(self,livros,usuarios):
        self.livros = livros
        self.usuarios = usuarios

def pausa():
    time.sleep(3)

def prosseguir():
    try:
        print("\n","Aperte qualquer botão para prosseguir...")
        keyboard.read_event()
    except:
        print("\n")

def espaco():
    print("\n"*30)

comando = 0

Minha_Biblioteca = Biblioteca([],[])
Meu_Usuario = Usuario(0, "teste", [])
id_global = -1
id_global2 = -1
id_global3 = -1
###################
###   SISTEMA   ###
###################

while True:
    print("\n"*3)
    print("=-"*11)
    print("SISTEMA DA BIBLIOTECA")
    print("=-"*11)
    print("OQUE VOCÊ DESEJA?", "\n")
    print("1 - Cadastrar livros.")
    print("2 - Cadastrar usuários.")
    print("3 - Realizar empréstimos de livros.")
    print("4 - Listar livros disponíveis e emprestados.")
    print("5 - Informações de um usuário específico.")
    print("6 - Devolver livro.")
    print("7 - Encerrar.")





    comando = input("")
    if (comando == "1"):
        espaco()
        id_global += 1
        Meu_Livro = Livro(0,0,0,0,0)
        Meu_Livro.id = id_global
        Meu_Livro.titulo = input("insira o titulo: ")
        Meu_Livro.titulo = Meu_Livro.titulo.lower()
        Meu_Livro.autor = input("insira o autor: ")
        Meu_Livro.disponibilidade = "disponivel"
        Meu_Livro.pertence = ""
        
        Minha_Biblioteca.livros.append(Meu_Livro)

    if (comando == "2"):
         espaco()
         id_global2 += 1
         Meu_Usuario = Usuario(0,0,0)
         Meu_Usuario.id = id_global2
         Meu_Usuario.nome = input("insira o nome: ")
         Meu_Usuario.nome = Meu_Usuario.nome.lower()
         Meu_Usuario.livros = []

         Minha_Biblioteca.usuarios.append(Meu_Usuario)

    if (comando == "3"):
         espaco()
         print("=-"*11)
         print("Lista de usuários")
         print("=-"*11)
         for usuario in Minha_Biblioteca.usuarios:
             print(usuario.nome)
         print("\n")

         print("=-"*11)
         print("Lista de livros")
         print("=-"*11)
         for livro in Minha_Biblioteca.livros:
             if (livro.pertence == ""):
                print(livro.titulo)
         print("\n")

         u = input("Insira o usuário ")
         u = u.lower()
         ##vvv SE O USUÁRIO EXISTIR vvv
         for usuario in Minha_Biblioteca.usuarios:
            if usuario.nome == u:
                l = input("Insira o livro que deseja emprestar ")
                l = l.lower()
                 ##vvv SE O LIVRO EXISTIR vvv
                for livro in Minha_Biblioteca.livros:
                    if l == livro.titulo:
                        ##ALTERAR DISPONIBILIDADE DO LIVRO
                        livro.disponibilidade = "emprestado"
                        livro.pertence = usuario.nome
                        ##ADICIONAR LIVRO AO USUÁRIO
                        usuario.livros.append(livro.titulo)


                        


    if (comando == "4"):
        espaco()
        print("=-"*11)
        print("Disponíveis")
        print("=-"*11)
        for livro in Minha_Biblioteca.livros:
            if livro.disponibilidade == "disponivel":
                print(livro.titulo, "-",livro.autor)
                print("\n")

        print("=-"*11)
        print("Emprestados")
        print("=-"*11)

        for livro in Minha_Biblioteca.livros:
            if livro.disponibilidade == "emprestado":
                print(livro.titulo, "-",livro.autor, "(pertence à: ", livro.pertence, ")")
                print("\n")
        pausa()
        prosseguir()
        

    if (comando == "5"):
        espaco()
        for usuario in Minha_Biblioteca.usuarios:
            print(usuario.nome)

        u = input("Deseja obter informações de Qual Usuário? ")
        u = u.lower()

        for usuario in Minha_Biblioteca.usuarios:
            if (u == usuario.nome):
                espaco()
                print(vars(usuario))
                pausa()
                prosseguir()

    if (comando == "6"):
        #TEM QUE REVELAR O LIVRO E A QUEM PERTENCE
        print("=-"*11)
        print("lista de livros emprestados")
        print("=-"*11)

        for livro in Minha_Biblioteca.livros:
            if not livro.pertence == "":
                print(livro.titulo, " - ", "Pertence à: ", livro.pertence)


        d = input("Deseja devolver qual livro? ")

        for livro in Minha_Biblioteca.livros:
            ##Minha_Biblioteca.usuarios livro.pertence
            #eu preciso remover uma string específica, dentro de uma array de objetos, que está dentro de uma array de objetos, pesquisando pelo atributo nome
            #COMO EU FAÇO ISSOOOO???????
            #Dentro de Minha biblioteca existe uma array de usuários, dentro de cada usuário, uma array de livros, eu preciso acessar esses locais para ai sim excluir o livro
            if d == livro.titulo:
                buscar_nome = livro.pertence
                for p in Minha_Biblioteca.usuarios:
                    if p.nome == buscar_nome:
                        usuario_encontrado = p #Objeto adiquirido após a pesquisa pelo atributo nome

                usuario_encontrado.livros.remove(livro.titulo)
                livro.disponibilidade = "disponivel"
                livro.pertence = "" 
                print("O livro", livro.titulo, " foi devolvido com sucesso!")

    if (comando == "7"):
        break



