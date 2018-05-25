"""This module contains all the utility functions needed"""


def to_int(input):
    """ This function takes the input and converts them into integer
    :arg: any input
    :returns: integer of that input
    """
    try:
        output = int(float(input))
        return output
    except ValueError:
        return None


def get_value(input, value):
    """

    :param input: takes any input dict. list, tuple or string
    :param value: takes desired value as a argument
    :return: function returns the position of the element
    if the input is list/tuple; returns value of the key if the input is dict.
    """
    if isinstance(input, list) or isinstance(input, tuple):
        try:
            element = value
            return input.index(element)

        except KeyError:
            return None
        except ValueError:
            return None

    elif isinstance(input, dict):
        try:
            for index in range(len(input)):
                index = value
                return input[index]
        except KeyError:
            return None

    else:
        return None


if __name__ == '__main__':
    try:
        print(to_int('msds'))
        print(to_int('2.23456 '))
        # This block lets user know if the input passed
        # to the function is string without quotes.
        # This will handle NameError exception
        # when testing the function
        print(to_int(husband))

    except NameError:
        print('Your input is not valid. For strings, put it inside'
              ' quotes when passing the input to the function'
              )

        x = {'a': '1', 'b': '52', 'd': '6'}
        y = ['a', 'c', 'd']
        z = ('d', 'e', 'f')

        print(get_value(z, 'e'))
        print(get_value(y, 'd'))
        print(get_value(x, 'b'))
        print(get_value(x, 'y'))  # testing for key that doesnot exist
        print(get_value(y, 'n'))  # testing for list element that doesnot exist
        print(get_value('arc', 'a'))
