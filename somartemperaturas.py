def soma_temperaturas(temp1, escala1, temp2, escala2):
    if escala1.upper() == escala2.upper():
        soma = temp1 + temp2
        escala = escala1
    else:
        if escala1.upper() == 'C':
            temp1 = (9/5) * temp1 + 32
        else:
            temp1 = (5/9) * (temp1 - 32)
        if escala2.upper() == 'C':
            soma = temp1 + temp2
        else:
            temp2 = (5/9) * (temp2 - 32)
            soma = temp1 + (9/5) * temp2 + 32
        escala = escala2
    return soma, escala

temp1 = float(input())
escala1 = input().upper()[0]
temp2 = float(input())
escala2 = input().upper()[0]

soma, escala = soma_temperaturas(temp1, escala1, temp2, escala2)

print(f"({round(soma,4)}, '{escala}')")
