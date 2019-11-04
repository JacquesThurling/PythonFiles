ip = str(input("Please enter an IP address: "))

count = 0
segment = 1
address = ''

for i in range(len(ip)):
    if ip[i] == '.':
        segment += 1
        if len(address) == 0:
            segment -= 1
        print("There are {0} segments length is {1}".format(segment, len(address)))

        address = ''
    else:
        address += ip[i]

print("There are {0} segments length is {1}".format(segment, len(address)))

# if segment != 1:
#     print("There are {0} segments length is {1}".format(segment,len(address)))
# else:
#     print("There is {0} segment".format(segment))

# print(address)
