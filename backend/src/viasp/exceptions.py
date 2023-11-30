"""
Exceptions
"""

class InvalidSyntax(Exception):
    """
    Exception returned when the input syntax is not expected
    """
    def __init__(self, *args):
        super().__init__("\n".join(str(arg) for arg in args))
