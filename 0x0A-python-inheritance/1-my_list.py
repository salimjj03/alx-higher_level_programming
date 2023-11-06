#!/usr/bin/python3
"""

In this module a class inherits from a list.

"""


class MyList(list):
    """ This Class dose the work.

    """

    def print_sorted(self):
        """ This method  sort the list.

        """
        print(sorted(self))
