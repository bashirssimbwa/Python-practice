fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1


fruit = 'hippo'
for letter in fruit[:: -1]:
    print(letter)
