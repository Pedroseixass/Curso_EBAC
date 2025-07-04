#Interação!
nome = input('Olá, gostaria de saber o seu nome? ')
print(f'Olá, {nome}!')

#Utilização de `while` para loopar até a pessoa confirmar que ira usar a calculadora
inicio = input('Gostaria de usar a calculadora? Digite: "sim ou "não"! ').lower()
respostas = 'sim'
while respostas not in inicio:
  inicio = input('Tem certeza? Digite "sim" para continuar. ').lower()

#Uso de `if` e èlif`para executar os cálculos e entregar os resultados
if respostas == 'sim':
  valor = float(input('Digite o primeiro valor: '))
  valor2 = float(input('Digite o segundo valor: '))
  operador = input('Digite o operador:   (ex: +, -, *, /)')
  if operador == '+':
    print(f'Resultado: {valor + valor2}')
  elif operador == '-':
    print(f'Resultado: {valor - valor2}')
  elif operador == '*':
    print(f'Resultado: {valor * valor2}')
  elif operador == '/':
    print(f'Resultado: {valor / valor2}')
