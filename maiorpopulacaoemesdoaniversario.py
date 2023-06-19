def mes(m):
    m = int(m)
    meses = ('JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO')
    lista = meses[m-1].strip().lower()
    return lista

def carrega_cidades(lista,popu):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes_aniversario, pop = map(str.strip,linha.split(';'))
            if int(pop) > popu and mes(mes_aniversario) == mes(lista):
                resultado.append(
                    (nome,uf,int(pop),dia,mes_aniversario)
                    )
    arquivo.close()
    return resultado

lista = input()
popu = int(input())
cidades = carrega_cidades(lista,popu)
meis = mes(lista)
print(f"CIDADES COM MAIS DE {popu} HABITANTES E ANIVERSÁRIO EM {meis.upper()}:")
for cidade in cidades:
    print(f"{cidade[0]}({cidade[1]}) tem {cidade[2]} habitantes e faz aniversário em {cidade[3]} de {mes(cidade[4]).lower()}.")
