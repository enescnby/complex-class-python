# complex-class-python [![Owner](https://img.shields.io/badge/owner-enescnby-blue)](https://github.com/enescnby)

[Github Repository](https://github.com/enescnby/complex-class-python)

This class is a basic form of complex numbers in Python.

+ In mathematics, a complex number is an element of a number system that extends the real numbers with a \
specific element denoted i, called the imaginary unit and satisfying the equation ***i² = -1*** ; \
every complex number can be expressed in the form ***a + bi***.

- a is called ***real part*** and b is called ***imaginary part***.

### Addition:

    The real part of complex numbers is added up with the real part of other complex numbers.
    
    Imaginary part of complex number is added up with the imaginary part of the other comlex numbers.
    
    When adding the complex number and the real number, you can think of the imaginary part of the real number as 0.

    (a + bi) + (c + di) = (a + c) + (b + d)i
    
### Multiplication:

    (a + bi) * (c + di) = a*c + (a*d)i + (b*c)i + (b*d)i² --> Use the equation of i² = -1
    = ac - bd + (ad + bc)i
    
### Equality:

    x = a + bi and y = c + di

    If a = c and b = d, these complex numbers are equal.

[Click here](https://en.wikipedia.org/wiki/Complex_number) for detailed information about complex numbers.


## METHODS:

1 \) **setreal** \(real : int \| float\) -> None :

    Sets the real part with given parameter.
    
2 \) **setimag** \(imag : int \| float\) -> None

    Sets the imaginary part with given parameter.
    
3 \) **getreal** \(\) -> int \| float :

    Returns the real part.
    
4 \) **getimag** \(\) -> int \| float :

    Returns the imag part.
