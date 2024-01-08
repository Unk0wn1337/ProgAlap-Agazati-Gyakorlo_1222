import Gep
f = open("gep.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def gepek_szama():
    index = 0
    while index < len(sorok):
        index+=1
    print(f"III/A,B:\n\tA gepek szama: {index}.")
def atlag():
    gepekIdOsszeg = 0
    gepekIdOsztando = 0
    index = 0
    while index < len(sorok):
        Gepek = Gep.Gep(sorok[index])
        if Gepek.id % 2 == 0:
            gepekIdOsszeg += Gepek.id
            gepekIdOsztando += 1
        index += 1
    print(f"III/C\n\tA paros teremszamu termek azonosito atlaga: {gepekIdOsszeg / gepekIdOsztando}.")

def legkisebb():
    legkisebbAzon = 5
    legkisebbHelye = ""
    index = 0
    while index < len(sorok):
        Gepek = Gep.Gep(sorok[index])
        if Gepek.id < legkisebbAzon:
            legkisebbAzon = Gepek.id
            legkisebbHelye = Gepek.hely
        index+=1
    print(f"III/D:\n\tA legkisebb asztali gep azonositoja: {legkisebbAzon}, helye: {legkisebbHelye}.")


