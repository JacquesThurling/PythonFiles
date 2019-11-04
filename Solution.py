ipaddress = input("Please enter an IP: ")
if ipaddress[-1] != '.':
    ipaddress += '.'

segment = 1
length = 0
# character = ''

for character in ipaddress:
    if character == '.':
        print("Segment {} contains {} characters".format(segment, length))
        segment += 1
        length = 0
    else:
        length += 1

# unless the final character in the string was a . then we haven't printed
# he last segment
# if character != '.':
#     print("Segment {} contains {} characters".format(segment, length))
