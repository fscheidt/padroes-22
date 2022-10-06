class NPC:
    # define o construtor:
    def __init__(self, nome, saude, forca):
        # inicializa os atributos:
        self.saude = saude
        self.forca = forca
        self.nome = nome
    def atacar(self):
        pass

class Dragao(NPC):
    def atacar(self):
        print(f'{self.nome} atacando com forca {self.forca}')

class Joker(NPC):
    def atacar(self):
        print(f'{self.nome} atacando com forca {self.forca}')

from enum import Enum
class NpcType(Enum): 
    DRAGAO = 1
    JOKER = 2
    ANFITRIAO = 3

class NpcFactory:
    @staticmethod
    def create(npc_type):
        if npc_type == NpcType.DRAGAO:
            return Dragao('dragao', 200, 30)
        if npc_type == NpcType.JOKER:
            return Joker('joker', 140, 20)

if __name__ == '__main__':
    '''
    dragao = Dragao('dragao', 200, 30)
    dragao.atacar()
    joker = Joker('joker', 140, 20)
    joker.atacar()
    '''
    npc = NpcFactory.create(NpcType.DRAGAO)
    npc.atacar()

    npc = NpcFactory.create(NpcType.JOKER)
    npc.atacar()