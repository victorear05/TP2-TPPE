# Código Duplicado
'''
Vamos considerar um exemplo de código duplicado relacionado à formatação de datas. Suponha que você tenha duas funções que fazem a mesma coisa, mas para formatos de data diferentes:
'''

import datetime

def formatar_data_para_usuario(data):
    return f"{data.day:02d}/{data.month:02d}/{data.year}"

def formatar_data_para_arquivo(data):
    return f"{data.year}-{data.month:02d}-{data.day:02d}"

# Chamadas das funções
data1 = datetime.date(2023, 1, 15)
data2 = datetime.date(2023, 3, 22)

data_formatada_usuario = formatar_data_para_usuario(data1)
data_formatada_arquivo = formatar_data_para_arquivo(data2)

print("Data formatada para usuário:", data_formatada_usuario)
print("Data formatada para arquivo:", data_formatada_arquivo)


'''
Neste exemplo, as funções formatar_data_para_usuario e formatar_data_para_arquivo têm lógica semelhante, mas formatam a data de maneiras diferentes. Isso pode ser considerado código duplicado, pois ambas as funções realizam a mesma tarefa básica (formatação de data) com variações mínimas.

A refatoração poderia envolver a criação de uma única função mais genérica que aceita um formato como parâmetro:
'''

# Código Após a Refatoração:
def formatar_data(data, formato):
    if formato == "usuario":
        return f"{data.day:02d}/{data.month:02d}/{data.year}"
    elif formato == "arquivo":
        return f"{data.year}-{data.month:02d}-{data.day:02d}"
    else:
        raise ValueError("Formato de data não suportado")

# Chamadas da função
data1 = datetime.date(2023, 1, 15)
data2 = datetime.date(2023, 3, 22)

data_formatada_usuario = formatar_data(data1, "usuario")
data_formatada_arquivo = formatar_data(data2, "arquivo")

print("Data formatada para usuário:", data_formatada_usuario)
print("Data formatada para arquivo:", data_formatada_arquivo)

'''
Essa refatoração elimina a duplicação, pois agora temos uma única função formatar_data que pode ser utilizada para diferentes formatos, evitando repetir a lógica de formatação.
'''