list = [2, 3, 4, 5, 6, 7]
iteration = iter(list)

for i in range(len(list)):
    print(next(iteration))

print('You did an iteration')