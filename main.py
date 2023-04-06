from time import sleep
print('Olá, vamos realizar os gastos da viagem!')
dias = int(input('Quantos dias o carro ficou alugados?'))
d = dias * 60
km = float(input('Quantos km rodados?'))
k = km * 0.15
total = d + k
print('O valor do aluguel do carro ficou de {:.2f} reais'.format(total))
gas = input('Quer realizar o calculo do gosto do combustivel?')
if gas == 'Sim':
    print('Otimo, estamos iniciando a calculadora...')
    sleep(2)
    km = float(input('Quantos km rodados?'))
    litro = float(input('Quantos litros esta fazendo o seu veiculo?'))
    kmtotal = km / litro
    print('O valor total de combustivel gasto é de {:.2f} litros'.format(kmtotal))
    combustivel = float(5.48)
    gasto = combustivel * km
    print('O total gasto com combustivel é de R$: {:.2f}'.format(gasto))
else:
    print('Obrigado pela preferencia!!!!')