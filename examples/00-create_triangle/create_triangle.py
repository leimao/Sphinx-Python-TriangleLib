from trianglelib.shape import Triangle

if __name__ == "__main__":

    t = Triangle(5, 5, 5)
    print('Equilateral?', t.is_equilateral())
    print('Isosceles?', t.is_isosceles())