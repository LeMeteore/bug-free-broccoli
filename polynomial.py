from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore

class Poly2:

    def __init__(self, *coeffs):
        assert len(coeffs) == 3, "Un polynome de degré 2 devrait avoir 3 coefficients"
        self.coeffs = {deg: co for deg, co in enumerate(coeffs[::-1])}

    def __add__(self, other):
        assert isinstance(other, Poly2)
        result = Poly2(0, 0, 0)
        result.coeffs = {**self.coeffs}
        for exp, c in other.coeffs.items():
            result.coeffs[exp] = result.coeffs.get(exp, 0) + c
        return result

    def __sub__(self, other):
        assert isinstance(other, Poly2)
        result = Poly2(0, 0, 0)
        result.coeffs = {**self.coeffs}
        for exp, c in other.coeffs.items():
            result.coeffs[exp] = result.coeffs.get(exp, 0) - c
        return result

    def __repr__(self):
        msg = "Poly2(" + ", ".join([str(c) for c in sorted(self.coeffs.values())]) + ")"
        return msg

    def __str__(self, var_string='X'):
        res = ''
        first_pow = len(self.coeffs) - 1
        for i, coef in self.coeffs.items():
            power = first_pow - i

            if coef:
                if coef < 0:
                    sign, coef = (' - ' if res else '- '), -coef
                elif coef > 0: # must be true
                    sign = (' + ' if res else '')

                str_coef = '' if coef == 1 and power != 0 else str(coef)

                if power == 0:
                    str_power = ''
                elif power == 1:
                    str_power = var_string
                else:
                    str_power = var_string + '^' + str(power)

                res += sign + str_coef + str_power
        return res

    def solve(self):
        a, b, c = self.coeffs.values()
        delta = sqrt(b**2 - 4*a*c)
        x1 = (-b + delta)/(2*a)
        x2 = (-b - delta)/(2*a)
        return x1, x2

    def _val(self, v):
        value = sum([pow((v*co), deg) for deg, co in self.coeffs.items()])
        return value

    def draw(self, x_points=None):
        if x_points is None:
            x_points = range(0, 20)
        y_points = [self._val(x) for x in x_points]
        plt.style.use('seaborn-whitegrid')
        plt.scatter(x_points, y_points, marker='x', c="green")
        plt.xlabel("Abscisses")
        plt.ylabel("Ordonnées")
        plt.title(self.__str__())
        plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
