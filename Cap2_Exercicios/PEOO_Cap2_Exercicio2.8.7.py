# Livro...: Programação Estruturada e Orientada a Objetos em Python com Aplicações de Sistemas Operacionais
# Capítulo: 03
# Questão.: 2.8.7
# Autor...: Fábio Procópio
# Data....: 18/02/2019

sal_base   = 1500
comissao   = 200

corretor   = input("Digite o nome do corretor: ")
qtd_vendas = int(input("Informe a quantidade de imóveis vendidos: "))
tot_vendas = float(input("Informe o valor total das vendas do corretor (R$): "))

sal_final  = sal_base + comissao * qtd_vendas + tot_vendas * 0.05

print("Salário final de {} é R$ {:.2f}".format(corretor, sal_final))