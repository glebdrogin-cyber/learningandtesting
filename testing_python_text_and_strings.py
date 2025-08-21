#a = "doesn't"
#b = '"Yes", they said.'
#c = '"Isn\'t it?" she asked.'
#print(a)
#print(b)
#print(c)

#word = "Python"
#print(word[0])
#print(word[0:4])
#print(word [0:1])
#print(word[1])  # Second character
#print(word[-1])  # Last character
#print(word[-2])  # Second to last character

# P y t h o n
# 0 1 2 3 4 5

#a = input("Bitte etwas eingeben:")
#print(a)

try:
    a = int(input("Eine zahl eingeben:"))
except ValueError:
    print("Das ist keine Zahl!")
