# Dependência Cíclica
'''
A dependência cíclica ocorre quando há uma cadeia de dependências entre duas ou mais classes de forma circular, o que pode tornar o código mais difícil de entender e manter. Vamos considerar um exemplo simplificado:
'''

# Classe A depende de B
class A:
    def __init__(self, instancia_b):
        self.b = instancia_b

    def metodo_a(self):
        print("Método A")
        self.b.metodo_b()

# Classe B depende de C
class B:
    def __init__(self, instancia_c):
        self.c = instancia_c

    def metodo_b(self):
        print("Método B")
        self.c.metodo_c()

# Classe C depende de A
class C:
    def __init__(self, instancia_a):
        self.a = instancia_a

    def metodo_c(self):
        print("Método C")
        self.a.metodo_a()

# Criar instâncias
instancia_c = C(None)
instancia_b = B(instancia_c)
instancia_a = A(instancia_b)

# Atualizar referências cruzadas
instancia_c.a = instancia_a
instancia_b.c = instancia_c


'''
Neste exemplo, temos uma dependência cíclica onde a Classe A depende da Classe B, que depende da Classe C, que por sua vez depende novamente da Classe A.
Uma maneira comum de resolver a dependência cíclica é utilizar injeção de dependência ou postergar a resolução da dependência para o momento em que ela é realmente necessária. Aqui está um exemplo de como isso pode ser feito:
'''

# Código Após a Refatoração:
class A:
    def __init__(self):
        pass

    def set_dependencia_b(self, instancia_b):
        self.b = instancia_b

    def metodo_a(self):
        print("Método A")
        self.b.metodo_b()

class B:
    def __init__(self):
        pass

    def set_dependencia_c(self, instancia_c):
        self.c = instancia_c

    def metodo_b(self):
        print("Método B")
        self.c.metodo_c()

class C:
    def __init__(self):
        pass

    def set_dependencia_a(self, instancia_a):
        self.a = instancia_a

    def metodo_c(self):
        print("Método C")
        self.a.metodo_a()

# Criar instâncias
instancia_c = C()
instancia_b = B()
instancia_a = A()

# Atualizar referências cruzadas
instancia_c.set_dependencia_a(instancia_a)
instancia_b.set_dependencia_c(instancia_c)
instancia_a.set_dependencia_b(instancia_b)

'''
Nesta refatoração, removemos as dependências iniciais no momento da criação das instâncias. Em vez disso, utilizamos métodos set_dependencia_X para estabelecer as dependências posteriormente. Isso resolve a dependência cíclica e permite uma inicialização mais flexível das classes.
'''
