# Switches Longos
'''
Vamos considerar um exemplo de uso excessivo de instruções switch ou case, que pode tornar o código difícil de entender e de dar manutenção:
'''

def processar_dados(tipo, dados):
    resultado = None

    if tipo == 'A':
        resultado = realizar_operacao_a(dados)
    elif tipo == 'B':
        resultado = realizar_operacao_b(dados)
    elif tipo == 'C':
        resultado = realizar_operacao_c(dados)
    elif tipo == 'D':
        resultado = realizar_operacao_d(dados)

    return resultado

def realizar_operacao_a(dados):
    # Lógica específica para o tipo 'A'
    return dados + 1

def realizar_operacao_b(dados):
    # Lógica específica para o tipo 'B'
    return dados * 2

def realizar_operacao_c(dados):
    # Lógica específica para o tipo 'C'
    return dados - 3

def realizar_operacao_d(dados):
    # Lógica específica para o tipo 'D'
    return dados ** 2


'''
Neste exemplo, o código utiliza uma série de instruções if-elif-else para determinar qual operação realizar com base no tipo. Esse padrão pode se tornar difícil de manter conforme novos tipos são adicionados, e a lógica para cada tipo cresce.
Podemos refatorar esse código usando um dicionário para mapear tipos para funções, evitando assim um longo bloco de instruções switch. Cada tipo terá uma função associada que realiza a operação específica:
'''

# Código Após a Refatoração:
def processar_dados(tipo, dados):
    operacoes = {
        'A': realizar_operacao_a,
        'B': realizar_operacao_b,
        'C': realizar_operacao_c,
        'D': realizar_operacao_d,
    }

    if tipo in operacoes:
        return operacoes[tipo](dados)
    else:
        raise ValueError(f'Tipo não suportado: {tipo}')

def realizar_operacao_a(dados):
    return dados + 1

def realizar_operacao_b(dados):
    return dados * 2

def realizar_operacao_c(dados):
    return dados - 3

def realizar_operacao_d(dados):
    return dados ** 2

'''
Essa abordagem usa um dicionário para mapear tipos para funções, tornando o código mais flexível e extensível. Adicionar novos tipos ou modificar o comportamento para um tipo existente agora é mais simples, pois as operações específicas são isoladas em funções separadas.
'''
