print ("Calculadora IMC")
nome = input(" qual o seu nome?")
print (f"Bem Vindo {nome},vamos analisar seu indice corporal.")
idade = input(" Sua idade? ")
print ("por favor inserir as informações com os seguintes formatos, (ALTURA x.xx), (peso em XX kg)")
altura = float (input(" Sua altura?"))
peso = float(input(" Seu peso atual?"))

calculo_imc = (peso / (altura * altura))
print(f"{nome} o resultado do calculo do seu imc é:{calculo_imc:.0f}")

if calculo_imc <18:
    print ("Você está Magro")

elif calculo_imc <18:
    print("Vocé está com peso normal")

elif calculo_imc <25:
    print("vocé está sobrepeso")

elif calculo_imc <30:
    print ("vocé está no grau de obesidade nivel 1")

elif calculo_imc <35:
    print ("Você está no grau de obesidade nivel 2")

else:
    print ("você está no grau de obesidade nivel 3")