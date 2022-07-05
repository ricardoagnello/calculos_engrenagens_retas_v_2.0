def diametro_externo(m, z):
    d_ext = m * (z+2)
    print(f"\nDiâmetro Externo: {d_ext:.2f}mm")
    print("\n")
    
def modulo(d_ext, z):
    m = d_ext / (z + 2)
    print(f"\nMódulo: {m:.2f}")
    print("\n")
    
def numero_de_dentes(d_ext, m):
    z = (d_ext / m) - 2
    print(f"\nNúmero de dentes: {round(z)}")
    print("\n")