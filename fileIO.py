# jabber = open("C:/python/sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
#
#
# jabber.close()


#
# with open("C:/python/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("C:/python/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("C:/python/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines, end='')
#
# for line in lines:
#     print(line,end='')

# with open("C:/python/sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines, end='')
#
# for line in lines[::-1]:
#     print(line,end='')

with open("C:/python/sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line,end='')