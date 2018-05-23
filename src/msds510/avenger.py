import datetime
from src.msds510.utils.date import*
from src.msds510.utils.conversion import*


class Avenger:
    def __init__(self, record):
        """
        Initializes the object with a dictionary-based record.

        Args:
            record (dict): Dictionary-based record of Avenger data
        """
        self.record = record

    def url(self):
        """
        Returns:
            str: The URL of the comic character on the Marvel Wikia

        """

        return self.record.get('url')

    def name_alias(self):
        """

        Returns:
            str: The full name or alias of the character

        """

        return self.record.get('name_alias')

    def appearances(self):
        """

        Returns:
            int: The number of comic books that
            character appeared in as of April 30

        """
        int_appearances = to_int(self.record.get('appearances'))
        return int_appearances

    def is_current(self):
        """
        Returns:
            bool: Is the member currently active on
            an avengers affiliated team? (True/False)
        """
        c = self.record.get('current')
        if c == 'YES':
            return True
        else:
            return False

    def gender(self):
        """

        Returns:
            str: The recorded gender of the character

        """
        return self.record.get('gender')

    def year(self):
        """
        Returns:
            int: The year the character was introduced as a
            full or reserve member of the Avengers
        """
        int_year = int(self.record.get('year'))
        return int_year

    def date_joined(self):
        """

        Returns:
            datetime.date: The date the character joined
            """
        year = int(self.record.get('year'))
        date_joined = get_date_joined(year,
                                      self.record.get('full_reserve_avengers_intro')
                                      )
        return date_joined

    def days_since_joining(self):
        """
            Returns:
            int: The number of integer days since the character joined
            """

        year = int(self.record.get('year'))
        month = self.record.get('full_reserve_avengers_intro')
        days = days_since_joined(year, month)
        return days

    def years_since_joining(self):
        """
        Returns:
            int: The number of integer years since the character joined
        """
        today_year = datetime.date.today().year
        yearsSinceJoining = today_year - int(self.record.get('year'))
        return yearsSinceJoining

    def notes(self):
        """STRIP OFF TRAILING NEWLINES AND SPACES
        Returns:
            str: Descriptions of deaths and resurrections.

        """
        formatted_notes = self.record.get('notes').strip('\n').strip(' ')
        return formatted_notes

    def to_markdown(self):
        print('Name/Alias: {}'.format(hank_pym.name_alias()))
        print('URL: {}'.format(hank_pym.url())),
        print('Appearances: {}'.format(hank_pym.appearances()))
        print('Is Current?: {}'.format(hank_pym.is_current()))
        print('Gender: {}'.format(hank_pym.gender()))
        print('Year Joined: {}'.format(hank_pym.year()))
        print('Date Joined: {}'.format(hank_pym.date_joined()))
        print('Days Since Joined: {}'.format(hank_pym.days_since_joining()))
        print('Years Since Joined: {}'.format(hank_pym.years_since_joining()))
        print('Notes: {}'.format(hank_pym.notes()))
        print('__str__: {}'.format(hank_pym.__str__()))
        print('__repr__: {}'.format(hank_pym.__repr__()))

    def __str__(self):
        """
        Returns:
            str: A human-readable value for this character
        """
        return self.record.__str__()

    def __repr__(self):
        """

        Returns:
            str: String representation of object.  Useful for debugging.
        """
        return " Avenger:%s " % (self.record)




if __name__ == '__main__':
    pym_record = {
        'appearances': '1269',
        'current': 'YES',
        'death1': 'YES',
        'death2': '',
        'death3': '',
        'death4': '',
        'death5': '',
        'full_reserve_avengers_intro': 'Sep-63',
        'gender': 'MALE',
        'honorary': 'Full',
        'name_alias': 'Henry Jonathan "Hank" Pym',
        'notes': 'Merged with Ultron in Rage of Ultron Vol. 1. A funeral was held.',
        'probationary_introl': '',
        'return1': 'NO',
        'return2': '',
        'return3': '',
        'return4': '',
        'return5': '',
        'url': 'http://marvel.wikia.com/Henry_Pym_(Earth-616)',
        'year': '1963',
        'years_since_joining': '52'
    }

    hank_pym = Avenger(pym_record)
    hank_pym.to_markdown()

