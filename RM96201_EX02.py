# Nicole Espinosa, RM:96201
print('Olá! Por favor, digite a quantidade de votos para cada dia da semana!')
dia1 = int(input('\nQuantos votos teve SEGUNDA-FEIRA? '))
dia2 = int(input('Quantos votos teve TERÇA-FEIRA? '))
dia3 = int(input('Quantos votos teve QUARTA-FEIRA? '))
dia4 = int(input('Quantos votos teve QUINTA-FEIRA? '))
dia5 = int(input('Quantos votos teve SEXTA-FEIRA? '))

print('\nSegunda-feira obteve {} votos | Terça-feira obteve {} votos \nQuarta-feira obteve {} votos | Quinta-feira'
      'obteve {} votos \nSexta-feira obteve {} votos.'.format(dia1, dia2, dia3, dia4, dia5))
if dia1 > dia2 and dia1 > dia3 and dia1 > dia4 and dia1 > dia5:
    print('\nO dia mais votado foi SEGUNDA-FEIRA.')

elif dia2 > dia1 and dia2 > dia3 and dia2 > dia4 and dia2 > dia5:
    print('\nO dia mais votado foi TERÇA-FEIRA.')

elif dia3 > dia1 and dia3 > dia2 and dia3 > dia4 and dia3 > dia5:
    print('\nO dia mais votado foi QUARTA-FEIRA.')

elif dia4 > dia1 and dia4 > dia2 and dia4 > dia3 and dia4 > dia5:
    print('\nO dia mais votado foi QUINTA-FEIRA.')

elif dia5 > dia1 and dia5 > dia2 and dia5 > dia3 and dia5 > dia4:
    print('\nO dia mais votado foi SEXTA-FEIRA.')

else:
    print('\nNão foi possível contabilizar os votos.')
