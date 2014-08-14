#Your optional code here
#You can import some modules or create additional functions


#def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  
    '''
    # Solution 1
    multidata = []
    for i in data:
        if data.count(i) > 1:
            multidata.append(i);

    return multidata
    '''
  
    # Solution 2
#    return [x for x in data if data.count(x) > 1]

# Solution 3
checkio = lambda d : [x for x in d if d.count(x) > 1]

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
