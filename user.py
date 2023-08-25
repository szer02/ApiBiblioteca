class Usuario:

    usuarios_cadastrados = []#

    def __init__(self, nome, login, senha, tipo, email, telefone):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.tipo = tipo
        self.email = email
        self.telefone = telefone
        Usuario.usuarios_cadastrados.append(self) #

    def cadastrar_usuario(self, info):
        #tinha um user = '' aqui
        for usuario in Usuario.usuarios_cadastrados:
            if usuario.nome == self.nome:  #era user
                return print(f'usuario {self.nome}, já cadastrado.')
            
            Usuario.usuarios_cadastrados.append(self)#
            return print(f'Usuario {self.nome}, Cadastrado com sucesso.')


    def consultar_usuario(self, info):
        for usuario in Usuario.usuarios_cadastrados:
           return print(usuario.nome)
    
    def alterar_usuario(self, info):
        pass