def converter_temperatura(temp , escala_inicial , escala_destino):
    if escala_inicial.upper() == 'C' and escala_destino.upper() == 'F':
        return (9/5) * temp + 32
    elif escala_inicial.upper() == 'F' and escala_destino.upper() == 'C':
        return (5/9) * (temp - 32)
    else:
        return temp

def maior_temperatura(temp1, escala1, temp2, escala2):
    temp1_convertida = converter_temperatura(temp1, escala1, 'C')
    temp2_convertida = converter_temperatura(temp2, escala2, 'C')
    if temp1_convertida > temp2_convertida:
        return temp1, escala1
    elif temp2_convertida > temp1_convertida:
        return temp2, escala2
    else:
        return temp1, escala1

temp1 = float(input())
escala1 = input().upper()[0]
temp2 = float(input())
escala2 = input().upper()[0]

maior_temp , maior_escala = maior_temperatura(temp1, escala1, temp2, escala2)

print(f"({round(maior_temp,4)}, '{maior_escala}')")
