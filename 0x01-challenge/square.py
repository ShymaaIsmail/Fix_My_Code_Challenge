#!/usr/bin/python3
""" Square Class"""

class square():

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ init function for square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """stringify the square class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
