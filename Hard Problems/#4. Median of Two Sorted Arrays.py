def MedianSortArray(nums1, nums2):
    nums3 = nums1 + nums2
    nums3.sort()

    median = 0
    if len(nums3) == 1:
        return nums3[0]

    middle_index = (len(nums3) - 1) / 2

    if middle_index % 2 == 0 or int(middle_index) == middle_index:
        median = nums3[int(middle_index)]
    elif middle_index - 0.5 == int(middle_index):
        median = (nums3[int(middle_index)] + nums3[int(middle_index)+1]) / 2
    elif int(middle_index) == middle_index:
        median = nums3[int(middle_index)]

    return median
