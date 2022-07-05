print("\n1 - Calculo diâmetro externo")
print("2 - Calculo do módulo")
print("3 - Calculo número de dentes")
opt = (input("\nDigite a opção desejada: "))

if(opt=='1'):
    m = float(input("\nDigite o módulo: "))
    z = int(input("Digite o número de dentes: "))
    d_ext = (z + 2) * m
    print(f"\nDiâmetro Externo: {d_ext:.2f}mm")
    print("\n")
    
elif(opt=='2'):
    d_ext = float(input("\nDigite o diâmetro externo: "))
    z = float(input("Digite o número de dentes: "))
    m = d_ext / (z + 2)
    print(f"\nMódulo: {m:.2f}")
    print("\n")
    
elif(opt=='3'):
    d_ext = float(input("\nDigite o diâmetro externo: "))
    m = float(input("Digite o módulo: "))
    z = (d_ext / m) - 2
    print(f"\nNúmero de dentes: {round(z)}")
    print("\n")
    
else:
    print("\nOpção inválida")
    print("\n")