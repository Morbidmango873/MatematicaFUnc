# Defina as funções f(x) e g(x)

def f(x):
    return x**2+1


def g(x):
    return 2*x-3


# Função para calcular a composição (g ° f)
def g_para_f(x):
    return g(f(x))

# (3^2)-1 = 8

# Função para calcular a composição (g ° g)
def g_para_g(x):
    return g(g(x))

#  (3-1)-1 = 1

# Função para calcular a composição (f ° f)
def f_para_f(x):
    return f(f(x))

# (3^2)^2 = (9)^2 = 81

# Função para calcular a composição (f ° g)
def f_para_g(x):
    return f(g(x))


# (3-1)^2 = 4

# Teste com alguns valores
x = int(input("Coloque um valor para X: "))


# Exiba os resultados
print("(g ° f) (",(x),")=", g_para_f(x))
print("(g ° g) (",(x),")=", g_para_g(x))
print("(f ° f) (",(x),")=", f_para_f(x))
print("(f ° g) (",(x),")=", f_para_g(x))





