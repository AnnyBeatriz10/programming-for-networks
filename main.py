# Leia uma string e uma letra no alfabeto e mostre o string no alfabeto da letra(usar apenas letras maiúsculas)
#s = (input("Digite um texto (maiúsculo):"))
#letra = (input("Informe uma letra (maiúscula):"))

#for letra in s:
#     print("o código ASCII da letra informada é:",ord(letra))
#else:
  #print("Essa letra não faz parte do texto informado")
  
#s =  (input("Digite o código do texto:"))
#letra = (input("Informe o código da letra:"))
#lista = []

#for i in s:
#   print("o texto do código informado é", chr(i))
#   s.append(lista)
#   for letra in lista:
#     print("o a letra correspondente é", chr(letra))
#     if letra in lista == False:
#        print("o código não faz parte do texto")

cifrado = input("Texto a decifrar : ")
texto = ""
for c in cifrado:
  l = chr(ord(c) -1)
  texto += l
print(texto)


# mostrar as próximas letras do texto: 

#texto = input("Texto a cifrar :")
#cifrado = ""

#for l in texto:
#   nl = chr(ord(l) + 1)
#   cifrado += nl
# print(cifrado)

# O LIVRO DOS CÓDIGOS
   

