#id!hely!tipus!ipcim

class Gep:
    def __init__(self,sor:str):
        adatok = sor.strip().split("!")
        self.id = int(adatok[0])
        self.hely = adatok[1]
        self.tipus = adatok[2]
        self.ipCim = adatok[3]

    def __str__(self):
        return f"id: {self.id}, hely: {self.hely}, tipus: {self.tipus}, ip cim: {self.ipCim}"