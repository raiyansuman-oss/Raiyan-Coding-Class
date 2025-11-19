#Input a word or sentence
word = input("Please senter your own word or sentense : ")

reverse = ""

#loop for printing in reverse
for i in word:
    reverse = i + reverse

print()

print("The Original String = ", word)
print("THE reversed String = ", reverse)