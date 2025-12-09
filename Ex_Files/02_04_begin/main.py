NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
print (len(NAMES),"\n")
print(range(5),", entspricht range(5)\n")
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1
print("-----\n print(NAMES[i], AGES[i])\n-----\n")

for name in NAMES:
    print(name)

print("-----\n  for name in NAMES: \n-----\n")

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

print("-----\n \n-----\n")

for name in reversed(NAMES):
    print(name)

print("-----\n \n-----\n")

for i in range(5):
    print(i)

print("-----\n \n-----\n")

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i}, {name}")


#for in erklärung 
# Erklärung:

# NAMES ist eine Variable, die eine Liste (oder ein anderes iterierbares Objekt) mit Namen enthalten muss, z.B. NAMES = ["Anna", "Ben", "Clara"].
# Die for-Schleife geht jedes Element in NAMES der Reihe nach durch.
# Bei jedem Durchlauf wird das aktuelle Element der Liste in die Variable name gespeichert.
# print(name) gibt den aktuellen Namen aus.
# Warum klappt das?
# Die Variable name wird in der Schleife automatisch für jedes Element aus NAMES gesetzt.
# Wenn NAMES nicht vorher definiert ist, bekommst du einen Fehler (NameError).
# Das Beispiel funktioniert also nur, wenn NAMES vorher existiert und z.B. eine Liste ist.


#neue erklärung für f in print:

# The f before the string in print(f"{name} {age}") stands for f-string (formatted string literal).
# What it does:
# It allows you to embed expressions (like variables) directly inside curly braces {} within the string.
# Python will replace {name} and {age} with the values of those variables when printing.

# Example:
# If name = "Anna" and age = 30,
# print(f"{name} {age}") will output: 
# Anna 30


#erklärung zu zip():

# In Python, zip(NAMES, AGES) kombiniert zwei Listen (oder andere iterierbare Objekte) paarweise.

# Beispiel:
# NAMES = ["Anna", "Ben", "Clara"]
# AGES = [30, 25, 28]

# for name, age in zip(NAMES, AGES):
#     print(name, age)

# Was macht zip?
# Es erstellt Paare:

# Erstes Element aus NAMES mit erstem aus AGES
# Zweites mit zweitem usw.
# Ausgabe:
# Anna 30
# Ben 25
# Clara 28

# Kurz:
# zip verbindet die Listen zu Tupeln, die du in der Schleife gleichzeitig verwenden kannst.


#erklärung range(5):  sehr speichereffizient enumerate ist anscheinend aber trotzdem besser

# range(5) erzeugt eine Folge von Zahlen von 0 bis 4 (insgesamt 5 Zahlen).
# for i in range(5):
#     print(i)

# erzeugt :
# 0
# 1
# 2
# 3
# 4
# range(5) wird oft verwendet, um eine Schleife genau 5-mal auszuführen.


# # # # # # erklärung enumerate():

# # # # # # # # # In Python, enumerate(NAMES) gibt dir beim Durchlaufen einer Liste sowohl den Index (i) als auch das Element (name).

# # # # # # # # # Beispiel:
# # # # # # # # # NAMES = ["Anna", "Ben", "Clara"]

# # # # # # # # # for i, name in enumerate(NAMES):
# # # # # # # # #     print(f"{i}, {name}")

# # # # # # # # # Ausgabe:
# # # # # # # # # 0, Anna
# # # # # # # # # 1, Ben
# # # # # # # # # 2, Clara

# # # # # # # # # Was macht enumerate?
# # # # # # # # # Es liefert bei jedem Schleifendurchlauf ein Tupel aus (Index, Element).
# # # # # # # # # So kannst du auf die Position und den Wert gleichzeitig zugreifen.