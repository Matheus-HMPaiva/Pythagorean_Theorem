import math

def calcular_terceiro_lado():
    print("Escolha quais lados do triângulo você possui:")
    print("1. Cateto 1 e Cateto 2")
    print("2. Cateto e Hipotenusa")
    escolha = int(input("Digite o número correspondente à sua escolha (1 ou 2): "))

    if escolha == 1:
        cateto1 = float(input("Digite o valor do primeiro cateto: "))
        cateto2 = float(input("Digite o valor do segundo cateto: "))
        hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
        print(f"A hipotenusa do triângulo é: {hipotenusa:.2f}")
    elif escolha == 2:
        cateto = float(input("Digite o valor do cateto: "))
        hipotenusa = float(input("Digite o valor da hipotenusa: "))
        if hipotenusa <= cateto:
            print("A hipotenusa deve ser maior que o cateto. Tente novamente.")
        else:
            cateto2 = math.sqrt(hipotenusa**2 - cateto**2)
            print(f"O valor do outro cateto é: {cateto2:.2f}")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    calcular_terceiro_lado()
