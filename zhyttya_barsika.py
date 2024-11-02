import random

class Kotyara:
    def __init__(self, name):
        self.name = name
        self.sleepiness = 50
        self.fullness = 0
        self.joy = 50
        self.hunger = 50
        self.alive = True

    def to_sraty(self):
        print("Idu posru")
        self.fullness -= 50
        self.sleepiness -= 5
        self.joy -= 10
        self.hunger -= 10

    def to_pogratysya(self):
        print("Pograyusya z hazyayinom")
        self.sleepiness += 5
        self.fullness += 20
        self.joy += 25
        self.hunger -= 20

    def to_spaty(self):
        self.sleepiness -= 20
        self.fullness += 20
        self.joy -= 20
        self.hunger -= 15

    def to_zhraty(self):
        self.sleepiness -= 10
        self.fullness += 40
        self.joy -= 10
        self.hunger += 50

    def is_Alive(self):
        if self.fullness >= 100:
            print("Barsika rozirvalo...")
            self.alive = False
        elif self.sleepiness >= 100:
            print("V Barsika perevtomlennya i vin zasnuv nazavzhdy...")
            self.alive = False
        elif self.joy <= 0:
            print("V Barsika depresiya i vin pishov z tvogo domu i ne povernuvsya...")
            self.alive = False
        elif self.joy > 100:
            print("V Barsika bulo perenasychennya adrenalinom i vin vypadkovo vykynuvsya z vikna...")
            self.alive = False
        elif self.hunger >= 100:
            print("Barsik zdoh z golodu...")

    def end_of_day(self):
        print(f"Sleepiness = {self.sleepiness}")
        print(f"Fullness = {(self.fullness)}")
        print(f"Joy = {(self.joy)}")
        print(f"Hunger = {(self.hunger)}")

    def live(self, day):
        day = "den " + str(day) + " z zhyttya " + self.name
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_sraty()
        elif live_cube == 2:
            self.to_pogratysya()
        elif live_cube == 3:
            self.to_spaty()
        elif live_cube == 4:
            self.to_zhraty
        self.end_of_day()
        self.is_Alive()

barsik = Kotyara(name="Barsik")

for day in range (366):
    if barsik.alive == False:
        break
    barsik.live(day)