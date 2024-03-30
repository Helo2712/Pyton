nome = str(input("Digite seu nome: "))
p = nome.find(" ")
primeiroNome = nome[:p]
print(f"Nome Maiusculo: {nome.upper()}\nNome Minusculo: {nome.lower()}\nQuantidade de letras: {len(nome.strip())}\nQuantidade de letras primeiro nome: {len(primeiroNome)}")