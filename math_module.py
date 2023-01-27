"""A module adding extra custom operations to integers."""


class IncompatibleOperandError(Exception):
    """A general exception for when operands are incomatible."""

    def __init__(self):
        self.msg = "The given operands are not compatible."

    def __str__(self):
        return self.msg


class IncompatibleMultiplierError(IncompatibleOperandError):
    """Given operands are not compatible becuase their multipliers
        do not match."""

    def __init__(self):
        super(IncompatibleMultiplierError, self).__init__()
        self.msg += ("\n\tThe multipliers of the given operands do"
                     "not match!")


class IncompatibleModulusError(IncompatibleOperandError):
    """Given operands are not compatible becuase their modulos
        do not match."""

    def __init__(self):
        super(IncompatibleModulusError, self).__init__()
        self.msg += ("\n\tThe modulos of the given operands do"
                     "not match!")


class WrappedInteger:
    """Acutal WrappedInteger class adding extra custom operations"""

    def __init__(self, obj, mod, alpha):
        self.object = obj
        self.mod = mod
        self.alpha = alpha

    # overwrite "print"
    def __str__(self):
        return f"<{str(self.object)} mod {str(self.mod)} | {str(self.alpha)} >"

    # define "*"
    def __mul__(self, other):
        """x * y = (x + y -αxy) mod n"""

        if self.mod != other.mod:   # modulos of operands do not match
            raise IncompatibleModulusError
        if self.alpha != other.alpha:   # multipliers of operands do not match
            raise IncompatibleMultiplierError

        x = self.object
        y = other.object
        a = self.alpha
        n = self.mod

        # return (x + y -αxy) mod n
        return WrappedInteger((x + y - a * x * y) % n, n, a)
