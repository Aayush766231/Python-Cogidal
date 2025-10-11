class RomanConverter:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    def int_to_roman(self, num):
        if not (0 < num < 4000):
            raise ValueError("Number must be between 1 and 3999")
        result = ""
        for value, numeral in self.value_map:
            while num >= value:
                result += numeral
                num -= value
        return result
    
def main():
    print("Roman Numeral Converter")
    try:
        number = int(input("Enter an integer between 1 and 3999: "))
        converter = RomanConverter()
        roman_numeral = converter.int_to_roman(number)
        print(f"Roman numeral: {roman_numeral}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
