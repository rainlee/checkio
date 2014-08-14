def checkio(text):
     
    maxcnt = 0
    maxc = ''
    ltext = text.lower()
    for x in range(ord('a'), ord('z')+1):
        tmp = ltext.count(chr(x))
        if tmp > maxcnt:
            maxcnt = tmp;
            maxc = chr(x)
    return maxc