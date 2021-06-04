class Dog:
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_dogs():
        print(f"There are currently {Dog.num_of_dogs} dogs")


def main():
    choco = Dog("Choco")
    spot = Dog('Spot')
    choco.get_num_dogs()


if __name__ == '__main__':
    main()
