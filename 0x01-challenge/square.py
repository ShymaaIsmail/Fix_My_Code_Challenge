#!/usr/bin/python3
""" Square Class"""


class Square():
    """ class square docs"""

    def __init__(self, *args, **kwargs):
        """ init function for Square"""
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.height != self.width:
            raise ValueError("Square height must be equal to square width")

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Permiter of the Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """stringify the Square class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ test sample of square"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
