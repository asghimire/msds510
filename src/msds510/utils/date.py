"""This module contains all the utility functions needed"""
import re
import datetime
from time import strptime


def get_date_joined(year, month):
    """

    :param year: takes year as argument
    :param month: takes month as argument
    :return: date joined
    """
    try:
        year = int(year)
        formatted_month = re.sub("[^a-zA-Z]+", "", month)
        formatted_month = (strptime(formatted_month, '%b').tm_mon)
        return(datetime.date(year,formatted_month,1))
    except ValueError:
        return None
    except TypeError:
        return None

def days_since_joined(year, month):
    """

        :param year: takes year as argument
        :param month: takes month as argument
        :return: number of days since avenger joined
        """
    date_joined_input = get_date_joined(year=year, month=month)
    Todays_date = datetime.date.today()
    number_of_days_since_joined = str((Todays_date-date_joined_input))
    return (number_of_days_since_joined)

if __name__ == '__main__':
     print(get_date_joined(1985,'may'))
     print(days_since_joined('1963', 'sep'))
