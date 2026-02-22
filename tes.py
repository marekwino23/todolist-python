plik = open("test.txt", "w")
if plik.writable():
    plik.write(input("Wpisz tekst: ") + "\n")
    
plik.close()

plik = open("test.txt", "r")
if plik.readable():
    for txt in plik:
        print(txt)
