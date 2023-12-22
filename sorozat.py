import random


print("II/A,B,C:")
randomSzamLista = []
index = 0
while index < 15:
    randomSzam = random.randint(-90,500)
    randomSzamLista.append(randomSzam)
    index+=1

def masodikFeladat():
    index = 0
    while index < len(randomSzamLista):
        if index == 0:
            print("\t{}".format(randomSzamLista[index]), end="")
        else:
            print("*{}".format(randomSzamLista[index]), end="")
        index+=1

def oszthatoak_szama():
    oszthatoakSzama = 0
    index = 0
    while index < len(randomSzamLista):
        if randomSzamLista[index] % 10 == 0:
            oszthatoakSzama += 1
        index+=1
    return  f"\tTizzel oszthato szamok szama: {oszthatoakSzama}"

def konzolra_ir():
    print("\nII/D,E: ")
    print(oszthatoak_szama())
    print("kimutatas.txt tartalma:")
    print("II/F:")
    f = open("kimutatas.txt","w",encoding="utf-8")
    f.write(oszthatoak_szama())
    f.close()
    print("\t",oszthatoak_szama())



