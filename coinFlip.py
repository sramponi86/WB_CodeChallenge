def coinFlip(flip):
    changeWithLeadingZero = 0
    changeWithLeadingOne = 0
    if len(flip) <= 1:
        return False
    else:
        for idx, x in enumerate(flip):
            if (x == 1 - (idx%2)):
                changeWithLeadingZero += 1
            if (x == (idx%2)):
                changeWithLeadingOne += 1
        return min(changeWithLeadingZero,changeWithLeadingOne)
