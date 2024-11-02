import random

class Human:
    def __init__(self, name="Ivan", job=None, home=None, car=None):
        self.name = name
        self.home = home
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive:
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Treba kupity palyvo")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Treba zhrachki kupit")
            self.money -= 50
            self.home.food += 50
        elif manage == "Yaycya":
            print("Kuplyu yaycya")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 1

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_index(self, day):
        day = f"syodni {day} z zhyttya {self.name}a"
        print(f"{day:=^50}", "\n")
        human_index = self.name + "a tablo"
        print(f"{human_index:=^50}", "\n")
        print(f"Bablo - {self.money}")
        print(f"Sitist - {self.satiety}")
        print(f"Dovolnist - {self.gladness}")

        home_index = f"Home tablo"
        print(f"{home_index:=^50}", "\n")
        print(f"Zhrachka - {self.home.food}")
        print(f"Svinstvo - {self.home.mess}")

        car_index = f"{self.car.brand} car tablo"
        print(f"{car_index:=^50}", "\n")
        print(f"Palivo - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depresiya...")
            return False
        if self.satiety < 0:
            print("Zdoh...")
            return False
        if self.money < - 500:
            print("Bankrot...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Bomzh")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Kupy mashinu {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"meni nada bablo togo ya stav {self.job.job}om z zarplatoyu {self.job.salary} kopiyok")
        self.day_index(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("zhraaaaat!")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("hochu pochilit ale v mene doma svynatnyk...\nTaksho priydetsya poprybiraty")
                self.clean_house()
            else:
                print("pochilyu")
                self.chill()
        elif self.money < 0:
            print("Nada na robotu")
            self.work()
        elif self.car.strength < 15:
            print("Nada mashinu pochinity")
            self.to_repair()
        elif dice == 1:
            print("Pochilyu")
            self.chill()
        elif dice == 2:
            print("Treba pracyuvaty")
            self.work()
        elif dice == 3:
            print("Nada hatu pribraty")
            self.clean_house()
        elif dice == 4:
            print("Chas dlya vkusnyashok")
            self.shopping(manage="Yaycya")


brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption":6},
    "Lada":{"fuel":50, "strength": 40, "consumption":10},
    "Volvo":{"fuel":70, "strength":150, "consumption":8},
    "Ferrari":{"fuel":80, "strength":120, "consumption":14}
}

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Mashina ne mozhe yihaty")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java Developer":{"salary":50, "gladness_less":10},
    "Python Developer":{"salary":40, "gladness_less":3},
    "C++ Developer":{"salary":45, "gladness_less":25},
    "Ruby Developer":{"salary":70, "gladness_less":1}
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

ivan = Human(name="Ivan")

for day in range(1, 8):
    if ivan.live(day) == False:
        break