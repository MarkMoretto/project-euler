
"""
Purpose: Project euler problem
Date created: 2021-03-31

Problen Number: 17
Name: Number letter counts
URL: https://projecteuler.net/problem=17

Contributor(s):
    Mark M.
"""

import re



class NumWordCollections:
    ones_dict = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            }
    
    tens_dict = {
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety",
            }
    
    thousands_dict = {
            1: "thousand",
            2: "million",
            3: "billion",
            4: "trillion",
            5: "quadrillion",
            6: "quintillion",
            7: "sextillion",
            8: "septillion",
            9: "octillion",
            10: "nonillion",
            11: "decillion",
            }


class NumToWord(NumWordCollections):

    def __init__(self):
        pass


    def __join(self, *args):
        return " ".join(filter(bool, args))


    def __get_word_number(self, N):
        if N < 20:
            return self.ones_dict[N]

        if N < 100:

            d, m = divmod(N, 10)
            return self.__join(self.tens_dict[d],
                               self.ones_dict[m])

        if N < 1000:
            if N % 100 == 0:
                return self.__divide(N, 100, "hundred")
            return self.__divide(N, 100, "hundred and")

        for k, v in self.thousands_dict.items():
            if N < 1000 ** (k + 1):
                break

        return self.__divide(N, 1000 ** k, v)


    def __divide(self, dividend, divisor, magnitude):

        d, m = divmod(dividend, divisor)

        return self.__join(self.__get_word_number(d),
                           magnitude,
                           self.__get_word_number(m),
                           )

    def get_word(self, number):
        if number < 0:
            return self.__join("negative", self.__get_word_number(-number))

        if number == 0:
            return "zero"
        return self.__get_word_number(number)




def test_NumToWord(verbose: bool = False):
    test_n2w = NumToWord()

    testdict = dict(
            number = [342, 115],
            string = [test_n2w.get_word(342), test_n2w.get_word(115)],
            expected = [23, 20],
            )
    
    
    max_len = max(map(len, testdict.values()))
    
    for i in range(max_len):
        number_ = testdict["number"][i]
        string_ = testdict["string"][i].replace(" ", "")
        expected_ = testdict["expected"][i]
        string_len = len(string_)
        assert (expected_ == string_len), f"Len. assertion error on {number_}"
        if verbose:
            print(f"The length of {number_} is {string_len} vs {expected_} expected.")


def main(max_number):

    n2w = NumToWord()

    tot: int = 0

    for i in range(1, max_number + 1):
        numword: str = n2w.get_word(i)
        tot += len(str(numword).replace(" ", ""))
    print(f"The sum of character counts for words from 1 to {max_number} is: {tot:,}.")


# n2w = NumToWord()
# for i in range(1, 11):
#     numword = n2w.get_word(i)
#     wordlen = len(numword.replace(" ", ""))
#     print(i, " -> ", numword, " : ", wordlen)

#     tot += len(numword.replace(" ", ""))


# n2w.get_word(9)
# n2w.get_word(99)
# n2w.get_word(111)
# n2w.get_word(999)
# n2w.get_word(499)
# n2w.get_word(500)
# n2w.get_word(501)
# n2w.get_word(1000**1)
# n2w.get_word(1000**2)
# n2w.get_word(1000**3)
# n2w.get_word(999999)
# n2w.get_word(342)

if __name__ == "__main__":
    main(1000)