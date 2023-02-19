
class Complex:

    def __init__(self, real: int | float, imag: int | float) -> None:

        if isinstance(real, (int, float)):
            self.real = real
        else:
            raise TypeError(
                f"Real part must be an integer or float not {type(real).__name__}")

        if isinstance(imag, (int, float)):
            self.imag = imag
        else:
            raise TypeError(
                f"Imaginary part must be an integer or float not {type(imag).__name__}")

    def __str__(self) -> str:

        if self.real == 0 and self.imag == 0:
            return "0"
        if self.real != 0 and self.imag == 0:
            return f"{self.real}"
        if self.real == 0 and self.imag != 0:
            return f"{self.imag}i"
        if self.real != 0 and self.imag != 0:
            if self.imag > 0:
                return f"{self.real} + ({self.imag})i"
            else:
                return f"{self.real} - ({-1 * self.imag})i"

    def __add__(self, other):

        if isinstance(other, (int, float)):

            real = self.real + other
            return Complex(real, self.imag)

        if isinstance(other, Complex):

            real = self.real + other.real
            imag = self.imag + other.imag
            return Complex(real, imag)

    def __sub__(self, other):

        if isinstance(other, (int, float)):

            real = self.real - other
            return Complex(real, self.imag)

        if isinstance(other, Complex):

            real = self.real - other.real
            imag = self.imag - other.imag
            return Complex(real, imag)

    def __mul__(self, other):

        if isinstance(other, (int, float)):

            real = self.real * other
            imag = self.imag * other
            return Complex(real, imag)

        if isinstance(other, Complex):

            real = self.real * other.real + -1 * (self.imag * other.imag)
            imag = self.real * other.imag  + other.real * self.imag
            return Complex(real, imag)

    def __eq__(self, other) -> bool:

        if isinstance(other, (int, float)) and self.imag == 0 and self.real == other:
            return True

        elif isinstance(other, Complex) and self.imag == other.imag and self.real == other.real:
            return True
        return False

    def setimag(self, imag: int | float) -> None:

        self.__init__(self.real, imag)

    def setreal(self, real: int | float) -> None:

        self.__init__(real, self.imag)

    def getreal(self) -> int | float:

        return self.real

    def getimag(self) -> int | float:

        return self.imag
