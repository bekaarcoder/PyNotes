class Animal:
    def __init__(self, type="Unknown", appearance="Unknown"):
        self.type = type
        self.appearance = appearance

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, value):
        self.__appearance = value

    def __str__(self):
        return f"An {type(self).__name__} is {self.type} it has {self.appearance}"


class Mammal(Animal):
    def __init__(self, type="born alive", appearance="hair or fur", nurse_young=True):
        Animal.__init__(self, type, appearance)
        self.nurse_young = nurse_young

    @property
    def nurse_young(self):
        return self.__nurse_young

    @nurse_young.setter
    def nurse_young(self, value):
        self.__nurse_young = value

    def __str__(self):
        return super().__str__() + f" and it is {self.nurse_young} they nurse their young"


def main():
    animal1 = Animal("born alive")
    print(animal1.type)
    print(animal1)

    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.type)
    print(mammal1.appearance)
    print(mammal1.nurse_young)

main()