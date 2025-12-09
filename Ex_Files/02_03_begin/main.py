NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

Random =[1, "Hello", 3.14, True ]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] # Slicing from start to index 2 (not inclusive)
GEORGE_RINGO = NAMES[2:] # Slicing from index 2 to the end
REVERSE = NAMES[::-1] # Reversing the list
EVERY_OTHER = NAMES[::2]

# print(sum(AGES))
# print(min(AGES))
# print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)
print(JOHN)
print(Random[2], Random[0])