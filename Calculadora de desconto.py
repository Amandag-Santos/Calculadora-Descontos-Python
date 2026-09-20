
# Entrada de valor

valor_compra = float(input(" Digite um valor = "))

# Como não tem valor mínimo, deixei o valor de 0

if(valor_compra <= 0 ):
    print(" Valor inválido ")
else:
    
    if ( valor_compra < 200.00 ):
        print(f" Você tem 5% de desconto. O valor final é: {valor_compra - (valor_compra * 0.05)}")

    elif( valor_compra >= 200.00 and valor_compra < 300.00):
        print(f" Você tem 10% de desconto. O valor final é: {valor_compra - (valor_compra * 0.10)}")

    elif( valor_compra > 300.00 ):
        print(f" Você tem 15% de desconto. O valor final é: {valor_compra - (valor_compra * 0.15)}")





