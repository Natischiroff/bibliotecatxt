# Sistema de biblioteca console
class Livro:
   def __init__(self,titulo,autor):
    #Privar os dados
    self.__titulo = titulo
    self.__autor = autor

    def exibir(self):
       print("Título:",self.__titulo)
       print("Autor:",self.__autor)

        #getter-> permite acessasr o título
    @property
    def titulo(self):
       return self.__titulo
    #setter -> permite alterar o titulo 
    @titulo.setter
    def titulo(self, novo_titulo):
       if len(novo_titulo) < 2:
          print("Título muito curto")
       else:
          self.__titulo = novo_titulo


livros = []


while True:
    print("\n ====Sistema de Biblioteca====")
    print("1- Cadastrar Livro ")
    print("2- Listar Livros ")
    print("3- Listar Livros ")
    print("4- Sair ")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor:")


        livro = livro(titulo,autor)
        livros.append(livro)

        ano = input("Digite o ano do livro:")
        arquivo = open("livros.txt", "r")
        arquivo.write(livro.titulo + "- "+ livro.autor+"\n")
        arquivo.close()

        print("Livro cadastrado!")

    elif opcao == "2":
        arquivo = open("livros.txt","r")
        livros = arquivo.readlines()
        print("\n === Livros Cadastrados ===")

        for livro in livros:
         print(livro.strip())



        arquivo.close()

  
 #Sair
    elif opcao =="3":
       print("Encerrando o sistema...")
       break
    else:
       print("Opção inválida")