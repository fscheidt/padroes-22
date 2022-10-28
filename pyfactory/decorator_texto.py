"""
O padrão Decorator permite adicionar 
dinamicamente novas funcionalidades 
(comportamento) a um "objeto" sem precisar 
alterar a sua implementação.
"""

class Texto:
    def __init__(self, conteudo ):
        self._texto = conteudo
    def exibir(self):
        return self._texto

class Italico(Texto):
    def exibir(self):
        return f"<i>{self._texto}</i>"
    
if __name__ == '__main__':
    # 1. texto simples (sem decorator)
    txt = Texto('frase do dia!')
    print(txt.exibir())

    # 2. decorator italico
    txt_italico = Italico(txt._texto)
    print(txt_italico.exibir())

    # 3. texto com dois decorators: 
    # Italico e Negrito
    # <b><i>frase do dia!</i></b>