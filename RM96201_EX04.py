# Nicole Espinosa, RM:96201
minuto = int(input("Escreva o minuto atual: "))

resultado = 1
count = 1

while count <= minuto:
    resultado *= count
    count += 1

print('A senha é LIBERDADE{}'.format(resultado))
