#!/usr/bin/python3
"""

The class MyInt  inherits from int.

"""


class MyInt(int):
    """ The class that inherits.

    """

    def __eq__(self, value):
        """ The first method.

        """

        if isinstance(self, type(value)):
            return False

    def __ne__(self, value):
        """ The second method.

        """

        if isinstance(self, type(value)):
            return True
