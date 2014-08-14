import re
def checkio(data):
     
    return (len(data) >= 10) and (re.search('[a-z]+', data) != None) and \
           (re.search('[A-Z]+', data) != None) and (re.search('[0-9]+', data) != None)
     
 
#Some hints
#Just check all conditions
 
'''
# Solution 2
import re
 
DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')
 
def checkio(data):
    """
    Return True if password strong and False if not
     
    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False
     
    if not DIGIT_RE.search(data):
        return False
 
    if not UPPER_CASE_RE.search(data):
        return False
 
    if not LOWER_CASE_RE.search(data):
        return False
         
    return True
'''    

if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print('All ok')