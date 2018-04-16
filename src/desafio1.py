# -*- coding: utf-8 -*-
__author__ = "dumon"
__date__ = "$15/03/2018 14:13:38$"

if __name__ == "__main__":
    print "Hello World"


desafio = input("Qual desafio ? \n 1-Boas vindas \n 2-Aniversario \n 3-Soma \n")

if desafio == 1:   
    nome = raw_input("Qual é seu nome ? \n")
    print "Seja bem vindo(a)", nome, "!"
elif desafio == 2:
    print('Informe a sua data de nascimento. Exemplo: 3 de dezembro de 2000')
    dia_nasc = input("Dia de nascimento, exemplo \"10\" \n")
    mes_nasc = raw_input("Mês de nascimento, exemplo \"Janeiro\" \n")
    ano_nasc = input("Ano de nascimento, exemplo \"2000\" \n")
    print "Você nasceu no dia ", dia_nasc, " no mês ", mes_nasc, " no ano de ", ano_nasc
elif desafio == 3:
    print "Informe 2 números para serem somados :\n"
    num_1 = input("Primeiro número: \n")
    num_2 = input("Segundo número: \n")
    print "A soma será de (", num_1, "o número", num_2, ") tem resultado de:", num_1 + num_2
else:
    print "Digite apenas 1, 2 e 3"
