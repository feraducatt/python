# two different class scripts
# both convert roman numerals to numbers and vice-versa depending on the method called
# for both, the same object can be called for different numbers and numerals
# the second uses decorations


class RomanNumerals(object):
    def __init__(self):
        self.dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                     'V': 5, 'IV': 4, 'I': 1}

    def to_roman(self, number):
        self.numeral = ''
        return self.to_roman_act(number)

    def to_roman_act(self, number):
        counter = number
        for key, value in self.dict.items():
            if counter >= value:
                self.numeral += key
                counter -= value
                if not (counter == 0):
                    self.to_roman_act(counter)
                return self.numeral

    def from_roman(self, numeral):
        self.number = 0
        return self.from_roman_act(numeral)

    def from_roman_act(self, numeral):
        num = numeral
        for key, value in self.dict.items():
            if num[0] == key:
                self.number += value
                num = num[1:len(num)]
                if not (num == ''):
                    self.from_roman_act(num)
                return self.number
            elif num[0:2] == key:
                self.number += value
                num = num[2:len(num)]
                if not (num == ''):
                    self.from_roman(num)
                return self.number




class RomanNumerals:
    @classmethod
    def to_roman(self, number):
        dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                'V': 5, 'IV': 4, 'I': 1}
        numeral = ''
        counter = number
        while not (counter == 0):
            for key, value in dict.items():
                if counter == 0:
                    return numeral
                if counter >= value:
                    numeral += key
                    counter -= value
        return numeral

    @classmethod
    def from_roman(self, numeral):
        dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                'V': 5, 'IV': 4, 'I': 1}
        number = 0
        num = numeral
        while not (num == ''):
            for key, value in dict.items():
                if num == '':
                    return number
                if num[0] == key:
                    number += value
                    num = num[1:len(num)]
                elif num[0:2] == key:
                    number += value
                    num = num[2:len(num)]
        return number

print(RomanNumerals().to_roman(144))
print(RomanNumerals().from_roman('MMXLIII'))

print(RomanNumerals.to_roman(144))
print(RomanNumerals.from_roman("MMXLIII"))