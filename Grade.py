# Nicole Espinosa, RM:96201
# variaveis para armazenar notas
n_impar = 0.0
n_par = 0.0

print('Bem-vindo(a)!')
# loop
print('Digite a nota dos alunos ÍMPARES')
for im in range(1, 50, 2):
    nota_impar = float(input('Informe a nota do aluno {}: '.format(im)))
    print('Você está digitando a nota dos alunos ÍMPARES')

    # media 1
    n_impar = n_impar + nota_impar

print('\nCerto, agora digite a nota dos alunos PARES')

# loop 2
for pa in range(2, 51, 2):
    nota_par = float(input('Informe a nota do aluno {}: '.format(pa)))
    print('Você está digitando a nota dos alunos PARES')

    # media 2
    n_par = n_par + nota_par

# calculo da media 1
media1 = n_impar / 25

# calculo da media 2
media2 = n_par / 25

# exibição dos resultados
if media1 > media2:
    print('\nA média dos alunos ÍMPARES foi a maior, apresentando {} de média.'.format(media1))
elif media1 < media2:
    print('\nA média dos alunos PARES foi a maior, apresentando {} de média.'.format(media2))
else:
    print('\nNão foi possível calcular a média dos alunos.')
