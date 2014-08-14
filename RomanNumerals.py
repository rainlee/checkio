def checkio(data):
     
    romans = [ ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],  
               ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],  
               ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],  
               ["", "M", "MM", "MMM", "", "", "", "", "", ""] ]
     
    sroman = ''
    i = 0
    while data != 0:
        sroman = romans[i][data%10] + sroman
        data //= 10
        i += 1
     
    return sroman