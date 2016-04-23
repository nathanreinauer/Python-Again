def sortFunc(*arg):

    numList = list(arg)                     # Converts arguments into a list
    print('Before sorting: ',numList)       # Prints that list before sorting happens
    numSort = []                            # Creates an empty list to put sorted numbers into
    i = 0                                   # This is the index
    a = 1                                   # 'a' is the comparison number (this is the magic sauce)

    while numList:                          # As long as numList has numbers in it, loop the following
    
        if numList[i] == numList[-1] and\
           numList[i] <= a:                 # If we're at the final index AND that last number is smaller than 'a'
            basket = numList.pop(i)         # then place that number in a basket
            numSort.append(basket)          # and dump the basket into the new list (numSort)
            i = 0

        elif numList[i] == numList[-1]:     # Otherwise, if we reach the last position in numList 
            i = 0                           # reset the index back to the first position
            a = a+1                         # and make the comparison number a little bigger

        elif numList[i] <= a:               # If we're anywhere else in the list and that number is smaller than 'a'
            basket = numList.pop(i)         # then pop that number into the basket
            numSort.append(basket)          # and dump it unceremoniously into the new list (numSort)
            i = 0                           # Then reset the index back to the first position
            a = a+1                         # and make the comparison number a little bigger
        
        else:                               # If none of those things happen
            i = i+1                         # then move on to the next number in the list

    print('After sorting: ',numSort)        # Once the while loop is up, print the result!

    
sortFunc(67, 45, 2, 13, 1, 998)             # These numbers are arbitrary, could be anything
                                            # as long as each number is different.