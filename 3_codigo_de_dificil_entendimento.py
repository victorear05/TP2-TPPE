# Código de Difícil Entendimento
'''
Vamos considerar um exemplo de código difícil de entender, onde a lógica é obscura e os nomes de variáveis não são descritivos o suficiente:
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
Neste exemplo, é difícil entender a finalidade do código devido aos nomes de variáveis pouco descritivos (a, b, c, d, etc.) e à lógica obscura. O que esse código faz não está claro à primeira vista, tornando a manutenção e a compreensão do código desafiadoras.
Vamos refatorar o código, tornando os nomes de variáveis mais descritivos e dividindo a lógica em funções mais compreensíveis:
'''

# Código Após a Refatoração:
def verificar_media_dos_pares(lista_numeros, multiplicador):
    numeros_pares_multiplicados = calcular_pares_multiplicados(lista_numeros, multiplicador)
    media_pares = calcular_media(numeros_pares_multiplicados)
    
    return media_pares > 10

def calcular_pares_multiplicados(lista_numeros, multiplicador):
    pares_multiplicados = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            resultado_multiplicacao = numero * multiplicador
            pares_multiplicados.append(resultado_multiplicacao)
    
    return pares_multiplicados

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

# Exemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplicador = 3

resultado = verificar_media_dos_pares(lista_numeros, multiplicador)
print(resultado)

'''
Nesta refatoração, introduzimos funções com nomes mais descritivos, tornando a lógica mais clara e a intenção do código mais compreensível. Agora, o código é mais legível e modular, facilitando a manutenção e compreensão.
'''
