from operacoes import Operacoes

def main():
    print("Calculadora")

    operacao = Operacoes()

    op = int(input("""Digite 1 para realizar uma soma de 2 números\n
            Digite 2 para realizar uma subtração de 2 números\n
            Digite 3 para realizar uma multiplicação de 2 números\n
            Digite 4 para realizar uma divisão de 2 números: \n"""))
    if (op == 1):
        num1 = int(input("Digite o primeiro número para calcular: "))
        num2 = int(input("Digite o segundo número para calcular: "))
        #operacao = Operacoes()
        resultado = operacao.soma(num1, num2)
        print("Resultado da soma: ", resultado)
        
    if (op == 2):
        num1 = int(input("Digite o primeiro número para calcular: "))
        num2 = int(input("Digite o segundo número para calcular: "))
        #operacao = operacoes()
        resultado = operacao.sub(num1, num2)
        print("Resultado da subtração: ", resultado)
        
    if (op == 3):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = operacao.multi(num1, num2)
        print(f'A multiplicação de {num1} por {num2} é: {resultado}')
    if (op == 4):
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = operacao.div(num1, num2)
        print(f'A multiplicação de {num1} por {num2} é: {resultado}')

if __name__ == "__main__":
    main()