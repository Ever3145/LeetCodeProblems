def isPalindrome(s):
    x = 0
    y = len(s)

    correct = ""

    for i in range(x, y):
        if s[i].isalnum():
            correct += s[i]
        else:
            continue
    return correct[::-1].lower() == correct.lower()