count = 0
total = 0
while True:
    line = input("Enter a Number :")
    if line.lower() == 'done':
        break
    try:
        number = float(line)
    except:
        print("Invalid Input")

        continue
    count += 1
    total += number
average = total / count
print("total:", total, "count:", count, "average:", average )
    





count = 0
total = 0
max_value = None 
min_value = None 

while  True:
    line = input("Enter a Number:")
    if line.lower() == 'done':
        break
    try:
        number = float(line)
    except:
        print("Enter a Valid Number")
        continue 
    count += 1
    total += number
    if max_value is None or number > max_value:
        max_value = number
    if min_value is None or number < min_value:
        min_value = number
print("total:", total)
print("count:", count)
print("min_value:", min_value)
print("max_value:", max_value)

