# Método Longo
'''
Vamos considerar um exemplo de um método longo que realiza várias tarefas. Em seguida, refatoraremos esse método para torná-lo mais conciso e modular:
'''

class Calculadora:
    def calcular_tudo(self, numeros):
        soma = 0
        produto = 1
        media = 0
        quantidade = len(numeros)

        for numero in numeros:
            soma += numero
            produto *= numero

        if quantidade > 0:
            media = soma / quantidade

        # Realizar mais cálculos complicados...
        resultado_final = soma * produto / (media + 1)

        return resultado_final


'''
Neste exemplo, calcular_tudo realiza várias operações diferentes, incluindo a soma, o produto, a média e outros cálculos mais complicados. Esse método longo pode ser difícil de entender e manter.

Vamos refatorar o código, dividindo as responsabilidades em métodos menores e mais específicos:
'''

# Código Após a Refatoração:
class Calculadora:
    def calcular_tudo(self, numeros):
        soma = self.calcular_soma(numeros)
        produto = self.calcular_produto(numeros)
        media = self.calcular_media(numeros)
        resultado_final = self.calcular_resultado_final(soma, produto, media)
        return resultado_final

    def calcular_soma(self, numeros):
        return sum(numeros)

    def calcular_produto(self, numeros):
        produto = 1        # Adicione mais tipos e operações conforme necessário

        for numero in numeros:
            produto *= numero
        return produto

    def calcular_media(self, numeros):
        quantidade = len(numeros)
        if quantidade > 0:
            return sum(numeros) / quantidade
        return 0  # Evitar divisão por zero

    def calcular_resultado_final(self, soma, produto, media):
        # Realizar mais cálculos complicados...
        resultado_final = soma * produto / (media + 1)
        return resultado_final
    
'''
Nesta refatoração, criamos métodos mais específicos (calcular_soma, calcular_produto, calcular_media, calcular_resultado_final) para realizar tarefas individuais. O método principal calcular_tudo agora chama esses métodos mais específicos, tornando o código mais legível, modular e fácil de entender. Cada método tem uma responsabilidade clara e pode ser testado separadamente.
'''
