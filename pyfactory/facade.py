# 1. facade 
# 2. decorator
# 3. trabalho da disciplina

# --------------------------------

"""
FACADE = Fachada
Fornecer uma única interface para um sistema 
complexo.
Complexo == requer múltiplas classes para 
inicializar um componente.
"""

class CPU:
    def __init__(self):
        pass
    def ligar(self):
        print('iniciando cpu...')

class Memoria:
    def __init__(self):
        pass
    def inicializar(self):
        print('init ram')

class SSD:
    def __init__(self):
        pass
    def ler_arquivos_boot(self):
        print('reading boot files...')

class ComputadorFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.ssd = SSD()

    def ligar(self):
        self.cpu.ligar()
        self.memoria.inicializar()
        self.ssd.ler_arquivos_boot()

if __name__ == '__main__':

    fachada = ComputadorFacade()
    fachada.ligar()

    # ligar a cpu
    # cpu.ligar()
    # inicialiar a ram
    # memoria.inicializar()
    # ler alguns arquivos do ssd
    # ssd.ler_arquivos_boot()

