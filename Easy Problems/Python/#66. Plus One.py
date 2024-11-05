
def plusOne(digits):
    final = 0
        
    for i in range(len(digits)-1, -1, -1):
        final += digits[i] * (10 ** (len(digits) - 1 - i))
    final += 1

    final = str(final)
    finalList = []
    for i in range(len(final)):
        finalList.append(int(final[i]))

    return finalList
