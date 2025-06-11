import numbers
from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other


    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + tuple(-n for n in other.coefficients[common:])
            #+ other.coefficients[common:]
            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __rsub__(self,other):
        if self.coefficients[0] >= other:
            return Polynomial((self.coefficients[0] - other,)+tuple(-n for n in self.coefficients[1:]))
        else:
            return Polynomial((other - self.coefficients[0],)+tuple(-n for n in self.coefficients[1:]))


    def __mul__(self,other):
        if isinstance(other , Number):
            return Polynomial(tuple(other*n for n in self.coefficients))

        if isinstance(other, Polynomial):
            degree_of_multiplied_polynomial = self.degree() + other.degree()
            list = [0 for i in range(degree_of_multiplied_polynomial+1)]
            i_addition = 0

            for i in self.coefficients:
                j_index = 0
                for j in other.coefficients:
                    list[(j_index+i_addition)] += (i*j)
                    j_index += 1
                i_addition += 1
            return Polynomial(tuple(list))


    def __rmul__(self,other):
        return self*other


    def __pow__(self,exponent):
        if isinstance(exponent, numbers.Integral):
            copy = self * 1
            for i in range(exponent-1):
                self = self * copy
            return self
        else:
            NotImplemented

    def __call__(self , x):
        if isinstance(x , Number):
            index = 0
            value = 0
            for i in self.coefficients:
                value += i*(( x )**index)
                index += 1
            return value

    def dx(self):
        if isinstance(self, Polynomial):
            derivative = self.coefficients[1:]
            index = tuple(i for i in range(1,self.degree()+2))
            result = tuple(a*b for a,b in zip(derivative,index))
            return Polynomial(result)





