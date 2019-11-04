fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         }

print(fruit)

veg = {
    "cabbage" : "Every child's favouraite",
    "sprouts" : "mmmm, lovely",
    "spinach" : "can I have some more fruit, please"
}

number = {
    1 : {"D" : 3}
}

number2 = {
    1: {"C" : 2}
}
print(veg)

number2[1].update(number[1])
print(number2)
# veg.update(fruit)
# print(veg)
#
# fruit.update(veg)
# print(fruit)

# print(fruit.update(veg))
# print(fruit)
#
# nice_and_nasty = fruit.copy()
# nice_and_nasty.update(veg)
# print(nice_and_nasty)
#
# print(veg)
# print(fruit)