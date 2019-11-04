text = input("Please enter your sample text here: ")
vowels = set(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"))

setText = set(text)
# print(sorted(setText))

difference = setText.difference(vowels)
output = "".join(sorted(difference))
print(output)

# Solution

sampleText = "Python is a very powerful language"

vowels2 = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels2)

print(finalSet)

finalList = sorted(finalSet)
print(finalList)