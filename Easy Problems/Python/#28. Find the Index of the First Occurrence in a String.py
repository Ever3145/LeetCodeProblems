def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
            return i
    return -1