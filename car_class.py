class car:

    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def getyear_model(self):
        return self.__year_model

    def getmake(self):
        return self.__make

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def main():
    auto = car("2000", "ford", 0)
    x = 0
    while x < 5:
        auto.accelerate()
        print(auto.get_speed())
        x += 1

    print(car)

main()
