import time
from statistics import mean
def escrever(texto):
    for I in texto:
        print(I, end="", flush= True)
        time.sleep(0.05)

q0 = None


def maior(q1l):
    return max(q1l)

def menor(q1l):
    return min(q1l)

def media(q1l):
    for q1i in range(1, len(q1l)):
        return mean(q1l)


def menu():
    while True:
        escrever("1 - Trocar o valor de uma nota\n2 - Média da turma\n3 - Menor nota\n4 - Maior nota")
        q1r = int(input("\nR: "))
        if q1r == 1:
            for q1i in range(1, len(q1l)):
                print(q1i, q1l[q1i])
            q1in = int(input("Escolha qual nota quer trocar: "))
            q1l[q1in] = int(input("Nota: "))
        elif q1r == 2:
            print(media(q1l))
        elif q1r == 3:
            print(menor(q1l))
        elif q1r == 4:
            print(maior(q1l))
        else:
            print("Resposta inválida")

q1la = input("Mim dê 10 notas: ")
q1l = [0, list(map(int, q1la.split()))]
menu()