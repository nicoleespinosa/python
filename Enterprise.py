dados1 = ['Adobe', '2012-11-01', 'e-mail, dicas de senha, senhas, nomes de usuário']
dados2 = ['Apollo', '2018-07-01',
          'e-mail, empregadores, localização, cargos, nomes, números de telegone, saudações, perfis de mídia social']
dados3 = ['Canva', '2019-05-01', 'e-mail, localização, nomes, senhas, nomes de usário']
dados4 = ['Facebook', '2019-11-01',
          'e-mail, empregados, localização, cargos, nomes, números de telefone, perfis de mídia social']
dados5 = ['Hurb', '2019-03-01',
          'datas de nascimento, e-mail, endereços IP, nomes, senhas, números de telefone, perfis de mídia social']

dados = [dados1, dados2, dados3, dados4, dados5]

datas = []
senhas = []
list = []
DatasOrdenas = []
listaFinal = []

for x in range(len(dados)):
    datas.append(dados[x][1])
datas.sort()
datas.reverse()

for x in range(len(dados)):
    for y in range(len(dados)):
        if [d for d in dados[y] if datas[x] in d]:
            list.append(y)

for x in range(len(dados)):
    DatasOrdenas.append(dados[list[x]])

for x in range(len(DatasOrdenas)):
    if [s for s in DatasOrdenas[x] if 'senhas' in s]:
        senhas.append(x)

for x in range(len(senhas)):
    listaFinal.append(DatasOrdenas[senhas[x]])

print(senhas)
print(DatasOrdenas)
print(listaFinal)
