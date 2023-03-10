'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

TODAY = datetime.now()

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def questao01():
    num1 = int(input('Núm 1: '))
    num2 = int(input('Núm 2: '))
    if num1+num2 > 10:
        print(f'{num1+num2} é maior do que 10!')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def questao02():
    num1 = int(input('Núm 1: '))
    num2 = int(input('Núm 2: '))
    if num1+num2 > 20:
        print(num1+num2+8)
    else:
        print(num1+num2-5)    

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def questao03():
    numero = int(input('Número: '))
    if numero % 3 == 0:
        print('É múltiplo de 3')
    else:
        print('Não é múltiplo de 3')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def questao04():
    numero = int(input('Número: '))
    if numero % 5 == 0:
        print('É divisível por 5')
    else:
        print('Não é divisível por 5')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def questao05():
    numero = int(input('Número: '))
    if numero % 3 == 0 and numero % 7 == 0:
        print(f'{numero} é divisível por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def questao06():
    salario_bruto = float(input('Salário Bruto: '))
    valor_prestacao = float(input('Valor da Prestação: '))
    credito = salario_bruto * 0.3
    if (valor_prestacao > credito):
        print(f'{valor_prestacao} não pode ser superior ao crédito de {credito}!')
    else:
        print('Empréstimo concedido!')

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def questao07():
    numero = int(input('Número: '))
    if numero >= 20 and numero <= 50:
        print('Número compreendido entre 20 e 50')
    else:
        print('Número NÃO está compreendido entre 20 e 50')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def questao08():
    numero = int(input('Número: '))
    if numero > 20:
        print('> 20')
    elif numero < 20:
        print('< 20')
    else:
        print('= 20')    

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def questao09():
    ano_nascimento = int(input('Ano de Nascimento: '))
    if ano_nascimento > TODAY.year:
        print(f'ERRO: Ano de nascimento {ano_nascimento} inválido!')
    else:
        idade = TODAY.year - ano_nascimento
        print(f'Idade: {idade}')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def questao10():
    a = int(input('1 Número: '))
    b = int(input('2 Número: '))
    c = int(input('3 Número: '))

    if a<=b and b<=c:
        print(f'{a}\t{b}\t{c}')
    elif a<=c and c<=b:
        print(f'{a}\t{c}\t{b}')
    elif b<=a and a<=c:
        print(f'{b}\t{a}\t{c}')
    elif b<=c and c<=a:
        print(f'{b}\t{c}\t{a}')
    elif c<=a and a<=b:
        print(f'{c}\t{a}\t{b}')
    else:
        print(f'{c}\t{b}\t{a}')

#11. Faça um programa que leia 3 números e imprima o maior deles.
def questao11():
    numero = int(input('1 Número: '))
    maior = numero
    numero = int(input('2 Número: '))
    if numero > maior:
        maior = numero
    numero = int(input('3 Número: '))
    if numero > maior:
        maior = numero
    print(f'Maior Número: {maior}')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
def questao12():
    idade = int(input('Idade: '))
    if idade >= 18:
        print('É maior de idade')
        if idade > 65:
            print('Idade maior de 65 anos')
    else:
        print('É menor de idade')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def questao13():
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    print(f'Nome: {nome}')
    print(f'Notas: {n1}\t{n2}')
    print(f'Média: {media}')
    if media >= 7:
        print('Aprovado!')
    elif media >= 3:
        print('Prova Final!')
    else:
        print('Reprovado!')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def questao14():
    salario = float(input('Salário: '))
    inss = 0.0
    if salario > 2000:
        inss = salario * 0.3
    elif salario > 1200:
        inss = salario * 0.25
    elif salario > 600:
        inss = salario * 0.2
    else:
        inss = 0.0
    print(f'INSS: {inss}')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def questao15():
    valor_produto = float(input('Custo do produto: '))
    lucro = 0.0
    if valor_produto < 20:
        lucro = valor_produto * 0.45 
    else:
        lucro = valor_produto * 0.3
    print(f'Valor de Venda: {valor_produto + lucro}')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def questao16():
    idade = int(input('Idade: '))
    if idade >= 18:
        print('Categoria Sênior!')
    elif idade >= 14:
        print('Categoria Juvenil B!')
    elif idade >= 11:
        print('Categoria Juvenil A!')
    elif idade >= 8:
        print('Categoria Infantil B!')
    elif idade >= 5:
        print('Categoria Infantil A!')
    else:
        print('Não pode participar do campeonato!')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def questao17():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    print('Valor do plano de saúde: ')
    if idade >= 65:
        print(400)
    elif idade >= 59:
        print(250)
    elif idade >= 45:
        print(150)
    elif idade >= 29:
        print(120)
    elif idade >= 10:
        print(60)
    else:
        print(30)

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def questao18():
    mes = int(input('Mês: '))
    if mes < 1 or mes > 12:
        print('Mês inválido!')
    else:
        data = datetime(2022, mes, 1)
        print(data.strftime('%b'))

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def questao19():
    a = int(input('Pontos J1: '))
    b = int(input('Pontos J2: '))
    c = int(input('Pontos J3: '))

    if a>=b and b>=c:
        print(f'{a}\t{b}\t{c}')
    elif a>=c and c>=b:
        print(f'{a}\t{c}\t{b}')
    elif b>=a and a>=c:
        print(f'{b}\t{a}\t{c}')
    elif b>=c and c>=a:
        print(f'{b}\t{c}\t{a}')
    elif c>=a and a>=b:
        print(f'{c}\t{a}\t{b}')
    else:
        print(f'{c}\t{b}\t{a}')
    
    soma = a+b+c
    if soma > 100:
        print(f'Média de pontos por jogador: {soma/3.0}')
    else:
        print('Equipe desclassificada')

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def questao20():
    saldo_medio = float(input('Saldo Médio: '))
    if saldo_medio > 3001:
        print(f'Crédito: {saldo_medio * 0.5}')
    elif saldo_medio >= 1001:
        print(f'Crédito: {saldo_medio * 0.4}')
    elif saldo_medio >= 501:
        print(f'Crédito: {saldo_medio * 0.3}')
    else:
        print('Nenhum crédito disponível')        

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def questao21():
    nome = input('Nome do Livro: ')
    tipo = input('Tipo A/P (Aluno ou Professor): ')
    if tipo == 'A':
        print(f'Total de dias: 3')
    elif tipo == 'P':
        print(f'Total de dias: 10')
    else:
        print('Não pode ser emprestado!')

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def questao22():
    kms = int(input('kms percorridos: '))
    tipo_carro = input('Tipo do Carro: ').upper().strip()[0]
    consumo = 0.0
    if tipo_carro == 'A':
        consumo = kms / 12
    elif tipo_carro == 'B':
        consumo = kms / 9
    else:
        consumo = kms / 8
    print(f'Consumo: {round(consumo, 1)} litros')

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal
def questao23():
    prato = input('Prato principal: ').strip().upper()
    bebida = input('Bebida: ').strip().upper()
    sobremesa = input('Sobremesa: ').strip().upper()
    calorias = 0
    calorias += 180 if prato == 'VEGETARIANO' else 0
    calorias += 230 if prato == 'PEIXE' else 0
    calorias += 250 if prato == 'FRANGO' else 0
    calorias += 350 if prato == 'CARNE' else 0
    calorias += 20 if bebida == 'CHA' else 0
    calorias += 70 if bebida == 'SUCO DE LARANJA' else 0
    calorias += 100 if bebida == 'SUCO DE MELAO' else 0
    calorias += 65 if bebida == 'REFRIGERANTE DIET' else 0
    calorias += 75 if sobremesa == 'ABACAXI' else 0
    calorias += 110 if sobremesa == 'SORVETE DIET' else 0
    calorias += 170 if sobremesa == 'MOUSSE DIET' else 0
    calorias += 200 if sobremesa == 'MOUSSE DE CHOCOLATE' else 0
    print(f'Total de calorias: {calorias} cal')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def questao24():
    placa = input('Placa: ')
    mes = int(placa[len(placa) - 1])
    data = datetime(2022, mes, 1)
    print(data.strftime('%b'))

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
def questao25():
    indice = float(input('Índice de Poluição: '))
    if indice >= 0.5:
        print('1º, 2º e 3º grupo')
    elif indice >= 0.4:
        print('1º e 2º grupo')
    elif indice >= 0.3:
        print('1º grupo')
    else:
        print('Não receberá intimação')

opcao = -1
menu = '''
================================
            PROGRAMAS
================================
[1]  - Adição
[2]  - Adição 2
[3]  - Múltiplo
[4]  - Múltiplo 2
[5]  - Múltiplo 3
[6]  - Crédito
[7]  - Intervalo
[8]  - Menor/Maior
[9]  - Idade
[10] - Crescente
[11] - Maior
[12] - Idade 2
[13] - Situação Aluno
[14] - INSS
[15] - Valor de Venda
[16] - Natação
[17] - Plano de Saúde
[18] - Mês do Ano
[19] - Arco e Flecha
[20] - Crédito Especial
[21] - Biblioteca
[22] - Consumo Combustível
[23] - Calorias
[24] - Emplacamento
[25] - Intimação

[0] - Sair
================================
'''

while opcao != 0:
    print(menu)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1: questao01()
    if opcao == 2: questao02()
    if opcao == 3: questao03()
    if opcao == 4: questao04()
    if opcao == 5: questao05()
    if opcao == 6: questao06()
    if opcao == 7: questao07()
    if opcao == 8: questao08()
    if opcao == 9: questao09()
    if opcao == 10: questao10()
    if opcao == 11: questao11()
    if opcao == 12: questao12()
    if opcao == 13: questao13()
    if opcao == 14: questao14()
    if opcao == 15: questao15()
    if opcao == 16: questao16()
    if opcao == 17: questao17()
    if opcao == 18: questao18()
    if opcao == 19: questao19()
    if opcao == 20: questao20()
    if opcao == 21: questao21()
    if opcao == 22: questao22()
    if opcao == 23: questao23()
    if opcao == 24: questao24()
    if opcao == 25: questao25()
