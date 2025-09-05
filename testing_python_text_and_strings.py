#a = "doesn't"
#b = '"Yes", they said.'
#c = '"Isn\'t it?" she asked.'
#print(a)
#print(b)
#print(c)

############################

#word = "Python"
#print(word[0])
#print(word[0:4])
#print(word [0:1])
#print(word[1])  # Second character
#print(word[-1])  # Last character
#print(word[-2])  # Second to last character

# P y t h o n
# 0 1 2 3 4 5

############################

#a = input("Bitte etwas eingeben:")
#print(a)

############################

#try:
#    a = int(input("Eine zahl eingeben:"))
#except ValueError:
#    print("Das ist keine Zahl!")

############################

#zahlen = [1, 2, 3, 4, 5, 1, 1, 1]
#for zahl in zahlen:
#    print(zahl)
#print("\n")
#print(zahlen[0:2])
#print(zahlen[4])

############################

#text = "Hallo zusammen!"
#for c in text:
#    print(c)

############################

#liste = [1, 2, 3, 4, 5, 1, 1, 1]
#print(len(liste))  # Gibt die Länge der Liste aus

#liste2 = [2, "a", liste, 2+3]
#print(liste2)  # Gibt die Liste mit verschiedenen Datentypen aus
#liste2.append("etwas der Liste hinzufügen")
#print (liste2) # Fügt einen neuen Eintrag zur Liste hinzu

#liste3 = [1, "a", 2.5, True, None] #Listen können auch gemischt sein, wie hier zu sehen ist.



#print(text.upper())  # Gibt den Text in Großbuchstaben aus
#print(text.lower())  # Gibt den Text in Kleinbuchstaben aus
#print(text.capitalize())  # Gibt den Text mit großem Anfangsbuchstaben aus

############################

#x = 1
#for x in range(1, 11):
#    if x > 5:
#        print(x, "ist größer als 5")
#    else:
#        print(x, "ist kleiner oder gleich 5")

#############################

#"A" < "a"
# "A" < "B"  # True
# "a" < "b"  # True
# "A" < "a"  # True, da Großbuchstaben vor Kleinbuch
# "a" < "A"  # False, da Kleinbuchstaben nach Großbuchstaben

#cha = ["a", "B", "A","z"]
#cha.sort()  # Sortiert die Liste cha
#print(cha)  # Gibt die sortierte Liste aus

############################

#boolean

#a = 100
#if a > 10 and a < 1000:
#    print("a ist größer als 10 und kleiner als 1000")

#b = 2
#if b == 2 or b == 2:
#    print ("b ist entweder 2 oder 4")

#c = 250
#if c > 2 and not c == 251:
#    print("c ist größer als 2 und nicht gleich 251")

############################

#text = "Das ist ein Text."
#if "z" in text:
#    print("Der Text enthält ein 'z'.")
#else:
#    print("Der Text enthält kein 'z'.")

#if "D" in text:                     # Case sensitive Suche!
#    print("Der Text enthält ein 'D'.")
#else:
#    print("Der Text enthält kein 'D'.")

##############################

#def quadrat(x):
#   return x * x
#quadrat(4.1)
#print(quadrat(4.1)) # Gibt 16.81 zurück


class person:

    pjahre = 0
    
    def __init__(self, name, age):
        self.name = name
        self.alter = age
        person.pjahre = person.pjahre + age
    

    def greet(self):
        print("Hallo, mein Name ist", self.name, "und ich bin", self.alter, "Jahre alt.")
        print("Insgesamt sind wir", person.pjahre, "Jahre alt.")        

pgleb = person("Gleb", 37)
print(pgleb)   
pgleb.greet()

ptriin = person("Triin", 35)
print(ptriin)   
ptriin.greet()

class Kind(person):
    def __init__(self, name, age):
        if age > 12:
            raise ValueError("Ein Kind muss 12 Jahre oder jünger sein.")
        
        super().__init__(name, age)

            

peterle = Kind("Peter", 3)
peterle.greet()


