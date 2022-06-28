def findFirstRepeatedN(firstList, secondList):
    breakOutFlag = False
    output = 0
    #firstList = sorted(firstList)
    #secondList = sorted(secondList)

    for x in firstList:
        for y in secondList:
            if x == y:
                output = x
                breakOutFlag = True
                break

        if breakOutFlag == True:
            break

    return output