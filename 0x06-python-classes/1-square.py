#!/usr/bin/python3


"""Example mple Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

"""


class Square:
    """The summary line for a class docstring should fit on one line.

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.

    """

    def __init__(self, size):

        """

        A special fun
        Args:
        siz (int): .....

        """
        self.__size = size
