import time
from statistics import mean
def escrever(texto):
    for I in texto:
        print(I, end="", flush= True)
        time.sleep(0.05)

q0 = None


def maior(self):
    return max(self)

def menor(self):
    return min(self)

def media(self):
    for i in range(1, len(self)):
        return mean(self)
    
def notas(self):
    for (self, item) in enumerate(self, start=1):
        print(self, item)

def soma(x, y):
    return (x + y)

def sub(x, y):
    return (x - y)

def div(x, y):
    return (x / y)

def multi(x, y):
    return(x * y)

def multiplo(x,y):
    if x % y == 0:
        return True
    else:
        return False
    
def areatri(x,y):
    return ((x * y)/2)

q1 = '''
def menu():
    while True:
        escrever("1 - Trocar o valor de uma nota\n2 - Média da turma\n3 - Menor nota\n4 - Maior nota\n5 - Mostrar notas")
        q1r = int(input("\nR: "))
        if q1r == 1:
            notas(q1l)
            q1in = int(input("Escolha qual nota quer trocar: "))
            q1l[q1in - 1] = int(input("Nota: "))
        elif q1r == 2:
            print(media(q1l))
        elif q1r == 3:
            print(menor(q1l))
        elif q1r == 4:
            print(maior(q1l))
        elif q1r == 5:
            notas(q1l)
        else:
            print("Resposta inválida")

q1la = input("Mim dê 10 notas: ")
q1l = list(map(int, q1la.split()))
menu()'''


q2 = '''
def que(q2s, q2i, q2l):
    print(q2s, q2i, q2l)

q2s = input("Mim dê uma palavra: ")
q2i = int(input("Mim dê um número: "))
q2la = input("Mim dê vários números: ")
q2l = list(map(int, q2la.split()))
que(q2s, q2i, q2l)'''


q3 = '''
def menor2(x,y):
    return min(x,y)

q3n1 = int(input("Mim dê um número: "))
q3n2 = int(input("Mim dê outro número: "))
if q3n1 != q3n2:
    print(menor2(q3n1, q3n2))
else:
    print("Os dois são iguais")
print(soma(q3n1, q3n2))
print(sub(q3n1, q3n2))
print(multi(q3n1, q3n2))
print(div(q3n1, q3n2))'''


q4 = '''
def notausa(nota):
    if nota == 10:
        return("A")
    elif nota >= 8:
        return("B")
    elif nota >= 6:
        return("C")
    elif nota >= 4:
        return("E")
    elif nota >= 0:
        return("F")
    
nota = int(input("Mim dê sua nota: "))
print(f"Sua nota é: {notausa(nota)}")'''


q5 = '''
q5n1 = int(input("Mim dê um valor: "))
q5n2 = int(input("Mim dê outro valor: "))
print(multiplo(q5n1, q5n2))'''

q6= '''
def escada(q6n):
    q6ii = 0
    for q6i in range(0, q6n):
        q6ii += 1
        print(q6ii)
        for q6i in range(0, q6ii):
            print(q6i + 1, end=" ")
    print(end='\r')


q6n = int(input("Mim dê um número: "))
escada(q6n)'''


q7 = '''
def menu():
    while True:
        escrever("1 - Botar as notas\n2 - Mostrar notas\n3 - Média das notas")
        q7r = int(input("\nR: "))
        if q7r == 1:
            q7la = input("Mim dê 4 notas: ")
            q7l = list(map(int, q7la.split()))
        elif q7r == 2:
            notas(q7l)
        elif q7r == 3:
            print(media(q7l))
        else:
            print("Resposta inválida")
menu()'''


q8 = '''
q8n1 = int(input("Mim dê a base: "))
q8n2 = int(input("Mim dê o lado: "))
print(areatri(q8n1, q8n2))'''


q9 = '''
def caracterlimit(x,y,z):
    if len(x) >= y and len(x) <= z:
        return True
    else: 
        return False
    
q9min = int(input("Mim dê uma um limite mínimo de caracteres: "))
q9max = int(input("Mim dê uma um limite máximo de caracteres: "))
q9s = input("Mim dê uma frase: ")
print(caracterlimit(q9s, q9min, q9max))
print(len(q9s))'''

q10 = '''
def countlista(x, y):
    if x.count(y) != 0:
        return True
    else:
        return False

q10l = ["banana","strogonoff","arroz","lasanha","jaca","pêra","macarrão","salada","pitaya","caju","maçã","feijão"]
q10s = input("Mim dê um nome de comida: ")
print(countlista(q10l, q10s))'''

