'''try:
    numero = eval(input("Digite um número: "))
    print(numero)
except:
    print("Seu burro! é número seu jumento: ")
    numero = eval(input("Digite um número: "))
    print(numero)'''

'''try:
    numero = eval(input("Entre com um número inteiro: "))
    print(numero)
except NameError:
    print("Somente número")'''

try:
    numero = eval(input("Número: "))
    print(numero)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")
''''''''''''''''''''''''''''''''
'''O tratamento completo das exceções
A forma geral completa para lidar com as exceções em Python é:'''

