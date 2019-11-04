number = "9,234,234,234,234,234"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

x = 23
x += 1
print(x)

x -= 2
print(x)
x *= 4
print(x)

x /= 3
print(x)

x **= 4
print(x)

x %= 60
print(x)

greeting = "Good"
greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)

