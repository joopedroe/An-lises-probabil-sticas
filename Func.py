from fractions import Fraction
import itertools
import random
from math import factorial

A = {1, 2, 3, 4, 5, 6}
par = '{2, 4, 6}'
x={1,2,3,4,5,6,7,8}
#-----------------------------------------------------------------#
def P(evento , espaco):
    "A probabilidade de um `evento `, dado o `espaco ` amostral evento pode ser um conjunto ou predicado"
    if callable(evento):
        evento=tal_que(evento, espaco)
    return Fraction(len(evento & espaco), len(espaco))
#-----------------------------------------------------------------#
def tal_que(predicado,colecao):
    "O subconjunto de elementos da colecao para os quais o predicado  é verdadeiro"
    return{e for e in colecao if predicado(e)}

#-----------------------------------------------------------------#
def eh_par(n):
    return n% 2==0
'''print(P(eh_par,A))
print(P(par,A))'''

#len(evento & espaço) pega o tamanho da interseção entre evento e espaço
#-----------------------------------------------------------------#
def cross(A, B):
    "O conjunto de formas de concatenar os itens de A e B (produto cartesiano)"
    return {a + b
        for a in A for b in B
        }

urna = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
# O pipe | representa a união entre os elementos
#-----------------------------------------------------------------#
def combos(items, n):
    "Todas as combinações de n itens; cada combinação concatenada em uma string"
    
    return{' '.join(combo) 
           
            for combo in itertools.combinations(items, n)
    
           }
U6 = combos(urna,6)
#-----------------------------------------------------------------#
def escolha(n,c):
    "Número de formas de escolher c itens de uma lista com n itens"
    return factorial(n)//(factorial(c)*factorial(n-c))

## o // é divisão inteira
#-----------------------------------------------------------------#




'''red6 = {s for s in U6 if s.count('R')==6}
prob_red6 = P(red6, U6)
b3w2r1={s for s in U6 if s.count('B')==3 and s.count('W')==2 and s.count('R')==1}
prob_b3w2r1 = P(b3w2r1, U6)
P(b3w2r1 , U6) == Fraction(escolha(6, 3) * escolha(8, 2) * escolha(9, 1),
len(U6))

Espaco = {(1,2,3),(1),(2),(3),(4),(1,3),(2,3), (1,4), (2,4)}
ev = {(1,2,3),(1,3)}
print(P(ev,Espaco))

def clicou3ou4(a):
    print(a)
    return a[0]==(1) and a[-1]==(3)
print(P(clicou3ou4,A))

def ver(lista):
    for i in lista:'''
        

a=cross('C','1')|cross('D','12')|cross('P','1')|cross('A','1')|cross('Y','12345')|cross('X','12345')|cross('Z','12345')|cross('M','1')
# C = Carrinho, D = Dropdown, P = Perfil, A = Altera senha, Y, X e Z = Produtos,  M = Mais produtos
# Números = possibilidades de acesso
com=[]
cont=0
for i in range(1):
    f=combos(a,5)
    aux=combos(a,i+1)
    for j in f:
        h=j.split(' ')
        if '1' in h[0]:
            if 'A' in h[0] or 'P' in h[0]:
                pass
            else:
                if 'M' in h[0] and len(h) > 1:
                    pass
                else:
                    if len(h) < 2:
                        if 'D' in h[0]:
                            cont+=1
                            print(j)
                    elif len(h) > 1:
                        if '1' in  h[1] or '2' in h[1]:
                            if 'D' in h[0]:
                                cont+=1
                                print(j)
                


            '''if 'P' == j[0] or 'A' == j[0]:
                k='11'
            else:
                
                if len(j) < 3:
                    com.append(j)
                if len(j) > 2:
                    
                    if 'C' == j[0] or 'M' == j[0]:
                        k='1'
                    else:
                        
                        com.append(j)



            if 'P' == o[0] or 'A' == o[0]:
                aux.remove(j)
            else:
                if i == 0:
                    if 'P' == o[0] or 'A' == o[0]:
                        print('------')
                    else:
                        print(o) 
                if 'iP1i' in o or 'iA1i' in o or 'iC1i' in o or 'iM1i' in o or  'C1i' in o or 'M1i' in o:
                    k='1'
                else:
                    print(o)


                elif 'P1 ' in j or 'A1 ' in j or 'C1 ' in j or 'M1 ' in j:
                    k='1'
                elif ' P1 ' in j or ' A1 ' in j or ' C1 ' in j or ' M1 ' in j:
                    k='1'
                else:
                   print(j)'''


                
        '''c=j.split(' ')
        print(j)
        if len(c)== 1 and '1' in c[0]:
            com.append(j)
        elif '1' in c[0]:
            if 'P' in c[-1] or 'A' in c[-1] or 'C' in c[-1] or 'M' in c[-1]:
                com.append(j)'''

print(cont)
       

