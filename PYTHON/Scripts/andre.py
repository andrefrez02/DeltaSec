def primeiroBin():
    binario = input('Digite um número binário: ')
    decimal = 0
    n = len(binario) - 1
    for d in binario:
        decimal = decimal + int(d)*2**n
        n -= 1
    return binario, decimal

def primeiroDec():
    num = int(input('Digite um número decimal: '))
    bin = ''
    while num != 0:
        r = num%2
        bin = str(r) + bin
        num = num//2
    return bin, num

def saida_bin2dec():
    val = primeiroBin()
    bin = val[0]
    dec = val[1]
    print(f'O binário {bin} é igual a {dec} na base 10')

def saida_dec2bin():
    val = primeiroDec()
    bin = val[0]
    dec = val[1]
    print(f'O decimal {dec} é igual a {bin}')

def inicio():
    op, primeiraRun = 'x', 'primeiraRun'
    while not op in '1234':
        if primeiraRun == 'primeiraRun':
            print('Entrada:\n1 - Primeiro número BINÁRIO\n2 - Primeiro número OCTAL\n',
            '\b3 - Primeiro número DECIMAL\n4 - Primeiro número HEXADECIMAL\n\nDigite', end = '')
            primeiraRun = 'x'
        else:
            print('\nOpção inválida.\nDigite novamente', end = '')
        try:
            op = input(' uma opção entre [1, 2, 3 e 4]: ')
            if op == '1':
                saida_bin2dec()
            elif op == '3':
                saida_dec2bin()
            else:
                print('Conteúdo não está pronto ainda... 😢')
        except:
            op = 'x'
            pass  

inicio()
#saida_bin2dec()
#saida_dec2bin()