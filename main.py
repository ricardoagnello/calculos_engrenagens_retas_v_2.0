import calculos as c

print("\n1 - Calculo diâmetro externo")
print("2 - Calculo do módulo")
print("3 - Calculo número de dentes")
opt = (input("\nDigite a opção desejada: "))

if(opt=='1'):
    m = float(input("\nDigite o módulo: "))
    z = int(input("Digite o número de dentes: "))
    d_ext = c.diametro_externo(m, z)
    
elif(opt=='2'):
    d_ext = float(input("\nDigite o diâmetro externo: "))
    z = float(input("Digite o número de dentes: "))
    m = c.modulo(d_ext, z)
    
    
elif(opt=='3'):
    d_ext = float(input("\nDigite o diâmetro externo: "))
    m = float(input("Digite o módulo: "))
    z = c.numero_de_dentes(d_ext, m)
    
else:
    print("\nOpção inválida")
    print("\n")