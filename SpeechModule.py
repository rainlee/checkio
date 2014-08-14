FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
 
 
def checkio(number):
     
    snum = []
    if number >= 100:
        hd = number // 100
        snum.append(FIRST_TEN[hd-1])
        snum.append(HUNDRED)
        number %= 100
     
    if number >= 20:
        snum.append(OTHER_TENS[number//10 - 2])
        if number%10 != 0:
            snum.append(FIRST_TEN[number%10 - 1])
    elif number >= 10:
        snum.append(SECOND_TEN[number-10])
    elif number > 0:
        snum.append(FIRST_TEN[number-1])
     
    return ' '.join(snum)