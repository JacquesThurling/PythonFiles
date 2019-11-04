# appendContent = ''
#
# for val1 in range(1, 13):
#
#     for val2 in range(2, 13):
#         string = '{} times {} is equal to {}.\n'.format(val1, val2, val1 * val2)
#         appendContent += string
#
# with open("C:/python/sample.txt", 'a+') as append_file:
#     append_file.write(appendContent)

#Solution

with open("C:/python/sample2.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} time {0} is {2}".format(i, j, i * j), file=tables)
        print('-' * 40, file=tables)