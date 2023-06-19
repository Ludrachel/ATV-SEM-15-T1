
def popu(p):
    lis = []
    pop = lis[p-1]
    return pop



def carrega_cidades(populacao):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            populashion = int(input())
            if populacao < populashion:
                resultado.append(
                    (uf, nome, pop)
                    )
            
    arquivo.close()
    return resultado




def main ():
    populashion = int(input())
    popul = carrega_cidades(populashion)
    populashion = popu(populashion)
    print(f'CIDADES COM MAIS DE {populashion} HABITANTES')
    for cidade in cidades:
        print(f'IBGE: {ibge} - {cidade[1]}({cidade[0]}) - POPULAÇÃO: {POP}')

if __name__== '__main__':
    main()


