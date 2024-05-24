class Number:
    def __init__(self) -> None:
        pass

    def check_number(self, number: str) -> None:
        if not number.isdigit():
            print(f"+{number} is not a valid number. The number must consist of numbers. Spaces and any other elements are not accepted!")
            return False
        elif len(number) > 12 or len(number) <= 3:
            print(f"+{number} is not valid number. Length of number must be at least 3 and at most 12!")
            return False
        return True 