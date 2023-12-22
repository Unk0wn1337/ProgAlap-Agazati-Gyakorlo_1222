import Gep
def helyzet():
    f = open("gep.txt","r",encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    gepekSzama = 0
    gepekIdOsszeg = 0
    gepekIdOsztando = 0
    legkisebbId = 2
    legkisebbIdHelye = ""
    index = 0
    while index < len(sorok):
        gepekSzama +=1
        Gepek = Gep.Gep(sorok[index])
        if Gepek.id % 2 == 0:
            gepekIdOsszeg += Gepek.id
            gepekIdOsztando += 1
        if Gepek.id < legkisebbId:
            legkisebbId = Gepek.id
            legkisebbIdHelye = Gepek.hely



        index+=1
    gepekAtlag = gepekIdOsszeg / gepekIdOsztando
    gepekAtlag = round(gepekAtlag,2)
    print("III/A,B:")
    print(f"\t A gepek szama: {gepekSzama}.")
    print("III/C:")
    print(f"\tA paros teremszamu termek azonosito atlaga {gepekAtlag}.")
    print("III/D:")
    print(f"\tA legkisebb asztali gep azonositoja: {legkisebbId} helye: {legkisebbIdHelye}.")