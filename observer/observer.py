"""
The Observer 👀

Permite que um objeto notifique outros objetos na ocorrência de determinado evento.
Essa funcionalidade permite que objetos se inscrevam a certos eventos.

Envolvidos:
-  Subject: representa a entidade na qual os observadores estão interessados 
- Observer: representa todos os objetos que serao notificados quando o estado do Subject mudar

"""

from abc import ABC, abstractmethod

class Subject(ABC):
    """ Abstract subject """
    pass

class Observer(ABC):
    """ Abstract Observer """
    pass


if __name__ == '__main__':
    print('Observer')
