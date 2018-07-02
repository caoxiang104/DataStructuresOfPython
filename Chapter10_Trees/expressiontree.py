class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self._data = data

    def postfix(self):
        return str(self)

    def infix(self):
        return str(self)

    def prefix(self):
        return str(self)

    def value(self):
        return int(self._data)

    def __str__(self):
        return str(self._data)


class InteriorNode(object):
    """Represents an operator and its two operator."""

    def __init__(self, op, leftOper, rightOper):
        self._operator = op
        self._leftOperand = leftOper
        self._rightOperand = rightOper

    def postfix(self):
        return self._leftOperand.postfix() + " " + \
            self._rightOperand.postfix() + " " + \
            self._operator

    def infix(self):
        return self._leftOperand.infix() + " " + \
            self._operator + " " + self._rightOperand.infix()

    def prefix(self):
        return self._operator + " " + self._leftOperand.prefix() + \
           " " + self._rightOperand.prefix()

    def value(self):
        if self._operator == '+':
            return self._leftOperand.value() + self._rightOperand.value()
        elif self._operator == '-':
            return self._leftOperand.value() - self._rightOperand.value()
        elif self._operator == '*':
            return self._leftOperand.value() * self._rightOperand.value()
        elif self._operator == '/':
            return self._leftOperand.value() / self._rightOperand.value()
        else:
            raise IndexError("Expression symbol is error")


def main():
    a = LeafNode(4)
    b = InteriorNode('+', LeafNode(2), LeafNode(3))
    c = InteriorNode('*', a, b)
    c = InteriorNode('-', c, b)

    print("Infix", c.infix())
    print("Postfix", c.postfix())
    print("Prefix", c.prefix())
    print("Value", c.value())


if __name__ == '__main__':
    main()