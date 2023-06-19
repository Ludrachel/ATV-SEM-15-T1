def mees(l):
    meses = ('JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO','AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO')
    lista = meses[l - 1]
    return lista
    
def carrega_cidades(d,m):
    resultado = []
    
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            dia = int(dia)
            mes = int(mes)
            if d == dia and m == mes:
                resultado.append(
                (uf, nome)
            )
    arquivo.close()
    return resultado

dia = int(input())
mes = int(input())
cidades = carrega_cidades(dia,mes)
mes = mees(mes)
print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes}:')
for cidade in cidades:
    print(f'{cidade[1]}({cidade[0]})')





