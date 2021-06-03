class Rectangle:

    type = "Shape"

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # Getter and Setter
    @property
    def height(self):
        print("Retrieving height.")
        return self.__height

    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please enter only numbers for the height.")

    @property
    def width(self):
        print("Retrieving height.")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please enter only numbers for the width.")

    def get_area(self):
        return int(self.__height) * int(self.__width)


def main():
    rect = Rectangle()
    height = input("Enter Height: ")
    width = input("Enter Width: ")
    rect.height = height
    rect.width = width
    print("Area: ", rect.get_area())
    print("Type: ", rect.type)


main()
