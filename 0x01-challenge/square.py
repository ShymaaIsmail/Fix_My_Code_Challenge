#!/usr/bin/python3
""" Square Class"""


class Square():
    """ class square docs"""

    def __init__(self, *args, **kwargs):
        """ init function for Square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_Square(self):
        """ Area of the Square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Permiter of the Square """
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """stringify the Square class"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_Square())
    print(s.PermiterOfMySquare())
