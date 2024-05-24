from helpers.countries import country_codes

class Country:
    def __init__(self) -> None:
        pass

    def show_countries(self) -> None:
        print("List of the countries and their phone codes ---> ")
        for con in country_codes:
            print(f"{con} ---> +{country_codes[con]}")

    def check_country(self, number: str) -> None:
        for con in country_codes:
            if number.startswith(country_codes[con]):
                self.country = con
        return self.country