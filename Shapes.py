import math


class Shape:
    """
    Base class for all shapes. Provides ID, print(), perimeter() and area() methods.
    """
    # Auto incrementing ID
    next_id = 1

    def __init__(self):
        self.id = Shape.next_id
        Shape.next_id += 1

    def print(self):
        """
        Returns a string representation of the shape including its ID, class name, perimeter, and area.
        """
        return "{id}: {className}, perimeter: {perimeter}, area: {area}" \
            .format(className=self.__class__.__name__, id=self.id,
                    perimeter="undefined" if self.perimeter() is None else round(self.perimeter(), 5),
                    area="undefined" if self.area() is None else round(self.area(), 5))

    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape. Must be implemented by child classes.
        """
        ...

    def area(self):
        """
        Calculates and returns the area of the shape. Must be implemented by child classes.
        """
        ...

    def __eq__(self, other):
        """
        Compares two shapes for equality based on their class names.
        """
        if isinstance(other, Shape):
            return self.__class__.__name__ == other.__class__.__name__
        return False

    def __hash__(self):
        """
        Returns a hash value for the shape.
        """
        return 1


class Ellipse(Shape):
    """
    Class representing an Ellipse shape.
    """
    def __init__(self, semi_minor, semi_major):
        super().__init__()
        self.semi_minor = float(semi_minor)
        self.semi_major = float(semi_major)

    def area(self):
        return math.pi * self.semi_major * self.semi_minor

    def eccentricity(self):
        calc = math.pow(self.semi_major, 2) - math.pow(self.semi_minor, 2)
        if calc < 0:
            return None
        else:
            return math.sqrt(calc)

    def print(self):
        return super().print() + " linear eccentricity: {eccentricity}"\
            .format(eccentricity="undefined" if self.eccentricity() is None else round(self.eccentricity(), 5))

    def __eq__(self, other):
        if isinstance(other, Ellipse):
            return self.semi_major == other.semi_major and self.semi_minor == other.semi_minor
        return False

    def __hash__(self):
        return hash((self.semi_major, self.semi_minor))


class Rhombus(Shape):
    """
    Class representing a Rhombus shape.
    """
    def __init__(self, diagonal1, diagonal2):
        super().__init__()
        self.diagonal1 = float(diagonal1)
        self.diagonal2 = float(diagonal2)

    def perimeter(self):
        return 2 * math.sqrt(math.pow(self.diagonal1, 2) + math.pow(self.diagonal2, 2))

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def side(self):
        return self.perimeter() / 4

    def in_radius(self):
        if self.diagonal1 == 0 or self.diagonal2 == 0:
            return None
        else:
            return (self.diagonal1 * self.diagonal2) / self.perimeter()

    def print(self):
        return super().print() + " side: {side}, in-radius: {in_radius}" \
            .format(side=round(self.side(), 5), in_radius=round(self.in_radius(), 0))

    def __eq__(self, other):
        if isinstance(other, Rhombus):
            return self.diagonal1 == other.diagonal1 and self.diagonal2 == other.diagonal2
        return False

    def __hash__(self):
        return hash((self.diagonal1, self.diagonal2))


class Circle(Shape):
    """
    Class representing a Circle shape.
    """
    def __init__(self, radius):
        super().__init__()
        self.radius = float(radius)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __hash__(self):
        return hash(self.radius)
