count = 0
numbers = [1,2,3,4,5,678,98,100]
for num in numbers:
    count = count +1 
print ("count:", count)

# TOTAL
TOTAL = 0
numbers = [1,2,4,56,7,89,90]
for num in numbers:
    total = total + num
print ('total:', total)


#Condition for num > 6
total = 0
numbers = [1,2,3,44,667.87,90, 102, 167, 189]
for num in numbers:
    if num > 100:
        total = total + num
print('total:', total)


#prompt a User for an Input
total = 0
count = 0
while True:
    line = input("Enter a number: ")

    if line == "done":
        break

    try:
        number = float(line)
    except:
        print ("Enter numeric character")
        continue

    total = total+number
    count = count +1 

average = total / count

print("Total:", total)
print("Count:", count)
print("Average", average)
    



numbers = [23, 45, 78, 89, 23, 12, 56, 900, 1020]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num 
print("Smallest:", smallest)
        



count = 0 
total = 0

while  True:
    line = input("Enter a Number:")
    if line.lower() == 'done':
        break
    try:
        number = float(line)
    except:
        print("Value Error: Enter a Numeric character")
        continue 

    count = count + 1
    total = number + total
average = total / count
print("count", count)
print("total", total)
print("Average", average)
