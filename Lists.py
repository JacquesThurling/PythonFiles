# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count('.'))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A norwegian blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
number_in_order = sorted(numbers)

print(number_in_order)

if numbers == number_in_order:
    print("The list are equal")
else:
    print("The lists are not equal")

if number_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")


