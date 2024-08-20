print("Ola mundo")

#nome = 'Tiago'
#idade = 16
#peso = 66
#altura = 1,82
#instrtutor = True

# FIXME:Visualisando tipos de dados:
# FIXME:Entrada de dados:

sobrenome = input('Digite o seu sobrenome: ')

print(type(sobrenome))

#convertendo o valor do input

idade = input('Digite sua idade: ')
idade = int(idade)
print(type(idade))

ano = int(input('Em qual ano estamos:'))
print(type(ano))

if ano > 2024:
   print('dentro do if')