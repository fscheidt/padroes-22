"""
Abrir documento/arquivo
"""

class OpenStrategy:
    @staticmethod
    def abrir(arquivo: str):
        # Qual a estrategia (funcao) necessaria para abrir
        # esse ???
        if arquivo.endswith('.pdf'):
            # Acrobat.open(arquivo)
            Foxit.open(arquivo)
        if arquivo.endswith('.md'):
            Browser.open(arquivo)
        if arquivo.endswith('.mp4'):
            VLC.open(arquivo)
        else:
            print('throw new Exeception()')
        



class ListView:
    @staticmethod
    def visualizar(self, arquivo):
        # abrir e visualizar
        pass

    @staticmethod
    def open(arquivo):
        # chama o acrobat...
        # print(f'abrindo {arquivo} no acrobat')
        OpenStrategy.abrir(arquivo)


if __name__ == '__main__':

    # evento abrir arquivo onTap
    # retornou o nome do arquivo escolhido
    # pelo usuario
    # arquivo = "slide.pdf"
    # arquivo = "README.md"
    arquivo = "videoaula.mp4"
    # acrobatReader, browser, ...
    ListView.open(arquivo)


