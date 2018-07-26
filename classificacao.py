from sklearn.naive_bayes import MultinomialNB

# sudo pip install virtualenv
# virtualenv ENV
# pip install numpy scipy scikit-learn
# python classificacao.py

# perna curta, rabo comprido, peludo, gordinho
porco1 = [1, 0, 0, 1]
porco2 = [0, 0, 1, 1]
porco3 = [1, 0, 1, 1]
porco4 = [1, 0, 0, 0]
gato1 =  [0, 1, 1, 0]
gato2 =  [0, 1, 0, 1]
gato3 =  [1, 1, 0, 0]
gato4 =  [0, 0, 1, 0]

dados = [porco1, porco2, porco3, porco4, gato1, gato2, gato3, gato4]
classes = [0, 0, 0, 0, 1, 1, 1, 1]

modelo = MultinomialNB()
modelo.fit(dados, classes)

misterioso1 = [1, 1, 1, 0] # gato
misterioso2 = [1, 0, 1, 0] # porco
misterioso3 = [0, 0, 0, 1] # porco
testes = [misterioso1, misterioso2, misterioso3]
classes_teste = [1, 0, 0]
animais_teste = ["gato" if i == 1 else "porco" for i in classes_teste]

resultado = modelo.predict(testes)
animais_resultado = ["gato" if i == 1 else "porco" for i in resultado]

print("Resposta correta = " + str(classes_teste).ljust(60, ' '))
print("Animais da resposta correta = " + str(animais_teste).ljust(60, ' ') + "\n")
print("Resultado = " + str(resultado).ljust(60, ' '))
print("Animais = " + str(animais_resultado).ljust(60, ' '))

# Calculo da taxa de acerto
diferencas = resultado - classes_teste
acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
print("\nTaxa de acerto = " + str(taxa_de_acerto))