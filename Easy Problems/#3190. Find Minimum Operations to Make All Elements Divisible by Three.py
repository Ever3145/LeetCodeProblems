def minimumOperations(nums):
    n = 0
    
    for i in nums:
        if i % 3 == 0:
            continue
        elif i % 3 == 1:
            n += 1
        else:
            n += 1
    return n