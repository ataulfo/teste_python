
''' Inicialização das variáveis'''
status = 1
b = []
J =  {1:12, 1:34, 3:67}
 
''''Começo do código '''

while status != 0:       
      a = int(input('Digite um numero: '))
      b.append(a)
      status = int(input('Deseja continuar digite 1, para sair 0: '))

if status == 0:
    for c in b:
        print('\nValores adicionados ',c)
        print('As chaves são ',str(J[1]))

