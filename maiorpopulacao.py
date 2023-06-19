def carrega_cidades(popu):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            pop = int(pop)
            if popu <= pop:
                resultado.append(
                    (uf,int(ibge),nome,pop)
                    )
    arquivo.close()
    return resultado

pop = int(input())
cidades = carrega_cidades(pop)
print(f"CIDADES COM MAIS DE {pop} HABITANTES:")
for cidade in cidades:
    print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[3]}")

