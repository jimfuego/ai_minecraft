class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "{}{}{}".format(self.get_x(), self.get_y(), self.get_z())

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return (self.get_x() == other.get_x()) and \
                   (self.get_y() == other.get_y()) and \
                   (self.get_z() == other.get_z())
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def get_x(self):
        return self.x

    def get_coordinate(self):
        return self.x, self.y, self.z

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z


coset = set()
coset.add(Coordinate(10, 5, 5))
print(len(coset))
coset.add(Coordinate(10, 5, 5))
print(len(coset))
print(Coordinate(10, 5, 5) == Coordinate(10, 5, 6))
