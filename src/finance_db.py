"""
This Class creates dataframes with Security Master Type Info on Equities
"""
import financedatabase as fd


class Equity:
    """
    This Class has function to pull in equities of different countries, 
    sectors, industries, exchanges etc.
    """
    def __init__(self, country: str = 'USA') -> None:
        self.country = country

    def __repr__(self):
        return f'Country: {self.country}'

    @staticmethod
    def countries():
        """
        Obtain ALL countries
        """
        return list(fd.Equities().options('country'))

    @staticmethod
    def sectors():
        """
        Obtain ALL Sectors
        """
        return list(fd.Equities().options('sector'))

    @staticmethod
    def industry_group():
        """
        Obtain ALL Industry Groups
        """
        return list(fd.Equities().options('industry_group'))

    @staticmethod
    def industry():
        """
        Obtain ALL Industries
        """
        return list(fd.Equities().options('industry'))

    @staticmethod
    def exchange():
        """
        Obtain ALL Exchanges
        """
        return list(fd.Equities().options('exchange'))

    @staticmethod
    def equities_country(country:str):
        """
        List of Countries
        """
        return fd.Equities().search(country)

    @staticmethod
    def equities_exchange(exchange: str):
        """
        List of Exchanges
        """
        return fd.Equities().search(exchange=exchange)


def main():
    """
    Main Python Program
    """
    equities = Equity(country='USA')
    nyse = equities.equities_exchange(exchange='NYSE')
    print(nyse)


if __name__ == '__main__':
    main()
