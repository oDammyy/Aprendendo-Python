#TABUADA + CALCULADORA (START: 8:35, END: 9:43) 31/03/2026
i = input("escolha o seu utilitario (TABUADA/CALCULADORA): ")

if i == "TABUADA":
    print("TABUADA INICIADA COM SUCESSO")
    escolha_tabuada = input("Deseja a TABUADA INTEIRA ou um NUMERO especifico?")
    if escolha_tabuada == "NUMERO":
        numero3 = int(input("Digite o numero que deseja calcular:"))
        for multiplicador in range(1,11):
            resultado = numero3 * multiplicador
            print(f"{numero3} x {multiplicador} = {resultado}")
    elif escolha_tabuada == "INTEIRA":
        for n_tabuada in range(1,11):
            print(f"TABUADA DO {n_tabuada}")
            for multiplicador in range(1,11):
                print(f"{n_tabuada} x {multiplicador} = {n_tabuada * multiplicador}")
            print("-" * 20)
elif i == "CALCULADORA":
    print("CALCULADORA INICIADA COM SUCESSO")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print("escolha o operador: +, - *, /")
    operacao = input()
    
    if operacao == "+":
        print(numero1 + numero2)
    elif operacao == "-":
        print(numero1 - numero2)
    elif operacao == "*":
        print(numero1 * numero2)
    elif operacao == "/":
        print(numero1 / numero2)
    else:
        print("Operador invalido!")

else:
    print("opção invalida")
