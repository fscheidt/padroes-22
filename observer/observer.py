"""
The Observer 👀

Permite que um objeto notifique outros objetos na 
ocorrência de determinado evento.

Essa funcionalidade permite que objetos se inscrevam a 
certos eventos.

Envolvidos:
-  Subject: representa a entidade na qual os observadores estão interessados 
- Observer: representa todos os objetos que serao notificados quando o estado do Subject mudar

"""

from abc import ABC, abstractmethod

class Subject(ABC):
    """ Abstract subject """
    
    def inscrever(self, observer):
        pass

    def sair(self, observer):
        pass

    def notificar(self):
        pass

class Estoque(Subject):
    """ Observadores ficaram de olho no Estoque  """
    def __init__(self):
        self.produtos = []
        self.observadores = []

    def inscrever(self, observer):
        if observer not in self.observadores:
            self.observadores.append(observer)

    def sair(self, observer):
        if observer in self.observadores:
            self.observadores.remove(observer)

    def notificar(self):
        print(f"Notificando observadores: {len(self.observadores)}")
        for observer in self.observadores:
            # avisar a todos os inscritos que algo aconteceu
            observer.atualizar()

    def receber_produto(self, produto: str):
        # gatilho - aqui acontece o evento
        # Um novo produto chegou, atualizar o estoque
        print("="*40)
        print(f"[Evento] Um novo produto chegou: {produto}")
        self.produtos.append(produto)
        self.notificar()

class Observer(ABC):
    """ Abstract Observer """
    def atualizar(self):
        pass

class Usuario(Observer):

    def __init__(self, nome, produto=None, subject=None):
        self.nome = nome
        # eh o produto que esta falta e o usuario
        # esta interassado em ser noticiado
        self.produto = produto # "Teclado Z" (joana)
        # estoque:
        self.subject = subject
        if self.subject:
            self.subject.inscrever(self)

    def atualizar(self):
        # SE true produto ja esta no estoque:
        if self.produto in self.subject.produtos:
            print(f"[Usuario] {self.nome} notificada")
            print(f"\tO produto {self.produto} esta disponivel")

            # sair da lista de observador (usuario ja foi notificado)
            self.subject.sair(self)


if __name__ == '__main__':
    print('Observer - Notificação de produtos')
    estoque = Estoque()
    joana = Usuario("Joana", "Teclado Z", subject=estoque)
    joao = Usuario("Joao", "Teclado B", subject=estoque)

    estoque.receber_produto("Teclado A")
    estoque.receber_produto("Teclado Z")
    estoque.receber_produto("Teclado B")
    estoque.receber_produto("Teclado A")