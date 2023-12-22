def elsoFeladat():
    print("I/A:")
    print("")
    muzeumNeve:str = input("\tMuzeum neve:")
    latogatoNeve:str = input("\tLatogato neve:")
    ertekeles = int(input("\tErtekeles (1-20):"))
    print("I/B:")
    if ertekeles <= 0:
        print("\n\tAz ertekeles nem lehet negativ vagy 0!")
    elif ertekeles > 20:
        print("\n\t20 pont feletti ertekeles nem elfogadhato!")
    else:
        print("\n\tKoszonjuk az ertekelest!")
