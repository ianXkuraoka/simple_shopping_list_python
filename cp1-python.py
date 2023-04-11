#RM98860 - Ian Xavier Kuraoka


#introdução


print('Bem-vindo ao site da Vinheira Agnello!')
nome = input('Por favor, digite seu nome completo: ')
idade = int(input('Digite sua idade: '))


#Verificar se o cliente é maior de idade


if idade < 18:
    print('Você precisa ter 18 anos ou mais para comprar bebidas alcoólicas!')
else:
    endereco_cliente = input('Digite seu endereço: ')
    endereco_entrega = input('Digite o endereço para entrega: ')
    
    if endereco_cliente != endereco_entrega:
        opcao = input('O endereço para entrega está correto? (S/N): ')
        if opcao.upper() != 'S':
            endereco_entrega = input('Digite o endereço de entrega: ')

    print('')
    print('Ótimo! Aqui está nosso catálogo de vinhos.')


#Catálogo de vinhos com preços


    catalogo = {'Vinho Tinto': 50, 'Vinho Branco': 40, 'Vinho Rosé': 35, 'Espumante Brut': 60, 'Espumante Moscatel': 45}


#Mostrar catálogo de vinhos


    print("")
    print('Catálogo de Vinhos:')
    for vinho, preco in catalogo.items():
        print(vinho + ': R$' + str(preco))
    print('')


#Solicitar a quantidade de vinhos que o cliente deseja comprar e calcular valor total


    x = 0
    total = 0
    for vinho, preco in catalogo.items():
        quantidade = int(input('Quantos ' + vinho + ' você deseja comprar? '))
        total += preco * quantidade
        x += quantidade


#Verificar se o valor total é menor que R$100


    if total < 100:
        print('')
        print('O valor mínimo de compra é de R$ 100. Por favor, selecione mais produtos da próxima vez.')
    else:


#Verificar se o valor total está entre R$100 e R$200 ou se é mais (ou iqual) a 200


        if total < 200:
            total += 30
            print('')
            print('Compras abaixo de R$200 possuem um frete de R$ 30.')
        else:
            print('')
            print('Frete grátis!')


#Mostrar mensagem de confirmação


        print('Pedido confirmado.')
        print('Você comprou ' + str(x) + ' itens.')
        print('Total a pagar: R$ ' + str(total))
        print('Endereço de entrega: ' + endereco_entrega)
        print('Obrigado pela compra, ' + nome + '! volte sempre !')


#fim