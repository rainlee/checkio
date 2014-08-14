def checkio(number):
    i = pigeon = 1   
    n = 1
    number -= 1
    while number > 0:
        i += 1
        pigeon += i        
        n = max(n, min(number, pigeon))
        number -= pigeon
         
    return n